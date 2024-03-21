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

# Run all tests
tests: install rpal_tests/
	@echo "Running tests..."
	@echo "!..not yet implemented...!"
	$(PYTHON) -m pytest -v rpal_tests/

# Run normal tests
test: 
	@echo "Running tests..."
	@if [ "$(F)" = "" ]; then \
		$(PYTHON) -m pytest -v --no-summary rpal_tests/test_generate_tests.py ; \
	else \
		$(PYTHON) -m pytest -v  -k "$(F)" rpal_tests/test_generate_tests.py -vvv --tb=short; \
	fi

# Run a specific test with parameters
test_ast:
	@echo "Running tests..."
	@if [ "$(F)" = "" ]; then \
		$(PYTHON) -m pytest -v --no-summary rpal_tests/test_generate_ast_tests.py ; \
	else \
		$(PYTHON) -m pytest -v  -k "$(F)" rpal_tests/test_generate_ast_tests.py -vvv --tb=short; \
	fi


# Clean up generated files
clean:
	@echo "Cleaning up..."
	-$(PYTHON) -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]') if p.exists()]"
	-$(PYTHON) -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__') if p.exists()]"
	-$(PYTHON) -Bc "import shutil; shutil.rmtree('.pytest_cache', ignore_errors=True)"

# Ensure that the requirements file is present
requirements.txt:
	@echo "Error: requirements.txt file not found."
	@exit 1
