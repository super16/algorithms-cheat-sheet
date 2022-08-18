# Algorithms Cheat Sheet

Collection of algorithms implementations for `python3`.

## Prepare environment

Requires [poetry](https://python-poetry.org/).

### Install dependencies

```bash
poetry install
```

## Lint

### Run

```bash
poetry run flake8
poetry run mypy algorithms_cheat_sheet/ tests/
```

## Tests

### Run

```bash
poetry run pytest
```

### Coverage

```bash
poetry run coverage run -m pytest
poetry run coverage report -m
```
