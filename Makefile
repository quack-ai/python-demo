# this target runs checks on all files
quality:
	isort . -c
	flake8
	mypy
	pydocstyle
	black --check .
	bandit -r . -c pyproject.toml
	autoflake -c .

# this target runs checks on all files and potentially modifies some of them
style:
	isort .
	black .
	autoflake -v --in-place .

# Run tests for the library
test:
	coverage run -m pytest tests/
