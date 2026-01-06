# Changelog

All notable changes to this project will be documented in this file.

Please choose versions by [Semantic Versioning](http://semver.org/).

* MAJOR version when you make incompatible API changes,
* MINOR version when you add functionality in a backwards-compatible manner, and
* PATCH version when you make backwards-compatible bug fixes.

## v0.1.2

- Fix CI to install dev dependencies with uv sync --all-extras

## v0.1.1

- Add standalone pytest.ini with short tracebacks and deprecation filtering
- Improve Makefile.precommit with check target and error tolerance
- Move pytest config from pyproject.toml to pytest.ini

## v0.1.0

- Add Kubernetes manifests (deployment, statefulset, service, ingress)
- Add k8s deployment tooling with Makefile.k8s
- Fix Docker image name from bborbe/skeleton to bborbe/python-skeleton
- Improve consumer error handling with logging
- Update environment config with export statements

## v0.0.1

- Initial release
- FastAPI HTTP server with health and metrics endpoints
- Kafka producer/consumer with Protocol-based DI
- Pydantic v2 BaseSettings for configuration
- uv package management
- ruff formatting and linting
- mypy type checking
- pytest testing
- Docker multi-stage build
- GitHub Actions CI
