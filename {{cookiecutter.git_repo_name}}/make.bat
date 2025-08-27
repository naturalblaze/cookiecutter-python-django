@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 2.0.0
REM

SET option=%1
SET PROJECT=<project-name>

IF "%option%" == "" (
    GOTO BAD_OPTIONS
)

{% if cookiecutter.package_manager == 'pip' %}

IF "%option%" == "all" (
    black %PROJECT%/
    black tests/
    pylint %PROJECT%\
    pytest --cov --cov-report=html -vvv
    bandit -c pyproject.toml -r .
    pip-audit -r requirements.txt
    GOTO END
)

IF "%option%" == "build" (
    python -m build
    GOTO END
)

IF "%option%" == "coverage" (
    pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%option%" == "pylint" (
    pylint %PROJECT%\
    GOTO END
)

IF "%option%" == "pytest" (
    pytest --cov -vvv
    GOTO END
)

IF "%option%" == "dev-run" (
    python -c "from %PROJECT% import cli;cli()" start -p 8080 -r
    GOTO END
)

IF "%option%" == "format" (
    black %PROJECT%/
    black tests/
    GOTO END
)

IF "%option%" == "check-vuln" (
    pip-audit -r requirements.txt
    GOTO END
)

IF "%option%" == "check-security" (
    bandit -c pyproject.toml -r .
    GOTO END
)

{% if cookiecutter.app_documents_location == 'github-pages' %}
IF "%option%" == "gh-pages" (
    rmdir /s /q docs\source\code
    sphinx-apidoc -o ./docs/source/code ./%PROJECT%
    sphinx-build ./docs ./docs/gh-pages
    GOTO END
)
{% endif %}

{% elif cookiecutter.package_manager == 'uv' %}

IF "%option%" == "all" (
    uv run black %PROJECT%/
    uv run black tests/
    uv run pylint %PROJECT%\
    uv run pytest --cov --cov-report=html -vvv
    uv run bandit -c pyproject.toml -r .
    uv export --no-dev --no-emit-project --no-editable > requirements.txt
    uv export --no-emit-project --no-editable > requirements-dev.txt
    GOTO END
)

IF "%option%" == "build" (
    uv build --wheel --sdist
    GOTO END
)

IF "%option%" == "coverage" (
    uv run pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%option%" == "pylint" (
    uv run pylint %PROJECT%\
    GOTO END
)

IF "%option%" == "pytest" (
    uv run pytest --cov -vvv
    GOTO END
)

IF "%option%" == "dev-run" (
    uv run python manage.py runserver
    GOTO END
)

IF "%option%" == "format" (
    uv run black %PROJECT%/
    uv run black tests/
    GOTO END
)

IF "%option%" == "check-security" (
    uv run bandit -c pyproject.toml -r .
    GOTO END
)

IF "%option%" == "pip-export" (
    uv export --no-dev --no-emit-project --no-editable > requirements.txt
    uv export --no-emit-project --no-editable > requirements-dev.txt
    GOTO END
)

{% if cookiecutter.app_documents_location == 'github-pages' %}
IF "%option%" == "gh-pages" (
    rmdir /s /q docs\source\code
    uv run sphinx-apidoc -o ./docs/source/code ./%PROJECT%
    uv run sphinx-build ./docs ./docs/gh-pages
    GOTO END
)
{% endif %}

{% endif %}

:OPTIONS
@ECHO make options
@ECHO     all             To run coverage, format, pylint, and check-vuln
@ECHO     build           To build a distribution
@ECHO     coverage        To run coverage and display ASCII and output to htmlcov
@ECHO     dev-run         To run the app
@ECHO     check-vuln      To check for vulnerabilities in the dependencies
@ECHO     check-security  To check for vulnerabilities in the code
@ECHO     format          To format the code with black
@ECHO     pylint          To run pylint
@ECHO     pytest          To run pytest with verbose option
{% if cookiecutter.package_manager == 'uv' %}@ECHO     pip-export      To export the requirements.txt and requirements-dev.txt{% endif %}
{% if cookiecutter.app_documents_location == 'github-pages' %}@ECHO     gh-pages  To create the GitHub pages{% endif %}
GOTO END

:BAD_OPTIONS
@ECHO Argument is missing
@ECHO Usage: make.bat option
@ECHO.
GOTO OPTIONS

:END
