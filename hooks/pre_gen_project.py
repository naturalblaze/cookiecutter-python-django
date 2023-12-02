"""
pre generation hooks for cookiecutter to validate data
"""
import re
import sys


def validate_git_repo_name() -> None:
    """Validate git_repo_name

    :rtype: None
    :returns: Nothing it exits if the git_repo_name is invalid
    """
    arg_regex = r'^([A-Z]|[a-z]|[0-9]|-{1})+$'
    arg_name = '{{ cookiecutter.git_repo_name }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid git_repo_name!')
        sys.exit(1)


def validate_full_name() -> None:
    """Validate full_name

    :rtype: None
    :returns: Nothing it exits if the full_name is invalid
    """
    arg_regex = r'^\S.*\S$'
    arg_name = '{{ cookiecutter.full_name }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid full_name only single spaces are allowed!')
        sys.exit(1)


def validate_email():
    """Validate email

    :rtype: None
    :returns: Nothing it exits if the email is invalid
    """
    arg_regex = r'^\S+$'
    arg_name = '{{ cookiecutter.email }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid email no spaces allowed!')
        sys.exit(1)


def validate_git_username() -> None:
    """Validate git_username

    :rtype: None
    :returns: Nothing it exits if the git_username is invalid
    """
    arg_regex = r'^\S+$'
    arg_name = '{{ cookiecutter.git_username }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid git_username no spaces allowed!')
        sys.exit(1)


def validate_git_url() -> None:
    """Validate git_url

    :rtype: None
    :returns: Nothing it exits if the git_url is invalid
    """
    arg_regex = r'^https://\S+$'
    arg_name = '{{ cookiecutter.git_url }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid git_url no spaces allowed!')
        sys.exit(1)


def validate_app_description() -> None:
    """Validate app_description

    :rtype: None
    :returns: Nothing it exits if the app_description is invalid
    """
    arg_regex = r'^\S.*\S$'
    arg_name = '{{ cookiecutter.app_description }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid app_description only single spaces are allowed!')
        sys.exit(1)


def validate_app_version() -> None:
    """Validate app_version

    :rtype: None
    :returns: Nothing it exits if the app_version is invalid
    """
    arg_regex = r'^\d+\.\d+\.\d+$'
    arg_name = '{{ cookiecutter.app_version }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid app_version should be semantic X.X.X!')
        sys.exit(1)


if __name__ == '__main__':
    validate_full_name()
    validate_email()
    validate_git_username()
    validate_git_repo_name()
    validate_git_url()
    validate_app_description()
    validate_app_version()
