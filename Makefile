# Variables
PYTHON = python
PYTEST = pytest

# Default target
.DEFAULT_GOAL := all

# Targets
.PHONY: install run test clean all

# Default target
all: clean install run test clean

# Install dependencies
install: requirements.txt
	@echo "Installing dependencies..."
	$(PYTHON) -m pip install -r requirements.txt

# Run the RPAL interpreter
run: install main.py test.txt
	@echo "Running RPAL interpreter..."
	$(PYTHON) main.py test.txt

# Run tests
test: install rpal_tests/
	@echo "Running tests..."
	@echo "!..not yet implemented...!"
	$(PYTEST) rpal_tests/

# Clean up generated files
clean:
	@echo "Cleaning up..."
	-$(PYTHON) -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]') if p.exists()]"
	-$(PYTHON) -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__') if p.exists()]"

# Ensure that the requirements file is present
requirements.txt:
	@echo "Error: requirements.txt file not found."
	@exit 1
