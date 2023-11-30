def test_bake_project_api_only(cookies, bake_project_api_only):
    result = cookies.bake(extra_context=bake_project_api_only)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'api-only'
    assert result.project.isdir()
    assert result.project.join('README.md').isfile()
    assert result.project.join('api_only').isdir()
    assert not result.project.join('api_only', 'static').isdir()
    assert not result.project.join('api_only', 'templates').isdir()
    assert not result.project.join('api_only', 'routers', 'hello_world.py').isfile()


def test_bake_project_api_with_webpages(cookies, bake_project_api_with_webpages):
    result = cookies.bake(extra_context=bake_project_api_with_webpages)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'api-with-webpages'
    assert result.project.isdir()
    assert result.project.join('README.md').isfile()
    assert result.project.join('api_with_webpages').isdir()
    assert result.project.join('api_with_webpages', 'static').isdir()
    assert result.project.join('api_with_webpages', 'templates').isdir()
    assert result.project.join('api_with_webpages', 'routers', 'hello_world.py').isfile()
