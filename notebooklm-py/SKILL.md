---
name: notebooklm-py
description: Unofficial Google NotebookLM Python API - automate research, generate podcasts, and integrate NotebookLM into AI agents
license: MIT
compatibility: opencode
metadata:
  audience: developers
  use-case: research-automation
---

# NotebookLM Python API

Unofficial Google NotebookLM library for Python and CLI. Automate research workflows, generate podcasts from documents, and integrate NotebookLM into AI agents.

## What You Can Do

- **AI Agent Tools** - Integrate NotebookLM into Claude Code or other LLM agents with natural language automation
- **Research Automation** - Bulk-import sources (URLs, PDFs, YouTube, Google Drive), run web research queries programmatically
- **Content Generation** - Generate Audio Overviews (podcasts), videos, quizzes, flashcards, and study guides

## Usage

### CLI Commands

```bash
# Authenticate (opens browser)
notebooklm login

# Create and use notebooks
notebooklm create "My Research"
notebooklm use <notebook_id>

# Add sources
notebooklm source add "https://en.wikipedia.org/wiki/Artificial_intelligence"
notebooklm source add "./paper.pdf"

# Chat
notebooklm ask "What are the key themes?"

# Generate podcast
notebooklm generate audio --wait
notebooklm download audio ./podcast.mp3
```

### Python API

```python
import asyncio
from notebooklm import NotebookLMClient

async def main():
    async with await NotebookLMClient.from_storage() as client:
        # List notebooks
        notebooks = await client.notebooks.list()

        # Create notebook and add source
        nb = await client.notebooks.create("Research")
        await client.sources.add_url(nb.id, "https://example.com")

        # Chat
        result = await client.chat.ask(nb.id, "Summarize this")
        print(result.answer)

        # Generate podcast
        status = await client.artifacts.generate_audio(nb.id)
        await client.artifacts.wait_for_completion(nb.id, status.task_id)

asyncio.run(main())
```

## Features

| Category | Capabilities |
|----------|-------------|
| Notebooks | Create, list, rename, delete, share |
| Sources | URLs, YouTube, files (PDF/TXT/MD/DOCX), Google Drive, pasted text |
| Chat | Questions, conversation history, custom personas |
| Generation | Audio podcasts, video, slides, quizzes, flashcards, reports, infographics, mind maps |
| Research | Web and Drive research agents with auto-import |
| Downloads | Audio, video, slides, infographics, reports, mind maps, data tables, quizzes, flashcards |

## Installation

```bash
# Basic installation
pip install notebooklm-py

# With browser login support
pip install "notebooklm-py[browser]"
playwright install chromium
```

## Important Notes

- **Unofficial Library** - Uses undocumented Google APIs that can change without notice
- Not affiliated with Google - Community project
- APIs may break - Google can change internal endpoints anytime
- Rate limits apply - Heavy usage may be throttled
- Best for prototypes, research, and personal projects

## When to Use

Use this skill when you need to:
- Automate research workflows involving document analysis
- Generate audio podcasts from written content programmatically
- Integrate NotebookLM capabilities into AI agent workflows
- Bulk-process sources and generate summaries/quiz/flashcards

## References

- Source: https://github.com/teng-lin/notebooklm-py
- CLI Reference: https://github.com/teng-lin/notebooklm-py/blob/main/docs/cli-reference.md
- Python API: https://github.com/teng-lin/notebooklm-py/blob/main/docs/python-api.md
