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

def test_application_init(client):
    response = client.get_schema(os.environ['INTUITION_TEST_APP_ID'])
    app = Application(**response['table'])
    assert app

def test_application_get(client):
    app = Application.get(os.environ['INTUITION_TEST_APP_ID'], client)
    assert app
