#!/usr/bin/env python3
"""
Simplify extracted content for beginners with analogies and step-by-step explanations.
"""

import sys
import json
import re


# Common jargon dictionary with simple explanations and analogies
JARGON_DICT = {
    # Programming/Tech
    "api": {
        "explanation": "A way for different programs to talk to each other",
        "analogy": "Like a waiter in a restaurant - you (the program) tell the waiter what you want, and they bring it to the kitchen (server) and back to you"
    },
    "database": {
        "explanation": "A organized collection of information that can be easily accessed and updated",
        "analogy": "Like a digital filing cabinet where you can quickly find and store information"
    },
    "algorithm": {
        "explanation": "A set of steps to solve a problem or complete a task",
        "analogy": "Like a recipe - a list of instructions to make something"
    },
    "cloud": {
        "explanation": "Servers connected through the internet that store and process data",
        "analogy": "Like having your files in a virtual storage unit instead of your local computer - you can access them from anywhere"
    },
    "encryption": {
        "explanation": "Converting information into a secret code to prevent unauthorized access",
        "analogy": "Like speaking in a secret language that only you and your friend understand"
    },
    "blockchain": {
        "explanation": "A chain of data blocks where each block is linked and secured using cryptography",
        "analogy": "Like a shared diary that everyone can read, but once something is written, it can never be erased or changed"
    },
    "machine learning": {
        "explanation": "Computers learning patterns from data instead of being explicitly programmed",
        "analogy": "Like teaching a child by showing many examples - eventually they recognize patterns on their own"
    },
    "neural network": {
        "explanation": "A computer system inspired by how the human brain works",
        "analogy": "Like a team of experts passing information down a chain, each person adding their expertise"
    },
    "frontend": {
        "explanation": "The part of a website or app that users see and interact with",
        "analogy": "Like the storefront of a shop - what customers see and walk through"
    },
    "backend": {
        "explanation": "The behind-the-scenes part that handles data and logic",
        "analogy": "Like the warehouse and office behind a shop - where all the real work happens"
    },
    "server": {
        "explanation": "A computer that provides data or services to other computers",
        "analogy": "Like a librarian who has all the books and answers your questions"
    },
    "cache": {
        "explanation": "A temporary storage area for frequently used data",
        "analogy": "Like keeping your most-used tools on your workbench instead of going back to the toolbox every time"
    },
    "latency": {
        "explanation": "The delay before data begins transferring",
        "analogy": "Like the time it takes for water to come out of a faucet after you turn it on"
    },
    "bandwidth": {
        "explanation": "The amount of data that can be transferred at once",
        "analogy": "Like the width of a highway - more lanes mean more cars can travel at the same time"
    },
    "authentication": {
        "explanation": "Verifying someone's identity",
        "analogy": "Like showing your ID at a security checkpoint"
    },
    "authorization": {
        "explanation": "Checking if someone has permission to do something",
        "analogy": "Like a VIP pass that allows access to special areas"
    },
    "deployment": {
        "explanation": "Making a software application available for use",
        "analogy": "Like opening a restaurant - all the preparation is done, now it's ready for customers"
    },
    "docker": {
        "explanation": "A tool that packages applications with all their dependencies",
        "analogy": "Like a shipping container that holds everything needed for the product inside"
    },
    "git": {
        "explanation": "A system for tracking changes in code and collaborating",
        "analogy": "Like an infinite undo button for code that lets multiple people work together"
    },
    "javascript": {
        "explanation": "A programming language that makes websites interactive",
        "analogy": "Like the muscles that make a robot move and respond"
    },
    "react": {
        "explanation": "A library for building user interfaces",
        "analogy": "Like a set of building blocks that snap together to create web pages"
    },
    "node": {
        "explanation": "A JavaScript runtime that lets you run JavaScript on servers",
        "analogy": "Like giving JavaScript superpowers to work outside of web browsers"
    },
    "rest": {
        "explanation": "A style of API design for communication between systems",
        "analogy": "Like ordering from a menu - you make a request (order) and get a response (food)"
    },
    "json": {
        "explanation": "A format for storing and sharing data",
        "analogy": "Like a well-organized shopping list that computers can easily read"
    },
    "query": {
        "explanation": "A request for information from a database",
        "analogy": "Like asking a question to a very organized librarian"
    },
    "variable": {
        "explanation": "A container for storing data values",
        "analogy": "Like a labeled box where you keep something for later use"
    },
    "function": {
        "explanation": "A reusable block of code that performs a specific task",
        "analogy": "Like a machine that takes input, does something, and gives output"
    },
    "loop": {
        "explanation": "Code that repeats until a condition is met",
        "analogy": "Like running laps around a track until you've completed a certain number"
    },
    "recursive": {
        "explanation": "A function that calls itself",
        "analogy": "Like Russian nesting dolls - each one contains a smaller version of itself"
    },
    "async": {
        "explanation": "Operations that don't wait for each other",
        "analogy": "Like cooking multiple dishes at once - you don't wait for one to finish before starting the next"
    },
    "callback": {
        "explanation": "A function passed as an argument to be called later",
        "analogy": "Like leaving a voicemail and asking for a callback when they have time"
    },
    "promise": {
        "explanation": "Represents a value that may be available now or in the future",
        "analogy": "Like a rain check - it represents a future delivery of something"
    },
    "keyword": {
        "explanation": "Reserved words in a programming language with special meaning",
        "analogy": "Like command words that a dog knows - they trigger specific actions"
    }
}


def split_into_sentences(text):
    """Split text into sentences."""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]


def identify_concepts(text):
    """Identify key concepts and jargon in the text."""
    found_concepts = []
    text_lower = text.lower()

    for term, info in JARGON_DICT.items():
        if term in text_lower:
            found_concepts.append({
                "term": term,
                "explanation": info["explanation"],
                "analogy": info["analogy"],
                "context": ""  # Will be filled with surrounding text
            })

    return found_concepts


def simplify_text(text):
    """Simplify text by identifying and explaining jargon."""
    sentences = split_into_sentences(text)
    simplified_sentences = []
    concepts = identify_concepts(text)

    for sentence in sentences:
        simplified_sentence = sentence
        for concept in concepts:
            if concept["term"] in sentence.lower():
                # Add inline explanation
                explanation = f" ({concept['explanation']})"
                simplified_sentence += explanation
        simplified_sentences.append(simplified_sentence)

    return {
        "simplified_text": " ".join(simplified_sentences),
        "concepts": concepts
    }


def create_step_by_step(content):
    """Convert content into step-by-step format if applicable."""
    steps = []

    # Look for numbered lists or sequential language
    paragraphs = content.split("\n\n")

    step_patterns = [
        r'^(\d+)[\.\)]\s+(.+)',
        r'^(first|second|third|next|then|finally)\s*:?\s*(.+)',
        r'^(step\s+\d+)[:\-]\s*(.+)'
    ]

    for para in paragraphs:
        for pattern in step_patterns:
            match = re.search(pattern, para, re.IGNORECASE)
            if match:
                step_num = len(steps) + 1
                step_content = match.group(2) if len(match.groups()) > 1 else match.group(1)
                steps.append({
                    "step": step_num,
                    "description": step_content.strip()
                })
                break

    return steps if steps else None


def create_summary_cards(sections):
    """Create summary cards for key concepts."""
    cards = []

    for i, section in enumerate(sections):
        if section.get("content"):
            # Create a card for each major section
            card = {
                "title": section["heading"],
                "summary": section["content"][:200] + "..." if len(section["content"]) > 200 else section["content"],
                "key_points": split_into_sentences(section["content"])[:3]
            }
            cards.append(card)

    return cards


def generate_real_world_analogy(concept, context):
    """Generate a real-world analogy for a concept."""
    if concept in JARGON_DICT:
        return JARGON_DICT[concept]["analogy"]
    return f"Think of {concept} like..."


def main():
    if len(sys.argv) < 2:
        print("Usage: python simplify_content.py <content.json>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)

    # Process the content
    result = {
        "title": content_data.get("title", ""),
        "url": content_data.get("url", ""),
        "simplified_version": {},
        "key_concepts": [],
        "step_by_step": [],
        "summary_cards": []
    }

    # Simplify each section
    simplified_sections = []
    for section in content_data.get("sections", []):
        simplified = simplify_text(section.get("content", ""))
        simplified_sections.append({
            "heading": section.get("heading", ""),
            "simplified_content": simplified["simplified_text"],
            "concepts_found": simplified["concepts"]
        })

        # Collect unique concepts
        for concept in simplified["concepts"]:
            if concept["term"] not in [c["term"] for c in result["key_concepts"]]:
                result["key_concepts"].append(concept)

    result["simplified_version"]["sections"] = simplified_sections

    # Create step-by-step guide if applicable
    full_content = content_data.get("content", "")
    steps = create_step_by_step(full_content)
    if steps:
        result["step_by_step"] = steps

    # Create summary cards
    result["summary_cards"] = create_summary_cards(content_data.get("sections", []))

    # Add analogies for each concept
    for concept in result["key_concepts"]:
        concept["real_world_analogy"] = generate_real_world_analogy(
            concept["term"],
            content_data.get("content", "")
        )

    # Output as JSON
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
