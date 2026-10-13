import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def login_page(page): return LoginPage(page)

@pytest.fixture
def inventory_page(page): return InventoryPage(page)

@pytest.fixture
def checkout_page(page): return CheckoutPage(page)

@pytest.fixture
def logged_in(login_page):
    """Fresh browser context per test, so tests never depend on each other."""
    login_page.open()
    login_page.login("standard_user")
