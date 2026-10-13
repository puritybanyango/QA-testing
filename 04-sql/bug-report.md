# BUG: Claim approved for a policy that had already ended

**Found by:** Query 4 (claims submitted after policy end)
**Environment:** SQLite, dataset from the brief
**Steps to reproduce:**
1. Run query 4 in `queries.sql`.
2. Look at claim id 4: member Wanjiru Kamau (id 3), policy_end 2026-06-30, submitted_on 2026-07-15.

**Expected:** A claim submitted after the policy end date is rejected (or flagged for manual review), never approved.
**Actual:** Claim 4 has status `approved`, amount 8000 (Baraka Dental), 15 days after the policy ended.
**Severity:** High (money is being paid out for a member who is not covered). **Priority:** High: fix validation and review whether other claims were wrongly approved.
**Note:** Query 5 also found a likely duplicate, claims 5 and 6 (Hassan Ali, Uhai Clinic, 3000, 2026-09-01), both `submitted`. That risks a double payment and deserves its own report.
