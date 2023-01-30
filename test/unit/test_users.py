import json
from test.unit import client


def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()
    assert '<img class="avatar" src="https://avatars.githubusercontent.com/u/1?v=4" alt="mojombo">' in html
    assert landing.status_code == 200


def test_pagination(client):
    users_page = client.get("/users/2?pagination=5")
    html = users_page.data.decode()
    assert '<img class="avatar" src="https://avatars.githubusercontent.com/u/1?v=4" alt="mojombo">' not in html


def test_fetch_users(client):
    data = client.get("/api/users/profiles")
    raw = data.data.decode()
    response = json.loads(raw)
    assert len(response['data']['rows']) == 15
    assert response['data']['rows'][0] is not None


def test_fetch_users_pagination(client):
    data = client.get("/api/users/profiles?page=2&&pagination=5")
    raw = data.data.decode()
    response = json.loads(raw)
    assert len(response['data']['rows']) == 5


def test_fetch_users_filter_id(client):
    data = client.get("/api/users/profiles?id=1")
    raw = data.data.decode()
    response = json.loads(raw)
    assert len(response['data']['rows']) == 1


def test_fetch_users_filter_username(client):
    data = client.get("/api/users/profiles?username=mojombo")
    raw = data.data.decode()
    response = json.loads(raw)
    assert len(response['data']['rows']) == 1
