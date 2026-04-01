---
description: "Search GitHub repositories and return structured results"
argument-hint: "<query> [--count N] [--sort stars|forks|updated|pushed] [--language LANG]"
allowed-tools:
  - Bash
---

Run the GitHub search script with the user's arguments and present the results.

Execute this:

```
python ~/.claude/skills/github-search/scripts/search.py $ARGUMENTS
```

Present the output directly to the user. If the script reports an error, explain it and suggest fixes.
