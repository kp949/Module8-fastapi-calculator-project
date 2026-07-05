from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home_page_loads():
    response = client.get("/")

    assert response.status_code == 200
    assert "FastAPI Calculator" in response.text
    assert "id=\"calculate\"" in response.text


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add_endpoint_success():
    response = client.post("/add", json={"a": 6, "b": 7})

    assert response.status_code == 200
    assert response.json() == {"result": 13.0}


def test_subtract_endpoint_success():
    response = client.post("/subtract", json={"a": 10, "b": 4})

    assert response.status_code == 200
    assert response.json() == {"result": 6.0}


def test_multiply_endpoint_success():
    response = client.post("/multiply", json={"a": 6, "b": 7})

    assert response.status_code == 200
    assert response.json() == {"result": 42.0}


def test_divide_endpoint_success():
    response = client.post("/divide", json={"a": 9, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"result": 3.0}


def test_divide_endpoint_division_by_zero():
    response = client.post("/divide", json={"a": 6, "b": 0})

    assert response.status_code == 400
    assert response.json() == {"error": "Cannot divide by zero!"}


def test_endpoint_rejects_bad_request():
    response = client.post("/add", json={"a": "not a number", "b": 2})

    assert response.status_code == 400
    assert "Both a and b must be numbers" in response.json()["error"]


def test_add_endpoint_handles_operation_error(monkeypatch):
    def broken_add(a, b):
        raise RuntimeError("add failed")

    monkeypatch.setattr("main.add", broken_add)

    response = client.post("/add", json={"a": 1, "b": 2})

    assert response.status_code == 400
    assert response.json() == {"error": "add failed"}


def test_subtract_endpoint_handles_operation_error(monkeypatch):
    def broken_subtract(a, b):
        raise RuntimeError("subtract failed")

    monkeypatch.setattr("main.subtract", broken_subtract)

    response = client.post("/subtract", json={"a": 1, "b": 2})

    assert response.status_code == 400
    assert response.json() == {"error": "subtract failed"}


def test_multiply_endpoint_handles_operation_error(monkeypatch):
    def broken_multiply(a, b):
        raise RuntimeError("multiply failed")

    monkeypatch.setattr("main.multiply", broken_multiply)

    response = client.post("/multiply", json={"a": 1, "b": 2})

    assert response.status_code == 400
    assert response.json() == {"error": "multiply failed"}


def test_divide_endpoint_handles_unexpected_error(monkeypatch):
    def broken_divide(a, b):
        raise RuntimeError("divide failed")

    monkeypatch.setattr("main.divide", broken_divide)

    response = client.post("/divide", json={"a": 1, "b": 2})

    assert response.status_code == 500
    assert response.json() == {"error": "Internal Server Error"}
