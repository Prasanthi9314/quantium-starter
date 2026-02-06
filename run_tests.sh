#!/bin/bash

# Activate virtual environment
source .venv/Scripts/activate

# Run pytest
pytest

# Store exit code
exit_code=$?

# If tests passed, exit 0, else exit 1
if [ $exit_code -eq 0 ]; then
  echo "All tests passed!"
  exit 0
else
  echo "Tests failed!"
  exit 1
fi
