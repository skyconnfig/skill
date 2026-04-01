# Changelog

All notable changes to the GitHub Search Skill project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-04-01

### Added

- Initial release of GitHub Search Skill
- Search GitHub repositories via GitHub Search API
- Multiple sorting options: stars, forks, updated, pushed
- Filter by: language, topic, license, organization, user
- Multiple output formats: pretty, JSON, CSV, Markdown
- Rate limit handling with automatic wait
- Configurable caching (memory-based)
- Comprehensive error handling and retry logic
- UTF-8 support for Windows
- Detailed documentation (README.md, SKILL.md)
- Setup script for easy installation
- Test suite for validation

### Features

- Free to use (no API key required, but token strongly recommended)
- Structured output with repository metadata
- Language distribution detection (via separate API call)
- Formatted numbers (K/M suffixes)
- Relative and absolute datetime formatting
- Configurable via config.yaml and .env files
- Support for pagination (up to 500 results)
- Automatic rate limit monitoring

### Documentation

- Complete README with usage examples
- SKILL.md with detailed technical specifications
- FAQ section addressing common questions
- Configuration examples
- Troubleshooting guide

### Development

- Test suite with unit and integration tests
- CI-ready structure
- Extensible architecture for future enhancements

---

## [Planned] - Future Releases

### v1.1.0 (Planned)

- [ ] Code search functionality
- [ ] Issue search functionality
- [ ] User search functionality
- [ ] GraphQL API support
- [ ] Redis cache backend
- [ ] File-based cache persistence
- [ ] Language detection for queries
- [ ] Trending topics feature
- [ ] Batch search from file

### v1.2.0 (Planned)

- [ ] Advanced analytics (growth trends, license distribution)
- [ ] Export to Excel (XLSX) format
- [ ] HTML report generation
- [ ] Web dashboard interface
- [ ] Repository comparison tool
- [ ] Star history tracking
- [ ] Email/Slack notifications

### v2.0.0 (Future)

- [ ] Multi-tenant support
- [ ] Distributed caching
- [ ] Rate limit distribution across instances
- [ ] Plugin architecture
- [ ] REST API wrapper
- [ ] GraphQL endpoint

---

## Migration Guide

### From v1.0.0 to v1.1.0

When v1.1.0 is released:

1. Update dependencies: `pip install -r requirements.txt --upgrade`
2. Review new configuration options in `config.yaml.example`
3. Test with `--dry-run` flag (will be added)
4. Update any scripts using the skill

No breaking changes expected in v1.x series.
