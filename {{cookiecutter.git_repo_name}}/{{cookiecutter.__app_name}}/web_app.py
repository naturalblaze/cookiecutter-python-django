"""
FastAPI WebApp
"""
from fastapi import FastAPI
from {{cookiecutter.__app_name}}.version import __version__
from {{cookiecutter.__app_name}}.routers import example


web_app = FastAPI(title='{{ cookiecutter.git_repo_name }}', version=__version__,
                  description='{{ cookiecutter.app_description }}')
web_app.include_router(example.router)
