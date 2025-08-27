"""Tests for cookiecutter-python-django project template."""

import os
import tomli


def test_bake_project_podman(cookies, bake_project_podman_pip: dict):
    """Test baking project with podman and pip

    Args:
        cookies (pytest-cookie): pytest-cookie function
        bake_project_podman_pip (dict): fixture with podman and pip options
    """
    result = cookies.bake(extra_context=bake_project_podman_pip)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "podman-project-pip"
    assert result.project_path.is_dir()
    assert result.project_path.joinpath("README.md").is_file()
    assert result.project_path.joinpath("requirements.txt").is_file()
    assert result.project_path.joinpath("requirements-dev.txt").is_file()
    assert result.project_path.joinpath("containers").is_dir()
    assert result.project_path.joinpath("containers", "Containerfile").is_file()
    assert not result.project_path.joinpath("containers", "Dockerfile").is_file()
    assert result.project_path.joinpath("tests").is_dir()
    assert result.project_path.joinpath("tests", "conftest.py").is_file()
    assert result.project_path.joinpath("tests", "data").is_dir()
    assert result.project_path.joinpath("tests", "data", "README.md").is_file()
    assert result.project_path.joinpath(".github", "workflows", "publish-to-pypi.yml").is_file()
    assert result.project_path.joinpath(".github", "workflows", "test-coverage-lint.yml").is_file()
    assert not result.project_path.joinpath(".github", "workflows", "publish-to-pypi-uv.yml").is_file()
    assert not result.project_path.joinpath(".github", "workflows", "test-coverage-lint-uv.yml").is_file()


def test_bake_project_podman_uv(cookies, bake_project_podman_uv: dict):
    """Test baking project with podman and uv

    Args:
        cookies (pytest-cookie): pytest-cookie function
        bake_project_podman_pip (dict): fixture with podman and uv options
    """
    result = cookies.bake(extra_context=bake_project_podman_uv)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "podman-project-uv"
    assert result.project_path.is_dir()
    assert result.project_path.joinpath("README.md").is_file()
    assert not result.project_path.joinpath("requirements.txt").is_file()
    assert not result.project_path.joinpath("requirements-dev.txt").is_file()
    assert result.project_path.joinpath("containers").is_dir()
    assert result.project_path.joinpath("containers", "Containerfile").is_file()
    assert not result.project_path.joinpath("containers", "Dockerfile").is_file()
    assert result.project_path.joinpath("tests").is_dir()
    assert result.project_path.joinpath("tests", "conftest.py").is_file()
    assert result.project_path.joinpath("tests", "data").is_dir()
    assert result.project_path.joinpath("tests", "data", "README.md").is_file()
    assert not result.project_path.joinpath(".github", "workflows", "publish-to-pypi.yml").is_file()
    assert not result.project_path.joinpath(".github", "workflows", "test-coverage-lint.yml").is_file()
    assert result.project_path.joinpath(".github", "workflows", "publish-to-pypi-uv.yml").is_file()
    assert result.project_path.joinpath(".github", "workflows", "test-coverage-lint-uv.yml").is_file()


def test_bake_project_docker_pip(cookies, bake_project_docker_pip: dict):
    """Test baking project with docker and pip

    Args:
        cookies (pytest-cookie): pytest-cookie function
        bake_project_docker_pip (dict): fixture with docker and pip options
    """
    result = cookies.bake(extra_context=bake_project_docker_pip)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "docker-project-pip"
    assert result.project_path.is_dir()
    assert result.project_path.joinpath("README.md").is_file()
    assert result.project_path.joinpath("requirements.txt").is_file()
    assert result.project_path.joinpath("requirements-dev.txt").is_file()
    assert result.project_path.joinpath("containers").is_dir()
    assert not result.project_path.joinpath("containers", "Containerfile").is_file()
    assert result.project_path.joinpath("containers", "Dockerfile").is_file()
    assert result.project_path.joinpath("tests").is_dir()
    assert result.project_path.joinpath("tests", "conftest.py").is_file()
    assert result.project_path.joinpath("tests", "data").is_dir()
    assert result.project_path.joinpath("tests", "data", "README.md").is_file()
    assert result.project_path.joinpath(".github", "workflows", "publish-to-pypi.yml").is_file()
    assert result.project_path.joinpath(".github", "workflows", "test-coverage-lint.yml").is_file()
    assert not result.project_path.joinpath(".github", "workflows", "publish-to-pypi-uv.yml").is_file()
    assert not result.project_path.joinpath(".github", "workflows", "test-coverage-lint-uv.yml").is_file()


def test_bake_project_docker_uv(cookies, bake_project_docker_uv: dict):
    """Test baking project with docker and uv

    Args:
        cookies (pytest-cookie): pytest-cookie function
        bake_project_docker_uv (dict): fixture with docker and uv options
    """
    result = cookies.bake(extra_context=bake_project_docker_uv)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "docker-project-uv"
    assert result.project_path.is_dir()
    assert result.project_path.joinpath("README.md").is_file()
    assert not result.project_path.joinpath("requirements.txt").is_file()
    assert not result.project_path.joinpath("requirements-dev.txt").is_file()
    assert result.project_path.joinpath("containers").is_dir()
    assert not result.project_path.joinpath("containers", "Containerfile").is_file()
    assert result.project_path.joinpath("containers", "Dockerfile").is_file()
    assert result.project_path.joinpath("tests").is_dir()
    assert result.project_path.joinpath("tests", "conftest.py").is_file()
    assert result.project_path.joinpath("tests", "data").is_dir()
    assert result.project_path.joinpath("tests", "data", "README.md").is_file()
    assert not result.project_path.joinpath(".github", "workflows", "publish-to-pypi.yml").is_file()
    assert not result.project_path.joinpath(".github", "workflows", "test-coverage-lint.yml").is_file()
    assert result.project_path.joinpath(".github", "workflows", "publish-to-pypi-uv.yml").is_file()
    assert result.project_path.joinpath(".github", "workflows", "test-coverage-lint-uv.yml").is_file()


def test_bake_project_django_addons(cookies, bake_project_django_addons: dict):
    """Test baking project with django addons

    Args:
        cookies (pytest-cookie): pytest-cookie function
        bake_project_django_addons (dict): fixture with django addons options
    """
    result = cookies.bake(extra_context=bake_project_django_addons)

    # Reads pyproject.toml and converts to python objects
    with open(result.project_path.joinpath("pyproject.toml"), "r", encoding="utf-8") as file:
        toml = file.read()
    pyproject_toml = tomli.loads(toml)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "django-project-addons"
    assert result.project_path.is_dir()
    assert pyproject_toml["project"]["dependencies"].count("django-environ") == 1
    assert pyproject_toml["project"]["dependencies"].count("django-markdownx") == 1
