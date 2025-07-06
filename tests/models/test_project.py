import pytest
from portfolio.factories import ProjectFactory

@pytest.fixture
def project_published():
    return ProjectFactory(title='Projeto com Pytest')

@pytest.mark.django_db
def test_create_published_project(project_published):
    assert project_published.title == 'Projeto com Pytest'
    assert project_published.status == 1
    assert project_published.author.username is not None
    assert project_published.github_link.startswith('http')
