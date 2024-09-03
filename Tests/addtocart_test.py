import pytest
from DemoblazePages.cart_page import CartPage
from DemoblazePages.index_page import IndexPage
from DemoblazePages.monitors_page import MonitorsPage
from DemoblazePages.prod_page import ProdPage
from DemoblazePages.user_credentials_popup import LoginPopup
from Tests.constants import USERNAME, PASSWORD


@pytest.fixture(scope="function")
def user_login(create_driver):
    driver = create_driver
    index_page = IndexPage(driver)
    index_page.open_page()
    index_page.click_login()
    cred_popup = LoginPopup(driver)
    cred_popup.login(USERNAME, PASSWORD)
    yield driver


@pytest.fixture(scope="function")
def clean_cart(user_login):
    driver = user_login
    yield driver
    cart_page = CartPage(driver)
    cart_page.open_page()
    cart_page.empty_cart()


@pytest.mark.flaky(rerun=2, reruns_delay=2)
def test_add_to_cart(clean_cart, create_user):
    driver = clean_cart
    index_page = IndexPage(driver)
    index_page.click_monitors()
    monitors_page = MonitorsPage(driver)
    max_price, max_title = monitors_page.choose_highest_price()
    product_page = ProdPage(driver)
    product_page.add_to_chart()
    cart_page = CartPage(driver)
    cart_page.open_page()
    cart_products = cart_page.get_products()
    assert (max_title, max_price) in cart_products, f'Product {max_title} with price {max_price} is not in cart.'
