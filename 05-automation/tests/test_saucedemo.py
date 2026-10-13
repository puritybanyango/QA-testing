from playwright.sync_api import expect

def test_standard_user_can_log_in(login_page, inventory_page):
    login_page.open()
    login_page.login("standard_user")
    expect(inventory_page.title).to_have_text("Products")
    expect(inventory_page.items).to_have_count(6)

def test_locked_out_user_sees_error(login_page, page):
    login_page.open()
    login_page.login("locked_out_user")
    expect(login_page.error).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    expect(page).to_have_url("https://www.saucedemo.com/")

def test_add_two_products_updates_cart_badge(logged_in, inventory_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    expect(inventory_page.cart_badge).to_have_text("2")

def test_checkout_shows_order_confirmation(logged_in, inventory_page, checkout_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    checkout_page.checkout_button.click()
    checkout_page.fill_details()
    checkout_page.finish_button.click()
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")
