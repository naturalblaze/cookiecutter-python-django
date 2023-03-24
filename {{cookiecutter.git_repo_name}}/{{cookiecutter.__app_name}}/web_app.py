"""
FastAPI WebApp
"""
from fastapi import FastAPI
from modules.version import __title__, __version__, __description__


web_app = FastAPI(title=__title__, version=__version__, description=__description__)
