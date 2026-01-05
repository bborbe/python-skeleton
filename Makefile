include Makefile.variables
include Makefile.precommit
include Makefile.docker
include example.env

SERVICE = bborbe/skeleton

.PHONY: all run install clean-local

all: precommit

# Install dependencies
install:
	uv sync --all-extras

# Run the application
run:
	uv run skeleton serve

# Clean build artifacts (local)
clean-local:
	rm -rf .venv dist *.egg-info .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
