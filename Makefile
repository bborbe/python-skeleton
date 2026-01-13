include Makefile.variables
include Makefile.precommit
include Makefile.docker
include example.env

SERVICE = bborbe/python-skeleton

.PHONY: all
all: precommit

.PHONY: install
# Install dependencies (alias for sync)
install: sync

.PHONY: sync
# Sync dependencies
sync:
	@uv sync --all-extras

.PHONY: run
# Run the application
run:
	uv run skeleton serve

.PHONY: clean-local
# Clean build artifacts (local)
clean-local:
	rm -rf .venv dist *.egg-info .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
