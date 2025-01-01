#!/bin/bash

# Base directory for the project
BASE_DIR="main_py_project"

# Create base directory
mkdir -p "$BASE_DIR"
cd "$BASE_DIR" || exit

# Create main application directory and subdirectories
mkdir -p src/utils
mkdir -p src/config
mkdir -p src/output/logs
mkdir -p src/tests
mkdir -p docs

# Create main script and utility files
touch src/main.py

# Utility modules
touch src/utils/validation_utils.py

touch src/utils/file_reader.py

touch src/utils/logger.py

# Configuration files
touch src/config/settings.py

touch src/config/help_text.py

# Output files
touch src/output/valid_ips.txt

touch src/output/logs/app.log

# Test files
touch src/tests/test_main.py

touch src/tests/test_validation.py

touch src/tests/test_file_reader.py

touch src/tests/test_logger.py

# Documentation files
touch docs/requirements.md

touch docs/architecture.md

touch docs/usage_guide.md

# Success message
echo "Directory structure for 'main_py_project' created successfully."
