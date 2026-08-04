# Changelog

All notable changes to this project will be documented in this file.

Please choose versions by [Semantic Versioning](http://semver.org/).

* MAJOR version when you make incompatible API changes,
* MINOR version when you add functionality in a backwards-compatible manner, and
* PATCH version when you make backwards-compatible bug fixes.

## Unreleased

- feat: add `audit` target (pip-audit over the hashed dependency set exported from uv.lock)
- feat: add `trivy` target (vulnerability + secret scanning), matching go-skeleton and node-skeleton
- feat: wire `audit` and `trivy` into `make check`; both depend on `sync` so a missing uv.lock cannot cause a silent pass
- feat: enable ruff's `S` (flake8-bandit) ruleset as the gosec analogue, with reasoned suppressions for S104 and tests-only S101
- feat: add `.trivyignore` with the reason-required header
- ci: install trivy in CI
- docs: document the security posture of all three skeletons in README
- test: fix `test_create_app_includes_routers` to assert via TestClient; FastAPI >=0.141 no longer exposes included routes as `.path` on `app.routes`
- refactor: switch build backend from setuptools to hatchling per python-project-structure
- fix: copy README.md in the Dockerfile builder stage; hatchling requires the file declared by `readme` to be present in the build context

## v0.5.0
- Add entrypoint script to display build metadata at container startup
- Fix Dockerfile build by moving src/ copy before uv sync
- Simplify build stage by removing redundant uv pip install step

## v0.4.0

- Harmonize build system with go-skeleton
- Add branch name sanitization in Makefile.variables (tr '/' '-')
- Remove --no-cache from docker build for better layer caching
- Rename build args: BUILD_VERSION → BUILD_GIT_VERSION, BUILD_COMMIT → BUILD_GIT_COMMIT
- Add comprehensive OCI labels to Dockerfile
- Add DOCKER_REGISTRY and BRANCH build args

## v0.3.0

- Upgrade Python from 3.12 to 3.14
- Update Docker base images to python:3.14-slim
- Update ruff and mypy target versions to py314
- Fix type hint for Generator in test fixture

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
