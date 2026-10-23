import pytest

from tests.config import config
import helpers.cart as cart
import helpers.user as user


def test_add_product_to_cart(context, logged_in_user):
    """
    Test to verify that a product remains in the cart after re-authentication.
    It also ensures the cart is refreshed with a clean browser context for the
    second login to avoid cached authentication data.

    Args:
        context: The browser context used by the test.
        logged_in_user: The authenticated page fixture.
    """
    page = logged_in_user

    cart.select_product_and_add_to_cart(page, config.product_name)
    cart.open_cart_and_verify_product(page, config.product_name)

    user.logout(page)
    context.clear_cookies()

    user.login_to_user_account(page)
    cart.open_cart_and_verify_product(page, config.product_name)
