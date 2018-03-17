import os
import pytest
from . import secrets

@pytest.fixture(scope="module")
def client():
    from intuition.client import Intuition
    _client = Intuition(secrets.INTUITION_TEST_URL, app_token=secrets.INTUITION_TEST_APP_TOKEN)
    _client.authenticate(secrets.INTUITION_TEST_USER, secrets.INTUITION_TEST_PW, 1)
    return _client

def test_authentication(client):
    assert client.ticket

def test_do_query_single_record(client):
    response = client.do_query(secrets.INTUITION_TEST_TABLEID, secrets.INTUITION_TEST_QUERY)
    print(response)
    assert response['record']['upc'] == '07084702090'
