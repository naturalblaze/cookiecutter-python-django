import os
import sys
import pytest

base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))


@pytest.fixture
def bake_project_podman_pip() -> dict:
    options = {
        "git_repo_name": "podman-project-pip",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-django",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_podman_uv() -> dict:
    options = {
        "git_repo_name": "podman-project-uv",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "package_manager": "uv",
    }

    return options


@pytest.fixture
def bake_project_docker_pip() -> dict:
    options = {
        "git_repo_name": "docker-project-pip",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "container_runtime": "docker",
        "package_manager": "pip",
    }

    return options


@pytest.fixture
def bake_project_docker_uv() -> dict:
    options = {
        "git_repo_name": "docker-project-uv",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "container_runtime": "docker",
        "package_manager": "uv",
    }

    return options


@pytest.fixture
def bake_project_django_addons() -> dict:
    options = {
        "git_repo_name": "django-project-addons",
        "email": "name@example.com",
        "git_username": "some-username",
        "git_url": "https://github.com/some-username/python-with-cli",
        "package_manager": "uv",
        "use_django_environ": "y",
        "use_django_markdownx": "y",
    }

    return options
