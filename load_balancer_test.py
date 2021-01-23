from load_balancer import loadbalancer

import pytest


@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client


def test_host_routing_hello(client):
    result = client.get("/hello", headers={"Host": "www.hello.com"})
    assert b'This is the hello application.' in result.data


def test_host_routing_golumolu(client):
    result = client.get('/golumolu', headers={"Host": "www.golumolu.com"})
    assert b'This is the golumolu application.' in result.data


def test_host_routing_notfound(client):
    result = client.get('/', headers={"Host": "www.notfound.com"})
    assert b'Not Found' in result.data
    assert 404 == result.status_code
