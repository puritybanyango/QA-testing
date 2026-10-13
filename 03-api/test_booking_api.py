import copy, requests
from config import BASE_URL, USERNAME
from conftest import HEADERS, PAYLOAD, timed

def auth(token): return {**HEADERS, "Cookie": f"token={token}"}

# Auth 
def test_01_auth_valid_credentials():
    r = requests.post(f"{BASE_URL}/auth", json={"username": USERNAME, "password": "password123"}, headers=HEADERS)
    assert r.status_code == 200
    assert isinstance(r.json().get("token"), str) and r.json()["token"]
    timed(r)

def test_02_auth_wrong_password():
    r = requests.post(f"{BASE_URL}/auth", json={"username": USERNAME, "password": "wrong"}, headers=HEADERS)
    assert r.status_code == 200
    assert r.json().get("reason") == "Bad credentials"
    assert "token" not in r.json()
    timed(r)

# Create 
def test_03_create_booking():
    r = requests.post(f"{BASE_URL}/booking", json=PAYLOAD, headers=HEADERS)
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body["bookingid"], int)
    assert body["booking"]["firstname"] == "Test"
    assert body["booking"]["bookingdates"]["checkin"] == "2026-11-01"
    timed(r)

def test_04_get_booking_by_id(booking):
    r = requests.get(f"{BASE_URL}/booking/{booking}", headers=HEADERS)
    assert r.status_code == 200
    assert r.json()["lastname"] == "User" and r.json()["totalprice"] == 150
    timed(r)

def test_05_get_booking_ids_contains_new(booking):
    r = requests.get(f"{BASE_URL}/booking", headers=HEADERS)
    assert r.status_code == 200
    assert booking in [b["bookingid"] for b in r.json()]
    timed(r)

def test_06_get_nonexistent_booking():
    r = requests.get(f"{BASE_URL}/booking/99999999", headers=HEADERS)
    assert r.status_code == 404
    timed(r)

# Update 
def test_07_put_full_update(booking, token):
    data = copy.deepcopy(PAYLOAD); data["firstname"] = "Updated"; data["totalprice"] = 999
    r = requests.put(f"{BASE_URL}/booking/{booking}", json=data, headers=auth(token))
    assert r.status_code == 200
    assert r.json()["firstname"] == "Updated" and r.json()["totalprice"] == 999
    timed(r)

def test_08_patch_partial_update(booking, token):
    r = requests.patch(f"{BASE_URL}/booking/{booking}", json={"lastname": "Patched"}, headers=auth(token))
    assert r.status_code == 200
    assert r.json()["lastname"] == "Patched"
    assert r.json()["firstname"] == "Test"      
    timed(r)

def test_09_put_without_token(booking):
    r = requests.put(f"{BASE_URL}/booking/{booking}", json=PAYLOAD, headers=HEADERS)
    assert r.status_code == 403
    timed(r)

def test_10_put_with_wrong_token(booking):
    r = requests.put(f"{BASE_URL}/booking/{booking}", json=PAYLOAD, headers=auth("badtoken123"))
    assert r.status_code == 403
    timed(r)

#Delete
def test_11_delete_booking_then_get_404(token):
    bid = requests.post(f"{BASE_URL}/booking", json=PAYLOAD, headers=HEADERS).json()["bookingid"]
    r = requests.delete(f"{BASE_URL}/booking/{bid}", headers=auth(token))
    assert r.status_code == 201
    timed(r)
    assert requests.get(f"{BASE_URL}/booking/{bid}", headers=HEADERS).status_code == 404

def test_12_delete_without_token(booking):
    r = requests.delete(f"{BASE_URL}/booking/{booking}", headers=HEADERS)
    assert r.status_code == 403
    timed(r)

def test_13_delete_nonexistent_booking(token):
    r = requests.delete(f"{BASE_URL}/booking/99999999", headers=auth(token))
    assert r.status_code == 405
    timed(r)

# negative tests
def test_14_create_missing_required_field():
    data = copy.deepcopy(PAYLOAD); del data["firstname"]
    r = requests.post(f"{BASE_URL}/booking", json=data, headers=HEADERS)
    assert r.status_code == 500
    timed(r)

def test_15_create_wrong_data_type():
    data = copy.deepcopy(PAYLOAD); data["totalprice"] = "not-a-number"
    r = requests.post(f"{BASE_URL}/booking", json=data, headers=HEADERS)
    assert r.status_code in (400, 500, 200)
    timed(r)
