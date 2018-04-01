import os
import pytest
from pyintuition.orm import Table, Application

@pytest.fixture(scope="module")
def client():
    from pyintuition import Intuition
    _client = Intuition(os.environ['INTUITION_TEST_URL'], 
                        app_token = os.environ['INTUITION_TEST_APP_TOKEN'] 
    )
    _client.authenticate(os.environ['INTUITION_TEST_USER'], os.environ['INTUITION_TEST_PW'], 1)
    return _client

def test_table_get(client):
    app = Application.get(os.environ['INTUITION_TEST_APP_ID'], client)
    table = Table.get(os.environ['INTUITION_TEST_TABLE_ID'], client, app)
    assert table
