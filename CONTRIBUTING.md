# Contributing to SAGE Studio

Thank you for your interest in contributing to SAGE Studio!

## Development Setup

SAGE Studio is part of the SAGE ecosystem. For development:

1. **Clone the repository**:
```bash
git clone https://github.com/SAGE-Research/sage-studio.git
cd sage-studio
```

2. **Install dependencies**:
```bash
python -m pip install -e ".[dev,full]"
```

3. **Install SAGE core dependencies** (if needed):
```bash
python -m pip install isage-common isagellm
```

## Architecture

SAGE Studio is built on top of SAGE's inference framework and follows the SAGE architecture:

- **Frontend**: React + TypeScript + Vite
- **Backend**: FastAPI application in `sage.studio.api.app`
- **Services**: visual flow registry, construction, persistence, and execution
- **Integration**: SAGE and SageLLM are consumed through their public package APIs

## Docs Consistency Checklist

When a PR changes startup chain, API routes, or runtime behavior, update docs in the same PR:

- [ ] `README.md` startup/port/dependency instructions are still correct
- [ ] `CONTRIBUTING.md` setup and testing commands match current implementation
- [ ] New or removed CLI options are documented

## Code Standards

- Follow SAGE's coding standards (see main SAGE repository)
- Use Ruff for linting and formatting
- Add tests for new features
- Update documentation

## Testing

```bash
# Run all tests
pytest tests/

# Run specific test suite
pytest tests/unit/
pytest tests/integration/
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Commit Convention

We follow Conventional Commits:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Test updates
- `chore:` - Maintenance tasks

## Community

- SAGE Research organization: https://github.com/SAGE-Research
- Documentation: https://intellistream.github.io/sage-docs/
- Issues: https://github.com/SAGE-Research/sage-studio/issues

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
