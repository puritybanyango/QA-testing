# Task 1: Test cases, "Book an appointment"

BVA = boundary value analysis. Priority: High/Medium/Low.

| ID | Title | Preconditions | Steps | Test data | Expected result | Priority |
|----|-------|---------------|-------|-----------|-----------------|----------|
| TC-01 | Book with active policy and in-network provider (happy path) | Member logged in, policy active, 0 upcoming appts | 1. Open Book appointment 2. Choose in-network provider 3. Pick a free slot tomorrow 10:00 4. Confirm | In-network clinic, tomorrow 10:00 | Booking created, appears in "Upcoming" | High |
| TC-02 | Member with expired policy cannot book | Policy end date = yesterday | 1. Open Book appointment 2. Try to pick provider and slot | Expired policy | Booking blocked with clear message about policy status | High |
| TC-03 | Out-of-network provider cannot be booked | Active policy | 1. Search for an out-of-network provider 2. Try to book | Out-of-network provider | Provider not offered, or booking rejected with message | High |
| TC-04 | Confirmation in-app and SMS after booking | Active policy, fake phone number on file | 1. Book a valid slot 2. Check notifications 3. Check SMS test inbox | Fake number +254700000000 | In-app confirmation and SMS received, with correct provider, date and time | High |
| TC-05 (BVA) | Book exactly 30 days ahead | Active policy | 1. Pick date today+30 2. Pick a free slot 3. Confirm | today+30, 10:00 | Booking succeeds | High |
| TC-06 (BVA) | Book 31 days ahead is rejected | Active policy | 1. Try to select today+31 (calendar or via API) | today+31 | Date not selectable / booking rejected with message | High |
| TC-07 (BVA) | First slot of the day (08:00) | Active policy | 1. Select tomorrow 08:00 2. Confirm | 08:00 | Booking succeeds | Medium |
| TC-08 (BVA) | Last slot 16:30-17:00 bookable; 17:00 start is not | Active policy | 1. Book 16:30 2. Try to book 17:00 | 16:30 and 17:00 | 16:30 succeeds; 17:00 not offered or rejected | Medium |
| TC-09 (BVA) | Slot before 08:00 not offered | Active policy | 1. View tomorrow's slots 2. Try 07:30 (via API if hidden in UI) | 07:30 | No 07:30 slot; direct request rejected | Medium |
| TC-10 | Cannot book a slot already passed today | Active policy, current time 14:10 | 1. Open today's slots 2. Try 13:30 | Past slot | Only slots after current time are selectable | High |
| TC-11 (BVA) | Third upcoming appointment is allowed | Member has 2 upcoming | 1. Book a third appointment | 3rd appt | Booking succeeds | High |
| TC-12 (BVA) | Fourth upcoming appointment is rejected | Member has 3 upcoming | 1. Try to book a fourth | 4th appt | Rejected with message about the limit of 3 | High |
| TC-13 | Cancelling frees a place in the limit | Member has 3 upcoming | 1. Cancel one (>2 h before) 2. Book a new one | n/a | Cancel succeeds, new booking succeeds | Medium |
| TC-14 (BVA) | Cancel 2 h 01 min before start is free | Appt at 14:00, now 11:59 | 1. Cancel | n/a | Cancelled, no charge | High |
| TC-15 (BVA) | Cancel 1 h 59 min before start is not free | Appt at 14:00, now 12:01 | 1. Cancel | n/a | Free cancellation refused or fee shown (per answer to Q3) | High |

Extra ideas if time allows: two members booking the same slot at once; same member booking the same slot twice; cancel at exactly 2 h 00 min.

## Questions for the product manager
1. Does "17:00" mean the last slot starts at 16:30 (ends 17:00), or can a slot start at 17:00? Is today+30 the last allowed day?
2. Do cancelled or completed appointments count toward the limit of 3, and does "upcoming" include today's appointments that haven't started?
3. What happens when cancelling less than 2 hours before: blocked, or allowed with a fee? And if the SMS fails, should the booking still stand?



