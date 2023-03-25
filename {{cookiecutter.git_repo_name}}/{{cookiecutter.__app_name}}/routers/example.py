"""
This is an example FIXME: Example delete this
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel  # pylint: disable=no-name-in-module
from {{cookiecutter.__app_name}}.utils.schemas import ErrorSchema


router = APIRouter(
    prefix='/api/v1',
    responses={400: {'model': ErrorSchema}, 401: {'model': ErrorSchema}},
    tags=['example']
)


class ResponseSchema(BaseModel):  # pylint: disable=too-few-public-methods
    """Schema for example"""
    response: str


@router.get('/example/{name}',
             responses={200: {'model': ResponseSchema}},
             description='This is an example',
             name='Example endpoint')
async def get_example(name: str) -> ResponseSchema:
    """Function for the example endpoint

    :type name: String
    :param name: A name

    :rtype: ResponseSchema
    :returns: The JSON Data

    :raises HTTPException: If anything goes wrong
    """
    try:
        result = ResponseSchema(response=name)

    except Exception as error:  # pragma: no cover
        raise HTTPException(status_code=400, detail=f'{error}') from error

    return result
