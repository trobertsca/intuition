import os
import pytest

@pytest.fixture(scope="module")
def client():
    from pyintuition.client import Intuition
    _client = Intuition(os.environ['INTUITION_TEST_URL'], app_token=os.environ['INTUITION_TEST_APP_TOKEN'])
    _client.authenticate(os.environ['INTUITION_TEST_USER'], os.environ['INTUITION_TEST_PW'], 1)
    _client.test_rid = None
    return _client

@pytest.mark.run(order=1)
def test_authentication(client):
    assert client.ticket

@pytest.mark.run(order=2)
def test_add_record(client):
    record = {
        'upc': '723755122161',
        'description': 'Moto G 5 Plus',
        'quantity': 10,
        'shelf_code': 'B1010',
        'restock_floor': 5,
        'restock_ceiling': 11,
        'units_per': 1
    }
    response = client.add_record("bni4qnmfm", record)
    client.test_rid = response['rid']
    assert response['errcode'] == '0'

@pytest.mark.run(order=3)
def test_do_query_single_record(client):
    response = client.do_query("bni4qnmfm", "{6.EX.'723755122161'}")
    assert response['errcode'] == '0'
    assert response['record']['upc'] == '723755122161'

@pytest.mark.run(order=4)
def test_update_record(client):
    record = {
        'rid': client.test_rid,
        'quantity': 5
    }
    response = client.update_record("bni4qnmfm", record)
    assert response['errcode'] == '0'

@pytest.mark.run(order=5)
def test_delete_record(client):
    rid = client.test_rid
    client.test_rid = None
    response = client.delete_record("bni4qnmfm", rid)
    assert response['errcode'] == '0'
