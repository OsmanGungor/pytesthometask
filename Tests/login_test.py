import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DemoblazePages.index_page import IndexPage
from DemoblazePages.user_credentials_popup import LoginPopup
from Tests.constants import TIMEOUT, USERNAME, PASSWORD


@pytest.mark.flaky(rerun=2, reruns_delay=2)
def test_login(create_driver, create_user):
    driver = create_driver
    index_page = IndexPage(driver)
    index_page.open_page()
    index_page.click_login()
    login_popup = LoginPopup(driver)
    assert WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located(login_popup.user_name_textbox_locator))
    assert WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located(login_popup.password_textbox_locator))

    login_popup.login(USERNAME, PASSWORD)
    index_page.wait_element_displayed(index_page.welcome_message_locator)
    assert WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located(index_page.welcome_message_locator))
    assert WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located(index_page.logout_locator))

    expected_text = f'Welcome {USERNAME}'
    actual_text = index_page.get_welcome_text()
    assert actual_text == expected_text, 'Welcome message is incorrect.'
