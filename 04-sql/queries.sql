-- Setup: run the script from the brief first (SQLite).

-- 1. Every claim with member, provider, amount, status, newest first
SELECT c.id, m.name AS member, p.name AS provider, c.amount, c.status, c.submitted_on
FROM claims c
JOIN members m   ON m.id = c.member_id
JOIN providers p ON p.id = c.provider_id
ORDER BY c.submitted_on DESC, c.id DESC;

-- 2. Total approved amount per employer (LEFT JOIN keeps employers with none)
SELECT e.name AS employer, COALESCE(SUM(c.amount), 0) AS approved_total
FROM employers e
LEFT JOIN members m ON m.employer_id = e.id
LEFT JOIN claims c  ON c.member_id = m.id AND c.status = 'approved'
GROUP BY e.id, e.name;

-- 3. Members who never submitted a claim
SELECT m.id, m.name
FROM members m
LEFT JOIN claims c ON c.member_id = m.id
WHERE c.id IS NULL;

-- 4. Claims submitted after the member's policy ended
SELECT c.id, m.name, m.policy_end, c.submitted_on, c.status, c.amount
FROM claims c
JOIN members m ON m.id = c.member_id
WHERE c.submitted_on > m.policy_end;

-- 5. Possible duplicate claims (same member, provider, amount, date)
SELECT member_id, provider_id, amount, submitted_on,
       COUNT(*) AS times, GROUP_CONCAT(id) AS claim_ids
FROM claims
GROUP BY member_id, provider_id, amount, submitted_on
HAVING COUNT(*) > 1;
