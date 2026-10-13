import pytest, requests
from config import BASE_URL, USERNAME, PASSWORD

HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
PAYLOAD = {
    "firstname": "Test", "lastname": "User", "totalprice": 150, "depositpaid": True,
    "bookingdates": {"checkin": "2026-11-01", "checkout": "2026-11-05"},
    "additionalneeds": "Breakfast",
}

def timed(resp, limit=2.0):
    assert resp.elapsed.total_seconds() < limit, f"slow: {resp.elapsed.total_seconds()}s"

@pytest.fixture(scope="session")
def token():
    r = requests.post(f"{BASE_URL}/auth", json={"username": USERNAME, "password": PASSWORD}, headers=HEADERS)
    assert r.status_code == 200 and "token" in r.json()
    return r.json()["token"]

@pytest.fixture
def booking(token):
    """Create a fresh booking for a test; delete it afterwards."""
    r = requests.post(f"{BASE_URL}/booking", json=PAYLOAD, headers=HEADERS)
    assert r.status_code == 200
    bid = r.json()["bookingid"]
    yield bid
    requests.delete(f"{BASE_URL}/booking/{bid}", headers={**HEADERS, "Cookie": f"token={token}"})
