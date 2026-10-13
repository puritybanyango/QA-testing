# Test summary: Sauce Demo release readiness

**Tested:** Task 2 manual exploratory (login, list, details, cart, checkout as problem_user vs standard_user); Task 3 API suite (15 tests, Restful Booker); Task 5 UI automation (4 tests).
**Not tested:** other users (performance_glitch_user, error_user, visual_user), mobile/other browsers, accessibility, security, payment (none in app), real data volumes.

**Results:**
Automation: 4 passed. 
API: 15 passed.
Manual: 4 bugs (1 critical, 1 high, 2 medium).

**Top 3 risks if released today**
1. Checkout can fail for affected users, so orders are lost.
2. Cart add/remove unreliable, so wrong or missing items.
3. Product images/sorting wrong, so buyers can't identify or find products.

**Recommendation:** WAIT until the checkout and cart defects are fixed and re-tested.

**Next time:** cross-browser and mobile runs, accessibility checks, remaining user types, negative checkout validation, wider API boundary tests, higher-load k6 on a private environment.
