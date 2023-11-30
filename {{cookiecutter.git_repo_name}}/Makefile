# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.5
#

.PHONY: info coverage pylint pytest gh-pages build dev-run

info:
	@echo "make options"
	@echo "    build     To build a distribution"
	@echo "    coverage  To run coverage and display ASCII and output to htmlcov"
	@echo "    dev-run   To run the app"
	@echo "    pylint    To run pylint"
	@echo "    pytest    To run pytest with verbose option"
{% if cookiecutter.app_documents_location == 'github-pages' %}	@echo "    gh-pages  To create the GitHub pages"{% endif %}

build:
	@python -m build

coverage:
	@pytest --cov --cov-report=html -vvv

pylint:
	@pylint {{cookiecutter.__app_name}}/

pytest:
	@pytest --cov -vvv

dev-run:
	@python -c "from {{cookiecutter.__app_name}} import cli;cli()" start -p 8080 -r

{% if cookiecutter.app_documents_location == 'github-pages' %}
gh-pages:
	@rm -rf ./docs/source/code
	@sphinx-apidoc -o ./docs/source/code ./{{cookiecutter.__app_name}}
	@sphinx-build ./docs ./docs/gh-pages
{% endif %}
