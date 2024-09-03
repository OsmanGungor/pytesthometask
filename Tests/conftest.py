import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from DemoblazePages.index_page import IndexPage
from DemoblazePages.user_credentials_popup import SignUpPopup


@pytest.fixture(scope="function")
def create_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def create_user():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    index_page = IndexPage(driver)
    index_page.open_page()
    index_page.click_signup()
    signup_popup = SignUpPopup(driver)
    signup_popup.signup('Admin', 'Admin')
    index_page.open_page()
    driver.quit()

