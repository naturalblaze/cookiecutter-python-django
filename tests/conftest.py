import os
import sys
import pytest
base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))


@pytest.fixture
def bake_project_api_only() -> dict:
    options = {
        'git_repo_name': 'api-only',
        'include_cli': 'y',
        'email': 'name@example.com',
        'git_username': 'some-username',
        'git_url': 'https://github.com/some-username/python-with-cli',
    }

    return options
