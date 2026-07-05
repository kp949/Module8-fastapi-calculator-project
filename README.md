# Module 8 FastAPI Calculator

This is my Module 8 calculator web application. It uses FastAPI for the API and a simple browser page for the calculator form.

## Features

- FastAPI web application
- Browser calculator page
- Jinja2 HTML template
- JavaScript frontend file
- Separate API endpoints for add, subtract, multiply, and divide
- Addition, subtraction, multiplication, and division
- Error handling for invalid operations and division by zero
- Logging for requests, operations, and errors
- Unit tests for `operations.py`
- Integration tests for API endpoints
- End-to-end test with Playwright
- GitHub Actions workflow that runs all tests

## Project Files

- `main.py` has the FastAPI app and routes.
- `app/operations.py` has the calculator functions.
- `templates/index.html` has the calculator web page.
- `static/calculator.js` has the browser interaction code.
- `test_operations.py` has unit tests.
- `test_api.py` has integration tests for the API.
- `test_e2e.py` has the Playwright browser test.
- `.github/workflows/ci.yml` runs the tests in GitHub Actions.
- `Dockerfile` can build the app container.
- `docker-compose.yml` includes the web app, PostgreSQL, and Redis services.

## Set Up

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
python -m playwright install chromium
```

Run the app:

```powershell
uvicorn main:app --reload
```

Open the browser at:

```text
http://127.0.0.1:8000
```

Run tests:

```powershell
pytest
```

Run with Docker Compose:

```powershell
docker compose up --build
```

## API

Health check:

```text
GET /health
```

Calculate:

```text
POST /add
POST /subtract
POST /multiply
POST /divide
```

Example JSON body:

```json
{
  "a": 10,
  "b": 5
}
```
