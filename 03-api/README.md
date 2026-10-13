# Task 3: API tests (pytest + requests) against Restful Booker

```
cd 03-api
pip install -r requirements.txt
pytest -v
```
Config via env vars: `BASE_URL`, `RB_USERNAME`, `RB_PASSWORD` (defaults in `config.py`: the public practice login).
The booking ID flows from the `booking` fixture into each test; the token comes from the `token` fixture.
