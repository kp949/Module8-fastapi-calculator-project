import socket
import subprocess
import sys
import time
from urllib.request import urlopen

import pytest
from playwright.sync_api import expect, sync_playwright


def find_free_port():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


@pytest.fixture(scope="session")
def live_server():
    port = find_free_port()
    url = f"http://127.0.0.1:{port}"
    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "main:app",
            "--host",
            "127.0.0.1",
            "--port",
            str(port),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    for _ in range(50):
        try:
            with urlopen(f"{url}/health", timeout=1) as response:
                if response.status == 200:
                    break
        except OSError:
            time.sleep(0.1)
    else:
        process.terminate()
        raise RuntimeError("FastAPI test server did not start")

    yield url

    process.terminate()
    process.wait(timeout=10)


def test_calculator_addition(live_server):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(live_server)

        expect(page.get_by_role("heading", name="FastAPI Calculator")).to_be_visible()
        page.locator("#a").fill("2")
        page.locator("#b").fill("3")
        page.locator("#operation").select_option("add")
        page.locator("#calculate").click()

        expect(page.locator("#result")).to_have_text("Result: 5")
        browser.close()
