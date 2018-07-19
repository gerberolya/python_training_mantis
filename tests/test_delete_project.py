from model.project import Project
from data.projects import testdata
import pytest
from random import randrange


#@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_delete_project(app):
    if app.project.count_projects() == 0:
        app.project.create(Project(name="to_delete"))
    old_projects = app.project.get_projects_list()
    index = randrange(len(old_projects))
    app.project.delete_project_by_index(index)
    new_projects = app.project.get_projects_list()
    assert len(old_projects) - 1 == len(new_projects)
