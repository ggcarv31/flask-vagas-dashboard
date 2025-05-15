from app import create_app
import pytest

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dashboard_route(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'Resumo de vagas' in res.data

    