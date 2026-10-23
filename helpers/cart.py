from tests.config import config
from playwright.sync_api import TimeoutError, expect


def select_product_and_add_to_cart(page, product_name):
    """
    Open the product page and add the selected product to the cart.

    Args:
        page: The Playwright page object.
        product_name: The exact product title to locate and add.

    Raises:
        TimeoutError: If the product or Add to Cart button never becomes visible.
    """
    page.goto(config.product_url)

    handle_cookie_consent(page)

    product = page.locator(f"text={product_name}")
    product.wait_for(state='visible', timeout=10000)
    page.locator(
        f"xpath=//div[contains(text(), '{product_name}')]/ancestor::a//button[normalize-space()='Add to Cart']"
    ).click()
    page.locator("div[id='cart-summary']").wait_for(state='visible', timeout=5000)


def handle_cookie_consent(page):
    """
    Handles the cookie consent banner if it appears.

    Args:
        page: The Playwright page object.

    Notes:
        If the banner is not present, the function exits quietly.
    """
    try:
        # Wait for the cookie consent banner to appear
        page.locator("#onetrust-banner-sdk").wait_for(state='visible', timeout=5000)
        page.click("button:has-text('Accept All Cookies')")
    except TimeoutError:
        # If the banner does not appear, do nothing
        pass


def open_cart_and_verify_product(page, product_name):
    """
    Opens the cart and verifies that the specified product is present.

    Args:
        page: The Playwright page object.
        product_name (str): The name of the product to verify in the cart.
    
    Raises:
        AssertionError: If the product is missing or quantity is not 1.
    """
    page.goto(config.cart_url)
    page.locator("xpath=//form[contains(@id, 'ac-form--cart')]").wait_for(state="visible", timeout=10000)

    # Get the product in the cart
    product = page.locator(f"xpath=//form[@id='ac-form--cart']//div[@title='{product_name}']")
    expect(product).to_be_visible(timeout=5000)

    # Get the product quantity
    product_quantity = page.inner_text(
        "xpath=//div[contains(text(), 'Order Details')]/following-sibling::div"
    )

    quantity_value = product_quantity.strip()
    quantity_number = quantity_value.split()[0]  # "1" from "1 item"

    assert quantity_number == "1", (
        f"Expected quantity to be 1, but got '{product_quantity}'"
    )


def empty_cart(page):
    """
    Empties the cart by removing all products.

    Args:
        page: The Playwright page object.
    """
    page.reload()
    page.goto(config.cart_url)
    page.locator("xpath=//img[contains(@alt, 'Remove icon')]").wait_for(state="visible", timeout=10000)

    # Get all "Remove" buttons in the cart
    remove_buttons = page.locator("xpath=//img[contains(@alt, 'Remove icon')]")
    count = remove_buttons.count()
    for i in range(count):
        remove_buttons.nth(i).click()
