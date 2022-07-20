"""
App Entrypoint
"""
import uvicorn


if __name__ == '__main__':  # pragma: no cover
    uvicorn.run('modules:web_app', reload=True, host='0.0.0.0', port=8080)
