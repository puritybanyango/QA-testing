# API findings (Restful Booker)

Found by running `pytest -v` in `03-api/` (15 tests, all within the 2-second limit).
Base URL: https://restful-booker.herokuapp.com

## Summary

| ID | Endpoint | Finding | Expected | Actual | Severity | Confirmed by |
| F-01 | POST /auth | Wrong password is not rejected with an error status | 401 Unauthorized | 200 OK with `{"reason":"Bad credentials"}` | Medium | test_02 |
| F-02 | DELETE /booking/{id} | Success returns "Created" | 200 OK or 204 No Content | 201 Created | Low | test_11 |
| F-03 | POST /booking | Missing required field crashes the server | 400 Bad Request with a validation message | 500 Internal Server Error | Medium | test_14 |
| F-04 | DELETE /booking/{id} | Deleting a booking that doesn't exist | 404 Not Found | 405 Method Not Allowed | Low | test_13 |

## Details

### F-01: Wrong password returns 200
- **Request:** `POST /auth` with `{"username":"admin","password":"wrong"}`
- **Expected:** 401 Unauthorized, no token.
- **Actual:** 200 OK, body `{"reason":"Bad credentials"}`, no token.
- **Why it matters:** Clients that treat any 200 as success may think the login worked. They have to read the body to find out it failed.

### F-02: DELETE returns 201 Created
- **Request:** `DELETE /booking/{id}` with a valid token.
- **Expected:** 200 OK or 204 No Content.
- **Actual:** 201 Created. The booking is deleted correctly (a follow-up GET returns 404).
- **Why it matters:** 201 means a resource was created, which is the opposite of what happened. This can confuse clients and monitoring.

### F-03: Missing required field returns 500
- **Request:** `POST /booking` with `firstname` removed.
- **Expected:** 400 Bad Request explaining which field is missing.
- **Actual:** 500 Internal Server Error.
- **Why it matters:** A 500 says the server failed, not that the client sent bad input. It gives the caller no help and may hide a crash in the code.

### F-04: Deleting a missing booking returns 405
- **Request:** `DELETE /booking/99999999` with a valid token.
- **Expected:** 404 Not Found.
- **Actual:** 405 Method Not Allowed.
- **Why it matters:** DELETE is allowed on bookings, so 405 is misleading. The real problem is that the booking doesn't exist.

