# cookiecutter-python-django

| BRANCH | STATUS |
| ------ |--------|
| main | [![Unit-Testing, Coverage, Linting](https://github.com/naturalblaze/cookiecutter-python-django/actions/workflows/test-bake.yml/badge.svg)](https://github.com/naturalblaze/cookiecutter-python-django/actions/workflows/test-bake.yml) |
| develop | [![Unit-Testing, Coverage, Linting](https://github.com/naturalblaze/cookiecutter-python-django/actions/workflows/test-bake.yml/badge.svg)](https://github.com/naturalblaze/cookiecutter-python-django/actions/workflows/test-bake.yml) |

* This is a "cookiecutter" repository designed to be used as a framework to create repository structure for Python Django projects.

## How to use a "cookiecutter" repository

1. First install the python library called [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/)

   ```bash
   # Via pip
   pip install cookiecutter

   # Via uv
   uv add cookiecutter
   ```

1. Create a **TOTALLY** empty repository in a GIT based system. In my example I am creating a repo called
   throw-me-away.

1. Use the cookiecutter repository to create your structure.

   * Use the latest

      * HTTPS

      ```bash
      cookiecutter https://github.com/naturalblaze/cookiecutter-python-django
      ```

      * SSH

      ```bash
      cookiecutter git@github.com:naturalblaze/cookiecutter-python-django.git
      ```

   * Use a specific version

      * HTTPS

      ```bash
      cookiecutter https://github.com/naturalblaze/cookiecutter-python-django.git -c 1.0.1
      ```

      * SSH

      ```bash
      cookiecutter git@github.com:naturalblaze/cookiecutter-python-django.git -c 1.0.1
      ```

   * Use a specific branch with `UV`

   ```bash
   uvx cookiecutter git@github.com:naturalblaze/cookiecutter-python-django.git --checkout develop
   ```

   * Use a `YAML` configuration input file with `UV`

   ```bash
   uvx cookiecutter -f --no-input --config-file test-repo.yml git@github.com:naturalblaze/cookiecutter-python-django.git
   ```

1. Now you will be asked a series of questions. This is an example
   **THE QUESTIONS MAY NOT BE THE EXACT FOR THIS COOKIECUTTER**, also if you have downloaded it before
   you will be asked if you want to download it again, always say yes to get the latest version.

   ```bash
   [1/15] Your Full Name (Firstname Lastname): Blaze B
   [2/15] Your E-Mail Address (example@example.com): somename@example.com
   [3/15] Your GitHub Username or GitHub Organization Name (some-username): naturalblaze
   [4/15] The Repository Name (some-repo-name): throw-me-away
   [5/15] The full GIT URL (https://github.com/some-username/some-repo-name): https://github.com/naturalblaze/throw-me-away
   [6/15] A short description (A short description): Super Awesome Django Project
   [7/15] Library Version (0.1.0): 0.1.0
   [8/15] Where will the documentation be hosted
      1 - Read the Docs
      2 - GitHub Pages
      Choose from [1/2] (1): 1
   [9/15] Which theme will be used for the documentation
      1 - Read the Docs Theme
      2 - Alabaster Theme
      Choose from [1/2] (1): 1
   [10/15] Which minimum Python version will be supported
      1 - 3.9
      2 - 3.10
      3 - 3.11
      4 - 3.12
      5 - 3.13
      Choose from [1/2/3/4/5] (1): 2
   [11/15] Which pacakge manager for Python will be supported
      1 - UV By Astral
      2 - PIP (The built in Python Package Installer)
      Choose from [1/2] (1): 1
   [12/15] Will you use the Django Environment library
      1 - No
      2 - Yes
      Choose from [1/2] (1): 2
   [13/15] Will you use the Django MarkdownX library
      1 - No
      2 - Yes
      Choose from [1/2] (1): 2
   [14/15] Which container runtime will be used
      1 - Podman
      2 - Docker
      Choose from [1/2] (1): 1
   [15/15] Which protocol will be used for installing in the container
      1 - SSH
      2 - HTTPS
      Choose from [1/2] (1): 1
   ```

   ### Input file example

   ```yaml
   ---
   default_context:
      full_name: "Blaze B"
      email: "nsomename@example.com"
      git_username: "naturalblaze"
      git_repo_name: "throw-me-away"
      git_url: "https://github.com/naturalblaze/throw-me-away"
      app_description: "Super Awesome Django Project"
      app_version: "0.1.0"
      app_documents_location: "readthedocs.io" or "github-pages"
      app_documents_theme: "sphinx_rtd_theme" or "alabaster"
      minimum_python_version: 3.9" or "3.10" or "3.11" or "3.12" or "3.13"
      package_manager: "uv" or "pip"
      use_django_environ: "y" or "n"
      use_django_markdownx: "y" or "n"
      container_runtime: "podman" or "docker"
      container_git_protocol: "ssh" or "https"
   ```

1. Now initialize it and push it up to the GIT based system.

   ```bash
   cd <git_repo_name>/
   git init -b main
   git add --all
   git commit -m "Cookiecutter bake"
   git remote add origin https://github.com/naturalblaze/throw-me-away.git
   git push -u origin main
   ```

1. Follow the `README.md` instructions in your repo to initialize your project
