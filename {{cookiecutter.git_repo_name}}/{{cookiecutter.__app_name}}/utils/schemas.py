"""
pydantic schemas
"""
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class ErrorSchema(BaseModel):  # pylint: disable=too-few-public-methods
    """Schema for simple Errors"""
    detail: str
