# Changelog

All notable changes to this project will be documented in this file.

Please choose versions by [Semantic Versioning](http://semver.org/).

* MAJOR version when you make incompatible API changes,
* MINOR version when you add functionality in a backwards-compatible manner, and
* PATCH version when you make backwards-compatible bug fixes.

## v0.2.0

- Restructure tests to mirror source hierarchy (handlers/, kafka/ subdirs)
- Add py.typed marker for PEP 561 compliance
- Add comprehensive test coverage for all 9 modules (30 tests total)
- Add tests for CLI entry point, logging setup, and server wrapper
- Add scoped conftest.py files with domain-specific fixtures
- Update README with complete test structure documentation

## v0.1.3

- Add sync target to Makefile for dependency management
- Add sync to precommit workflow for automatic dependency updates
- Improve Makefile structure with .PHONY declarations next to each target
- Make install an alias for sync target

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
