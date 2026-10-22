import os
from tests.config import config
from playwright.sync_api import TimeoutError


def login_to_user_account(page):
    """
    Authenticate the user on the login page.

    This function fills the username and password from environment variables,
    submits the login form, waits for user input for MFA approval in the app,
    and accepts the trust-device prompt if it appears.

    Args:
        page: The Playwright page object for the login flow.

    Notes:
        If the trust-device prompt does not appear, the function continues without error.
    """
    page.goto(config.login_url)
    page.fill("input[id='user']", os.getenv("APP_USER"))
    page.click("button[data-testid='login-new-user-submit']")
    page.fill("input[id='login-password']", os.getenv("APP_PASSWORD"))
    page.click("button[data-testid='login-button']")

    input("Press Enter after approving the authentication request in the app...")

    try:
        trust_device_button = page.locator("button:has-text('Trust Device')")
        trust_device_button.wait_for(state='visible', timeout=5000)
        trust_device_button.click()
    except TimeoutError:
        pass


def logout(page):
    """
    Log the current user out of the application.

    Args:
        page: The Playwright page object for the authenticated session.
    """
    page.reload()
    page.goto(config.base_url)
    page.locator("button[data-uic-component*='Account.Trigger']").click()
    page.locator("span:has-text('Sign Out')").click()
