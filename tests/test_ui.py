from tests.config import config
import helpers.cart as cart
import helpers.user as user


def test_add_product_to_cart(context, logged_in_user):
    page = logged_in_user

    cart.select_product_and_add_to_cart(page, config.product_name)
    cart.open_cart_and_verify_product(page, config.product_name)

    user.logout(page)
    context.clear_cookies()

    user.login_to_user_account(page)
    cart.open_cart_and_verify_product(page, config.product_name)
