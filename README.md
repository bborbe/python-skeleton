# Python Skeleton

[![CI](https://github.com/bborbe/python-skeleton/actions/workflows/ci.yml/badge.svg)](https://github.com/bborbe/python-skeleton/actions/workflows/ci.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: BSD-2-Clause](https://img.shields.io/badge/License-BSD--2--Clause-blue.svg)](LICENSE)

Production-ready Python project skeleton with FastAPI, Kafka, and modern tooling.

## Features

- **FastAPI** HTTP server with health and metrics endpoints
- **Kafka** producer/consumer with Protocol-based DI
- **Pydantic v2** configuration management
- **uv** package management
- **ruff** for formatting and linting
- **mypy** for type checking
- **pytest** for testing
- **Docker** multi-stage builds
- **GitHub Actions** CI

## Quick Start

```bash
# Install dependencies
make install

# Run the server
make run

# Run all checks
make precommit
```

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `/healthz` | Liveness probe (Kubernetes) |
| `/readiness` | Readiness probe (Kubernetes) |
| `/metrics` | Prometheus metrics |

## Configuration

Environment variables (or `.env` file):

| Variable | Default | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` | Server host |
| `PORT` | `8080` | Server port |
| `LOG_LEVEL` | `INFO` | Logging level |
| `KAFKA_BROKERS` | `localhost:9092` | Kafka brokers |
| `SENTRY_DSN` | `` | Sentry DSN (optional) |

## Development

```bash
# Format code
make format

# Lint code
make lint

# Type check
make typecheck

# Run tests
make test

# Dependency vulnerabilities
make audit

# Vulnerability + secret scan
make trivy
```

## Security gates

`make check` runs `audit` (pip-audit) and `trivy fs` (vulnerabilities **and** secrets) alongside `lint` and `typecheck`, mirroring go-skeleton and node-skeleton.

`pip-audit` scans the fully-resolved, hashed dependency set exported from `uv.lock`, so it covers the exact transitive tree that gets installed. Unlike node-skeleton's `npm audit --audit-level=high`, there is **no severity threshold**: PyPI advisories carry no reliable severity field, so there is nothing to threshold on. The gate fails on any known vulnerability — stricter than the Node gate, not weaker.

`audit` and `trivy` both depend on `sync` because `uv.lock` is gitignored. Without that dependency a fresh clone would scan no Python manifest at all and report zero vulnerabilities — a silent pass, which is worse than no gate.

Static security analysis (the `gosec` analogue) is ruff's `S` ruleset — flake8-bandit, which is a port of bandit — rather than a separate `bandit` tool. Same rules, no second tool or config, and it runs in the existing `lint` pass. Two rules are suppressed with reasons in `pyproject.toml`: `S104` globally (binding `0.0.0.0` is correct for a containerised service) and `S101` for `tests/**` (`assert` is pytest's assertion mechanism).

`osv-scanner` is **not** included, unlike go-skeleton — it would pull a Go toolchain into a Python repo to add a third advisory database over ground pip-audit and trivy already cover.

Ignores live in `.trivyignore`, one ID per line with a reason. An entry without a reason is a silent risk.

| Skeleton | Security gates in `make check` |
|---|---|
| go-skeleton | `vulncheck`, `osv-scanner`, `gosec`, `trivy` (vuln + secret) |
| node-skeleton | `npm audit` (high/critical), `trivy` (vuln + secret) |
| python-skeleton | `pip-audit` (any severity), ruff `S`, `trivy` (vuln + secret) |

## Docker

```bash
# Build image
docker build -t skeleton .

# Run container
docker run -p 8080:8080 skeleton
```

## Project Structure

```
src/skeleton/
├── __init__.py         # Version
├── __main__.py         # CLI entry point
├── config.py           # Pydantic BaseSettings
├── logging_setup.py    # Logging configuration
├── factory.py          # DI factory functions
├── server.py           # FastAPI server
├── handlers/           # HTTP handlers
│   ├── health.py       # Health probes
│   └── metrics.py      # Prometheus metrics
└── kafka/              # Kafka modules
    ├── producer.py     # Message producer
    └── consumer.py     # Message consumer

tests/
├── conftest.py         # Shared pytest fixtures
├── test_config.py      # Configuration tests
├── test_factory.py     # Factory function tests
├── handlers/           # Handler tests
│   ├── conftest.py     # Handler fixtures
│   ├── test_health.py  # Health check tests
│   └── test_metrics.py # Metrics endpoint tests
└── kafka/              # Kafka tests
    ├── conftest.py     # Kafka fixtures
    ├── test_producer.py # Producer protocol tests
    └── test_consumer.py # Consumer protocol tests
```

## License

BSD-2-Clause
