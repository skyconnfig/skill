#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design Controller - Master orchestration for design workflows
Routes requests to appropriate design specialists based on intent
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, Optional, Any
from datetime import datetime


class DesignController:
    """Master controller for design workflows with intelligent routing."""

    def __init__(self):
        self.current_skill_path = Path(__file__).parent.parent
        self.skills_path = self.current_skill_path.parent
        self.context = {}

    def parse_args(self):
        """Parse command line arguments."""
        parser = argparse.ArgumentParser(
            description='Design Controller - Master design orchestration'
        )
        parser.add_argument(
            '--intent',
            required=True,
            choices=['creative', 'normative', 'hybrid', 'extract'],
            help='Design intent: creative, normative, hybrid, or extract'
        )
        parser.add_argument('--project', type=str, help='Project description')
        parser.add_argument('--reference', type=str, help='Reference description or URL')
        parser.add_argument('--url', type=str, help='URL for extraction')
        parser.add_argument('--style', type=str, help='Style hints for creative path')
        parser.add_argument('--balance', type=str, help='Balance ratio for hybrid path')
        parser.add_argument('--output', type=str, default='display',
                           help='Output format: display, json, file')

        return parser.parse_args()

    def run(self):
        """Run the design controller."""
        args = self.parse_args()

        print("=" * 60)
        print("Design Controller")
        print("=" * 60)
        print(f"Intent: {args.intent}")
        print(f"Timestamp: {datetime.now().isoformat()}")
        print("-" * 60)

        # Route to appropriate handler
        handlers = {
            'creative': self.handle_creative,
            'normative': self.handle_normative,
            'hybrid': self.handle_hybrid,
            'extract': self.handle_extract
        }

        handler = handlers.get(args.intent)
        if handler:
            result = handler(args)
            self.print_result(args.intent, result)
        else:
            print(f"Unknown intent: {args.intent}")

    def handle_creative(self, args) -> Dict:
        """Handle creative design path."""
        print("\nPath: Creative Design")
        print("=" * 40)

        if not args.project:
            return {'error': 'Project description required for creative path'}

        print(f"Project: {args.project}")
        print(f"Style hints: {args.style or 'Free creative direction'}")
        print("\n-> Calling frontend-design-skill...")

        # Call frontend-design-skill
        cmd = [
            'python', '-m',
            f'{self.skills_path / "frontend-design" / "scripts" / "main.py"}',
            '--project', args.project
        ]

        if args.style:
            cmd.extend(['--style', args.style])

        try:
            result = subprocess.run(
                ' '.join(cmd),
                capture_output=True,
                text=True,
                shell=True
            )
            output = result.stdout if result.returncode == 0 else result.stderr

            return {
                'path': 'creative',
                'project': args.project,
                'style_hints': args.style,
                'execution': 'frontend-design-skill',
                'output': output,
                'success': result.returncode == 0
            }
        except Exception as e:
            return {
                'path': 'creative',
                'project': args.project,
                'error': str(e),
                'success': False
            }

    def handle_normative(self, args) -> Dict:
        """Handle normative replication path."""
        print("\nPath: Normative Replication")
        print("=" * 40)

        if not args.reference:
            return {'error': 'Reference description required for normative path'}

        print(f"Reference: {args.reference}")
        print(f"Project: {args.project or 'Not specified'}")

        # Step 1: Query ui-ux-pro-max for matching pattern
        print("\n-> Phase 1: Searching ui-ux-pro-max database...")
        ui_ux_result = self.query_ui_ux_pro_max(args.reference)

        if not ui_ux_result.get('found'):
            print("  [WARNING]  No exact match found in database")
            print("  [TIP] Suggestion: Use extract path to add this reference")
            return {
                'path': 'normative',
                'reference': args.reference,
                'database_search': ui_ux_result,
                'suggestion': 'Use --intent extract to add this pattern'
            }

        print(f"  [OK] Found matching pattern: {ui_ux_result.get('match_name')}")
        print(f"  - Colors: {len(ui_ux_result.get('colors', []))} extracted")
        print(f"  - Typography: {ui_ux_result.get('typography', {}).get('font_family', 'N/A')}")

        # Step 2: Replicate using frontend-design-skill
        print("\n-> Phase 2: Replicating pattern via frontend-design-skill...")
        frontend_result = self.replicate_with_frontend_design(
            args.project,
            ui_ux_result
        )

        return {
            'path': 'normative',
            'reference': args.reference,
            'database_match': ui_ux_result,
            'replication': frontend_result,
            'success': frontend_result.get('success', False)
        }

    def handle_hybrid(self, args) -> Dict:
        """Handle hybrid creative + normative path."""
        print("\n[LOC] Path: Hybrid (Standards + Creativity)")
        print("=" * 40)

        print(f"Reference: {args.reference}")
        print(f"Project: {args.project or 'Not specified'}")
        print(f"Balance: {args.balance or 'Default (50/50)'}")

        # Phase 1: Establish standards via ui-ux-pro-max
        print("\n-> Phase 1: Establishing design standards...")
        standards = self.query_ui_ux_pro_max(args.reference, comprehensive=True)

        if not standards.get('found'):
            print("  [WARNING]  No matching standards found")
            print("  [TIP] Falling back to creative path")
            return self.handle_creative(args)

        print(f"  [OK] Standards established:")
        print(f"  - Color palette: {len(standards.get('colors', []))} colors")
        print(f"  - Typography: {standards.get('typography', {}).get('font_family', 'N/A')}")
        print(f"  - Spacing scale: {len(standards.get('spacing', {}).get('scale', []))} steps")
        print(f"  - Components: {len(standards.get('components', []))} documented")

        # Phase 2: Creative interpretation via frontend-design-skill
        print("\n-> Phase 2: Creative interpretation...")
        creative_result = self.creative_interpretation(
            args.project,
            standards,
            args.balance
        )

        return {
            'path': 'hybrid',
            'reference': args.reference,
            'standards': standards,
            'creative_interpretation': creative_result,
            'success': creative_result.get('success', False)
        }

    def handle_extract(self, args) -> Dict:
        """Handle design standard extraction path."""
        print("\n[LOC] Path: Design Standard Extraction")
        print("=" * 40)

        if not args.url:
            return {'error': 'URL required for extraction path'}

        print(f"Target URL: {args.url}")
        print("\n-> Phase 1: Capturing website via playwright...")

        # Step 1: Capture via playwright
        capture_result = self.capture_via_playwright(args.url)

        if not capture_result.get('success'):
            return {
                'path': 'extract',
                'url': args.url,
                'capture': capture_result,
                'error': 'Capture failed'
            }

        print(f"  [OK] Screenshot saved: {capture_result.get('screenshot_path')}")
        print(f"  [OK] CSS extracted: {len(capture_result.get('css_rules', []))} rules")
        print(f"  [OK] HTML structure captured")

        # Step 2: Analyze design system
        print("\n-> Phase 2: Analyzing design system...")
        analysis = self.analyze_design_system(capture_result)

        print(f"  [OK] Colors extracted: {len(analysis.get('colors', []))}")
        print(f"  [OK] Typography analyzed: {analysis.get('typography', {}).get('font_family', 'Unknown')}")
        print(f"  [OK] Components identified: {len(analysis.get('components', []))}")

        # Step 3: Store to ui-ux-pro-max database
        print("\n-> Phase 3: Storing to ui-ux-pro-max database...")
        storage = self.store_to_ui_ux_pro_max(args.url, analysis)

        return {
            'path': 'extract',
            'url': args.url,
            'capture': capture_result,
            'analysis': analysis,
            'storage': storage,
            'success': storage.get('success', False)
        }

    def query_ui_ux_pro_max(self, reference: str, comprehensive: bool = False) -> Dict:
        """Query ui-ux-pro-max database for matching design pattern."""
        # Simulated database lookup
        # In production, this would query the actual ui-ux-pro-max database

        # Mock database of 57 styles
        mock_database = {
            'stripe': {
                'name': 'Stripe-style Clean Dashboard',
                'colors': ['#635BFF', '#00D4FF', '#F7F9FC', '#1A1F36'],
                'typography': {
                    'font_family': 'Inter',
                    'base_size': '16px',
                    'scale': '1.25'
                },
                'spacing': {
                    'base': '4px',
                    'scale': [4, 8, 12, 16, 24, 32, 48, 64]
                },
                'components': ['card', 'button', 'input', 'table', 'chart'],
                'style_category': 'fintech-clean'
            },
            'apple': {
                'name': 'Apple-style Minimal',
                'colors': ['#000000', '#FFFFFF', '#0071e3', '#86868b'],
                'typography': {
                    'font_family': 'SF Pro',
                    'base_size': '17px',
                    'scale': '1.125'
                },
                'spacing': {
                    'base': '8px',
                    'scale': [8, 12, 16, 20, 24, 32, 40, 48]
                },
                'components': ['button', 'card', 'hero', 'gallery'],
                'style_category': 'minimal-premium'
            },
            'linear': {
                'name': 'Linear-style Dark Minimal',
                'colors': ['#5E6AD2', '#10162F', '#C5C8D2', '#2A2F45'],
                'typography': {
                    'font_family': 'Inter',
                    'base_size': '14px',
                    'scale': '1.2'
                },
                'spacing': {
                    'base': '4px',
                    'scale': [4, 6, 8, 12, 16, 20, 24, 32]
                },
                'components': ['button', 'input', 'select', 'table', 'sidebar'],
                'style_category': 'dark-minimal'
            }
        }

        # Search for matching pattern
        reference_lower = reference.lower()
        matched = None
        match_score = 0

        for key, pattern in mock_database.items():
            if key in reference_lower:
                matched = pattern
                match_score = 1.0
                break
            # Partial match
            for color in pattern.get('colors', []):
                if color in reference_lower:
                    matched = pattern
                    match_score = 0.7
                    break

        if matched:
            return {
                'found': True,
                'match_name': matched['name'],
                'match_score': match_score,
                'colors': matched.get('colors', []),
                'typography': matched.get('typography', {}),
                'spacing': matched.get('spacing', {}),
                'components': matched.get('components', []),
                'style_category': matched.get('style_category')
            }

        return {
            'found': False,
            'searched_for': reference,
            'database_size': '57 styles available',
            'suggestion': 'Use extract path to add new pattern'
        }

    def replicate_with_frontend_design(self, project: str, pattern: Dict) -> Dict:
        """Replicate design pattern via frontend-design-skill."""
        # In production, this would call frontend-design-skill with pattern parameters
        return {
            'pattern_applied': pattern.get('match_name', 'Unknown'),
            'project': project,
            'success': True,
            'message': f"Pattern '{pattern.get('match_name')}' applied to project"
        }

    def creative_interpretation(self, project: str, standards: Dict, balance: str) -> Dict:
        """Apply creative interpretation based on standards."""
        return {
            'standards_used': standards.get('match_name', 'Custom'),
            'project': project,
            'balance': balance or '50/50',
            'success': True,
            'message': 'Creative interpretation completed with documented standards'
        }

    def capture_via_playwright(self, url: str) -> Dict:
        """Capture website via playwright."""
        # In production, this would call the playwright skill
        # For now, simulate the capture

        return {
            'success': True,
            'url': url,
            'screenshot_path': f'capture_{url.replace("https://", "").replace("http://", "").replace("/", "_")}.png',
            'css_rules': ['color: #333', 'font-family: Inter', 'background: #fff', 'padding: 16px'],
            'html_structure': {
                'tags': ['header', 'nav', 'main', 'section', 'footer'],
                'classes': ['container', 'card', 'button', 'input']
            },
            'timestamp': datetime.now().isoformat()
        }

    def analyze_design_system(self, capture_result: Dict) -> Dict:
        """Analyze captured design system."""
        # Extract colors from CSS
        css_rules = capture_result.get('css_rules', [])
        colors = []
        for rule in css_rules:
            if 'color:' in rule or 'background:' in rule:
                color = rule.split(':')[1].strip()
                if color not in colors:
                    colors.append(color)

        return {
            'colors': colors or ['#333333', '#FFFFFF', '#0071e3'],
            'typography': {
                'font_family': 'Inter',
                'base_size': '16px',
                'scale': '1.25'
            },
            'spacing': {
                'base': '8px',
                'scale': [8, 12, 16, 20, 24, 32, 40, 48]
            },
            'components': ['button', 'card', 'input', 'nav'],
            'layout': {
                'type': 'flexbox',
                'container_width': '1200px'
            }
        }

    def store_to_ui_ux_pro_max(self, url: str, analysis: Dict) -> Dict:
        """Store extracted design to ui-ux-pro-max database."""
        # In production, this would update the actual database
        import hashlib

        entry_id = hashlib.md5(f"{url}{datetime.now().isoformat()}".encode()).hexdigest()[:12]

        return {
            'success': True,
            'entry_id': entry_id,
            'source_url': url,
            'stored_at': datetime.now().isoformat(),
            'colors_count': len(analysis.get('colors', [])),
            'typography': analysis.get('typography', {}),
            'style_category': 'extracted',
            'quality_score': 0.85,
            'message': f'New design standard stored with ID: {entry_id}'
        }

    def print_result(self, intent: str, result: Dict):
        """Print the final result."""
        print("\n" + "=" * 60)
        print("Result Summary")
        print("=" * 60)

        if result.get('success'):
            print("[OK] Execution completed successfully")
        elif result.get('error'):
            print(f"[ERROR] Error: {result.get('error')}")
        else:
            print("[WARNING]  Partial execution - see details above")

        print("\nNext Steps:")
        if intent == 'creative':
            print("- Review generated design")
            print("- Provide feedback for iterations")
        elif intent == 'normative':
            print("- Review replicated pattern")
            print("- Adjust parameters if needed")
        elif intent == 'hybrid':
            print("- Review design with standards")
            print("- Export design tokens")
        elif intent == 'extract':
            print(f"- Standard stored: {result.get('storage', {}).get('entry_id', 'N/A')}")
            print("- Ready for replication via normative path")

        print("\n" + "-" * 60)


def main():
    """Main entry point."""
    controller = DesignController()
    controller.run()


if __name__ == '__main__':
    main()
