# Task 2: Bug reports, Sauce Demo (problem_user)

**Environment :** Chrome <Version 150.0.7871.186>, <OS: Ubuntu 22.04> , <resolution: 1920x1200>, https://www.saucedemo.com, tested <13-10-2026>
**Preconditions (all):** Logged in as `problem_user` / `secret_sauce`. Compared with `standard_user`.

---
## BUG-01: All products show the same image on the product list
**Steps:** 1. Log in as problem_user. 2. Look at the product list.
**Expected:** Each product shows its own image (as for standard_user).
**Actual:** Every product shows the same dog image.
**Severity:** Medium. **Priority:** High: users can't tell what they are buying.
**Evidence:** screenshots/bug-01.png

## BUG-02: "Add to cart" / "Remove" does not work for some products
**Steps:** 1. Log in. 2. Click "Add to cart" on each product in turn. 3. Check the cart badge and button text. 4. Click "Remove" on an added product.
**Expected:** Each click adds the product, the badge increments, the button becomes "Remove"; Remove reverses it.
**Actual:** For some products the button or badge doesn't update, and Remove does not remove them. (Note exactly which products.)
**Severity:** High. **Priority:** High: core purchase flow is broken.
**Evidence:** screenshots/bug-02.png

## BUG-03: Sorting the product list has no effect
**Steps:** 1. Log in. 2. Choose "Price (low to high)" in the sort dropdown.
**Expected:** Products are reordered by price.
**Actual:** Order doesn't change.
**Severity:** Medium. **Priority:** Medium: user can still browse manually.
**Evidence:** screenshots/bug-03.png

## BUG-04: Checkout "Last name" field does not accept input correctly
**Steps:** 1. Log in. 2. Add a product that works. 3. Open cart, click Checkout. 4. Enter First name "Test", Last name "User", Postal code "12345". 5. Click Continue.
**Expected:** All fields keep their values; user reaches the overview page.
**Actual:** Last name stays empty / input goes to the wrong field, and "Last Name is required" is shown.
**Severity:** Critical. **Priority:** High: users cannot complete an order.
**Evidence:** screenshots/bug-04.png


