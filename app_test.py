import pytest
from flask_app import app_100, add_numbers

# 開一個假的瀏覽器測試環境，用完即刪
@pytest.fixture
def client():
    app_100.config['TESTING'] = True
    with app_100.test_client() as client:
        yield client

def test_health(client):
    # 測試"/healthz"路由
    response = client.get('/healthz')
    assert response.status_code == 200
    # 回傳內容是否為json格式
    assert response.content_type == "application/json"
    # 端點內的json內容，staus欄位是否為"ok"
    assert response.get_json()["status"] == "ok"

def test_hello_route_exists(client):
    # 測試"/hello"路由
    response = client.get("/hello")
    assert response.status_code == 200

def test_add_numbers():
    # 測試加法函數
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
