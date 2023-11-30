def test_bake_project_api_only(cookies, bake_project_api_only):
    result = cookies.bake(extra_context=bake_project_api_only)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'api-only'
    assert result.project.isdir()
    assert result.project.join('README.md').isfile()
    assert result.project.join('api_only').isdir()
