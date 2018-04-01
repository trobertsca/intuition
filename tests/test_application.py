import os
import pytest
from pyintuition.orm import Application
from pyintuition import Intuition

@pytest.fixture(scope="module")
def client():
    from pyintuition import Intuition
    _client = Intuition(os.environ['INTUITION_TEST_URL'], 
                        app_token = os.environ['INTUITION_TEST_APP_TOKEN'] 
    )
    _client.authenticate(os.environ['INTUITION_TEST_USER'], os.environ['INTUITION_TEST_PW'], 1)
    _client.test_rid = None
    return _client

@pytest.fixture(scope="module")
def app(client):
    app = Application.get(os.environ['INTUITION_TEST_APP_ID'], client)
    return app

def test_application_get(client, app):
    assert app
