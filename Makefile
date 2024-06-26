# Makefile for RPAL interpreter 

# Makefile for RPAL interpreter 

# Usage:
# - `make`: Installs dependencies, runs the RPAL interpreter, runs tests, and cleans up.
# - `make install`: Installs project dependencies.
# - `make run`: Executes the RPAL interpreter.
# - `make test`: Executes all test cases.
# - `make test F=...`: Executes a specific test case.(in rpal_tests/rpal_sources)
# - `make test_ast`: Executes all test cases related to Abstract Syntax Tree (AST).
# - `make test_ast F=...`: Executes a specific test case related to AST. (in rpal_tests/rpal_sources)
# - `make test_st : Executes all test cases related to Standardized Syntax Tree (ST).
# - `make test_st F=...`: Executes a specific test case related to ST. (in rpal_tests/rpal_sources)
# - `make clean`: Cleans up generated files.
# - `make all`: Installs dependencies, runs the RPAL interpreter, runs tests, and cleans up.
# - `make converge`: run all pytest, runs the RPAL interpreter
# - `make converg_report`: get converg report in html format

############################################################################################################
# define variables for the RPAL interpreter
############################################################################################################

ifeq ($(GITHUB_ACTIONS),true)
  ifeq ($(OS),Windows_NT)
	SHELL := cmd.exe
  else
	SHELL := /bin/sh
  endif
endif

###########################################################################################################
# OS detection
###########################################################################################################
# Variables
ifeq ($(OS),Windows_NT)
	PYTHON := python
	PIP := pip
	PY_VERSION := $(shell $(PYTHON) --version 2>&1)
else
	PYTHON := python3
	PIP := pip
	PY_VERSION := $(shell $(PYTHON) --version 2>&1)
endif

PYTEST = pytest

# Default target
.DEFAULT_GOAL := all

# Targets
.PHONY: install run tests test test_ast test_st test_all clean all check_python check_pip

# Default target
all: install clean test_all clean
############################################################################################################
# define install target for the RPAL interpreter
############################################################################################################
# Install dependencies
install: check_python check_pip requirements.txt
	@echo "Installing dependencies..."
	$(PYTHON) -m $(PIP) install -r requirements.txt
############################################################################################################
# end of install target for the RPAL interpreter
############################################################################################################

############################################################################################################
# check targets for the RPAL interpreter to check if Python and pip are installed correctly and their versions 
############################################################################################################
# Check if Python is installed
R = 1
check_python:
	@echo "Checking Python installation..."
	@if [ -z "$(PYTHON)" ]; then \
		echo "$(PYTHON) is not installed. Please install $(PYTHON)."; \
		exit 1; \
	else \
		echo "Python is installed at $(PYTHON)"; \
		echo "Python version: $(PY_VERSION)"; \
	fi

# Check if pip is installed
check_pip:
	@echo "Checking pip installation..."
	@if [ -z "$(PIP)" ]; then \
		echo "$(PIP) is not installed. Please install $(PIP)."; \
		exit 1; \
	else \
		echo "$(PIP) is installed at $(shell command -v $(PIP))"; \
	fi

############################################################################################################
# end of check targets for the RPAL interpreter
############################################################################################################
############################################################################################################
# define run target for the RPAL interpreter
############################################################################################################

# Run the RPAL interpreter
run: install myrpal.py test.txt
	@echo "Running RPAL interpreter..."
	$(PYTHON) myrpal.py test.txt
############################################################################################################
# end of run target for the RPAL interpreter
############################################################################################################
############################################################################################################
# define test targets for the RPAL interpreter
############################################################################################################

# Run normal tests
test: 
	@echo "Running tests...$(OS)"
	@if [ "$(OS)" = "Windows_NT" ] && [ "$(R)" = " " ]; then \
		if [ "$(F)" = "" ]; then \
			$(PYTHON) -m pytest -v --no-summary rpal_tests/test_generate_tests_with_rpal_exe.py ; \
		else \
			$(PYTHON) -m pytest -v  -k "$(F)" rpal_tests/test_generate_tests_with_rpal_exe.py -vvv --tb=short; \
		fi \
	else \
		if [ "$(F)" = "" ]; then \
			$(PYTHON) -m pytest -v --no-summary rpal_tests/test_generate_tests.py ; \
		else \
			$(PYTHON) -m pytest -v  -k "$(F)" rpal_tests/test_generate_tests.py -vvv --tb=short; \
		fi \
	fi

# Run a specific test with parameters
test_st:
	@echo "Running tests...$(OS)"
	@if [ "$(OS)" = "Windows_NT" ] && [ "$(R)" = " " ]; then \
		if [ "$(F)" = "" ]; then \
			$(PYTHON) -m pytest -v --no-summary rpal_tests/test_generate_st_tests_with_rpal_exe.py ; \
		else \
			$(PYTHON) -m pytest -v  -k "$(F)" rpal_tests/test_generate__st_tests_with_rpal_exe.py -vvv --tb=short; \
		fi \
	else \
		if [ "$(F)" = "" ]; then \
			$(PYTHON) -m pytest -v --no-summary rpal_tests/test_generate_st_tests.py ; \
		else \
			$(PYTHON) -m pytest -v  -k "$(F)" rpal_tests/test_generate_st_tests.py -vvv --tb=short; \
		fi \
	fi

# Run a specific test with parameters
test_ast:
	@echo "Running tests...$(OS)"
	@if [ "$(OS)" = "Windows_NT" ] && [ "$(R)" = " " ]; then \
		if [ "$(F)" = "" ]; then \
			$(PYTHON) -m pytest -v --no-summary rpal_tests/test_generate_ast_tests_with_rpal_exe.py ; \
		else \
			$(PYTHON) -m pytest -v  -k "$(F)" rpal_tests/test_generate__ast_tests_with_rpal_exe.py -vvv --tb=short; \
		fi \
	else \
		if [ "$(F)" = "" ]; then \
			$(PYTHON) -m pytest -v --no-summary rpal_tests/test_generate_ast_tests.py ; \
		else \
			$(PYTHON) -m pytest -v  -k "$(F)" rpal_tests/test_generate_ast_tests.py -vvv --tb=short; \
		fi \
	fi

test_all:
	@echo "Running tests...$(OS)"
	@if [ "$(OS)" = "Windows_NT" ] && [ "$(R)" = " " ]; then \
		echo "=========================================================================================================="; \
		echo "Running tests for Abstract Syntax Tree (AST):"; \
		$(PYTHON) -m pytest -q --no-summary rpal_tests/test_generate_ast_tests_with_rpal_exe.py ; \
		echo "=========================================================================================================="; \
		echo "Running tests for Standardized Syntax Tree (ST):"; \
		$(PYTHON) -m pytest -q --no-summary rpal_tests/test_generate_st_tests_with_rpal_exe.py ; \
		echo "=========================================================================================================="; \
		echo "Running tests :"; \
		$(PYTHON) -m pytest -q --no-summary rpal_tests/test_generate_tests_with_rpal_exe.py ; \
	else \
		echo "=========================================================================================================="; \
		echo "Running tests for Abstract Syntax Tree (AST):"; \
		$(PYTHON) -m pytest -q --no-summary rpal_tests/test_generate_ast_tests.py ; \
		echo "=========================================================================================================="; \
		echo "Running tests for Standardized Syntax Tree (ST):"; \
		$(PYTHON) -m pytest -q --no-summary  rpal_tests/test_generate_st_tests.py ; \
		echo "=========================================================================================================="; \
		echo "Running tests:"; \
		$(PYTHON) -m pytest -q --no-summary  rpal_tests/test_generate_tests.py ; \
	fi

############################################################################################################
# end of test targets for the RPAL interpreter
############################################################################################################

############################################################################################################
# cleanup targets for the RPAL interpreter  and check for requirements file existence
############################################################################################################

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
############################################################################################################
# end of makefile for the RPAL interpreter
############################################################################################################

############################################################################################################
# coverage check for the RPAL interpreter
############################################################################################################

coverage:
	@echo "Running tests..."
	$(PYTHON) -m coverage run -m pytest 
	@echo "Generating HTML coverage report..."
	$(PYTHON) -m coverage html

coverage_report: 
	@echo "Generating HTML coverage report..."
	$(PYTHON) -m coverage html
	@echo "Opening HTML coverage report..."
	@if [ "$(OS)" = "Windows_NT" ] ; then \
		cmd /c start htmlcov/index.html ; \
		@echo "Generating coverage report...";\
		$(PYTHON) -m coverage html;\
	else \
		xdg-open htmlcov/index.html; \
	fi

############################################################################################################

############################################################################################################

############################################################################################################









