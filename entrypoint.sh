#!/bin/bash
set -e

# Print build metadata
echo "=== Build Metadata ==="
echo "Version: ${BUILD_GIT_VERSION:-unknown}"
echo "Commit:  ${BUILD_GIT_COMMIT:-unknown}"
echo "Date:    ${BUILD_DATE:-unknown}"
echo "======================"

# Execute the main command
exec "$@"
