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
```

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
```

## License

BSD-2-Clause
