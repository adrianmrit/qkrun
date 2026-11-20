# qkrun - A CLI Tool for Quick Tasks

[![License](https://img.shields.io/github/license/adrianmrit/qkrun)](https://github.com/adrianmrit/qkrun/blob/main/LICENSE)

qkrun is a powerful and flexible command-line tool designed to simplify task automation. It supports both per-project and global task configurations, making it ideal for developers and teams.

Documentation is available at [qkrun.readthedocs.io](https://qkrun.readthedocs.io/en/latest/).

Upgrading from `quickie-runner`? See the [migration notes](CHANGELOG.md#2.0.0).

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Setup

```bash
uv sync --dev
pre-commit install
```

### Running tests

```bash
uv run pytest
```

Run the tests with coverage and enforce the project's coverage threshold:

```bash
uv run pytest --cov --cov-report=term-missing --cov-fail-under=95
```

### Linting and formatting

```bash
uv run ruff check .
uv run ruff format .
```

### Pre-commit

Hooks are configured in `.pre-commit-config.yaml` and run automatically on commit. To run them manually:

```bash
uv run pre-commit run --all-files
```

### Continuous integration

CI runs on GitHub Actions for every push and pull request (see `.github/workflows/ci.yml`). It runs the test suite with coverage, linting, formatting checks, and pre-commit.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.
