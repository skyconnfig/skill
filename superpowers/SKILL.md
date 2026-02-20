---
name: superpowers
description: Complete software development workflow for coding agents - skills framework with TDD, planning, and subagent-driven development
license: MIT
compatibility: opencode
metadata:
  audience: developers
  use-case: software-development
  workflow: agentic-development
---

# Superpowers - Agentic Skills Framework

Complete software development workflow for coding agents, built on composable "skills" that trigger automatically to ensure agents follow best practices.

## The Core Workflow

1. **brainstorming** - Refines rough ideas through questions, explores alternatives, presents design in sections for validation
2. **using-git-worktrees** - Creates isolated workspace on new branch, runs project setup, verifies clean test baseline
3. **writing-plans** - Breaks work into bite-sized tasks (2-5 minutes each) with exact file paths and verification steps
4. **subagent-driven-development** or **executing-plans** - Dispatches subagent per task with two-stage review (spec compliance, then code quality)
5. **test-driven-development** - Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass
6. **requesting-code-review** - Reviews against plan, reports issues by severity
7. **finishing-a-development-branch** - Verifies tests, presents merge/PR/keep/discard options

## Available Skills

### Testing

- **test-driven-development** - RED-GREEN-REFACTOR cycle with testing anti-patterns reference

### Debugging

- **systematic-debugging** - 4-phase root cause process (root-cause-tracing, defense-in-depth, condition-based-waiting)
- **verification-before-completion** - Ensure fixes are actually working

### Collaboration

- **brainstorming** - Socratic design refinement
- **writing-plans** - Detailed implementation plans
- **executing-plans** - Batch execution with checkpoints
- **dispatching-parallel-agents** - Concurrent subagent workflows
- **requesting-code-review** - Pre-review checklist
- **receiving-code-review** - Responding to feedback
- **using-git-worktrees** - Parallel development branches
- **finishing-a-development-branch** - Merge/PR decision workflow
- **subagent-driven-development** - Fast iteration with two-stage review

### Meta

- **writing-skills** - Create new skills following best practices
- **using-superpowers** - Introduction to the skills system

## Philosophy

- **Test-Driven Development** - Write tests first, always
- **Systematic over ad-hoc** - Process over guessing
- **Complexity reduction** - Simplicity as primary goal
- **Evidence over claims** - Verify before declaring success

## When to Use

Use this skill when:
- Starting a new development task that requires planning
- Working on features that need TDD approach
- Needing systematic debugging methodology
- Managing complex multi-step implementations
- Coordinating subagent workflows
- Reviewing code against specifications

## Key Principles

The agent checks for relevant skills **before any task**. These are mandatory workflows, not suggestions.

## Installation

For OpenCode:
```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
```

## References

- Source: https://github.com/obra/superpowers
- Documentation: https://github.com/obra/superpowers/tree/main/docs
- Blog: https://blog.fsck.com/2025/10/09/superpowers/
