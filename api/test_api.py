from api import app 

def test_jenkins():
    resp = app.test_client().get('/jenkins')
    assert resp.get_json() == {'resp': 'It ran'}