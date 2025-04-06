sources = {{ cookiecutter.pkg_name }}

.PHONY: test format lint unittest coverage pre-commit clean
test: format lint unittest

format:
	isort $(sources)
	black $(sources)

lint:
	flake8 $(sources)
	mypy $(sources)

clean:
	rm -rf .mypy_cache .pytest_cache
	rm -rf *.egg-info
	rm -rf .tox dist site
	rm -rf coverage.xml .coverage

deploy:
	poetry run kodexa deploy model.yml --update

undeploy:
	poetry run kodexa undeploy model.yml

generate-data-classes:
	poetry run kodexa get taxonom {{ cookiecutter.taxonomy_ref }} --output-file taxonomy.json
	poetry run kodexa dataclasses taxonomy.json --output-path {{ cookiecutter.pkg_name }} --output-file data_classes.py
