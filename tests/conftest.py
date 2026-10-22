import logging
import pytest
from playwright.sync_api import sync_playwright

import helpers.user as user
import helpers.cart as cart


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)


@pytest.fixture(scope="session")
def pw():
    """Create and provide the Playwright runtime for the whole test session."""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(pw):
    browser = pw.chromium.launch(headless=False)
    yield browser

    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context(
        storage_state=None,  # Start with a clean state
    )
    yield context

    context.close()


@pytest.fixture
def page(context):
    p = context.new_page()
    yield p

    p.close()


@pytest.fixture
def logged_in_user(page):
    """Log in the user before the test and perform cleanup in teardown."""
    user.login_to_user_account(page)
    yield page

    # ======= tear down =======
    cart.empty_cart(page)
    user.logout(page)
