POETRY_VERSION = 1.1.13

# Env stuff
.PHONY: get-poetry
get-poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - --version $(POETRY_VERSION)

.PHONY: build-env
build-env:
	poetry install

# Tests
.PHONY: tests
tests:
	poetry run ./manage.py test

# Passive linters
.PHONY: black
black:
	poetry run black .

.PHONY: flake8
flake8:
	poetry run flake8 --max-line-length=88 --ignore=E203,W503 .

.PHONY: isort
isort:
	poetry run isort .

# Aggresive linters
.PHONY: black!
black!:
	poetry run black .

.PHONY: isort!
isort!:
	poetry run isort .

# Receive args (use like `$(filter-out $@,$(MAKECMDGOALS))`)
%:
	@: