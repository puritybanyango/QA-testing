# API findings (Restful Booker)

> Verify each by running the suite and add real response bodies. Listed from my testing plan.

| ID | Finding | Expected | Actual |
| F-01 | Wrong password on `auth` | 401 Unauthorized | 200 OK with `{"reason":"Bad credentials"}` |
| F-02 | `DELETE /booking/{id}` success code | 200 or 204 | 201 Created |
| F-03 | POST with missing field / wrong type | 400 with a validation message | 500 Internal Server Error (or accepted) |
| F-04 | DELETE/PUT on a booking that does not exist | 404 Not Found | 405 Method Not Allowed |
| F-05 | `Accept` header handling | 406 if unsupported | Behaviour depends on header; check |
