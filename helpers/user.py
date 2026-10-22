import os
from config import config
from playwright.sync_api import TimeoutError


def login_to_user_account(page):
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
    page.reload()
    page.goto(config.base_url)
    page.locator("button[data-uic-component*='Account.Trigger']").click()
    page.locator("span:has-text('Sign Out')").click()
    page.screenshot(path="screenshots/after_logout.png")
