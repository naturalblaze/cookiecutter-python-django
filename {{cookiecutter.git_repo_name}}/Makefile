# Makefile for project needs
# Author: Ben Trachtenberg/Blaze Bryant
# Version: 3.0.0
#
PROJECT = <project-name>
# APP = <app-name>

.PHONY: all info build build-container coverage format pylint pytest gh-pages build dev-run start-container \
	stop-container remove-container check-vuln check-security pip-export

info:
	@echo "make options"
	@echo "    all                 To run coverage, format, pylint, and check-vuln"
	@echo "    build               To build a distribution"
	@echo "    build-container     To build a container image"
	@echo "    check-vuln          To check for vulnerabilities in the dependencies"
	@echo "    check-security      To check for vulnerabilities in the code"
	@echo "    coverage            To run coverage and display ASCII and output to htmlcov"
	@echo "    dev-run             To run the app"
	@echo "    format              To format the code with black"
	@echo "    pylint              To run pylint"
	@echo "    pytest              To run pytest with verbose option"
	@echo "    ruff-format         To run ruff formatter"
	@echo "    ruff-lint           To run ruff linter"
	@echo "    start-container     To start the container"
	@echo "    stop-container      To stop the container"
	@echo "    remove-container    To remove the container"
{% if cookiecutter.package_manager == 'uv' %}	@echo "    pip-export          To export the requirements to requirements.txt and requirements-dev.txt"{% endif %}
{% if cookiecutter.app_documents_location == 'github-pages' %}	@echo "    gh-pages           To create the GitHub pages"{% endif %}

{% if cookiecutter.package_manager == 'pip' %}

all: format pylint coverage check-security check-vuln

build:
	@python -m build

coverage:
	@pytest --cov --cov-report=html -vvv

format:
	@black $(PROJECT)/
# 	@black $(APP)/
	@black tests/
	@black scripts/

pylint:
	@pylint $(PROJECT)/
# 	@pylint $(APP)/

pytest:
	@pytest --cov -vvv

dev-run:
	@python manage.py runserver

check-vuln:
	@pip-audit -r requirements.txt

check-security:
	@bandit -c pyproject.toml -r .

{% if cookiecutter.app_documents_location == 'github-pages' %}
gh-pages:
	@rm -rf ./docs/source/code
	@sphinx-apidoc -o ./docs/source/code ./$(PROJECT)
	@sphinx-build ./docs ./docs/gh-pages
{% endif %}

{% elif cookiecutter.package_manager == 'uv' %}

all: format pylint coverage check-security pip-export

build:
	@uv build --wheel --sdist

coverage:
	@uv run pytest --cov --cov-report=html -vvv

format:
	@uv run black $(PROJECT)/
# 	@uv run black $(APP)/
	@uv run black tests/
	@uv run ruff format scripts/

pylint:
	@uv run pylint $(PROJECT)/
# 	@uv run pylint $(APP)/

pytest:
	@uv run pytest --cov -vvv

ruff-format:
	@uv run ruff format $(PROJECT)/
# 	@uv run ruff format $(APP)/
	@uv run ruff format tests/
	@uv run ruff format scripts/

ruff-lint:
	@uv run ruff check $(PROJECT)/
# 	@uv run ruff format $(APP)/

dev-run:
	@uv run python manage.py runserver

check-security:
	@uv run bandit -c pyproject.toml -r .

pip-export:
	@uv export --no-dev --no-emit-project --no-editable > requirements.txt
	@uv export --no-emit-project --no-editable > requirements-dev.txt

{% if cookiecutter.app_documents_location == 'github-pages' %}
gh-pages:
	@rm -rf ./docs/source/code
	@uv run sphinx-apidoc -o ./docs/source/code ./$(PROJECT)
# 	@uv run sphinx-apidoc -o ./docs/source/code ./$(APP)
	@uv run sphinx-build ./docs ./docs/gh-pages
{% endif %}

{% endif %}

{% if cookiecutter.container_runtime == "podman" %}
build-container:
	@cd containers && podman build --ssh=default --build-arg=build_branch=main -t {{ cookiecutter.git_repo_name }}:latest -f Containerfile

start-container:
	@podman run -itd --name {{ cookiecutter.git_repo_name }} -p 8080:8080 localhost/{{ cookiecutter.git_repo_name }}:latest

stop-container:
	@podman stop {{ cookiecutter.git_repo_name }}

remove-container:
	@podman rm {{ cookiecutter.git_repo_name }}
{% endif %}

{% if cookiecutter.container_runtime == "docker" %}
build-container:
	@cd containers && docker build --ssh=default --build-arg=build_branch=main -t {{ cookiecutter.git_repo_name }}:latest -f Dockerfile

start-container:
	@docker run -itd --name {{ cookiecutter.git_repo_name }} -p 8080:8080 localhost/{{ cookiecutter.git_repo_name }}:latest

stop-container:
	@docker stop {{ cookiecutter.git_repo_name }}

remove-container:
	@docker rm {{ cookiecutter.git_repo_name }}
{% endif %}
