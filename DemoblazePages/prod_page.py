from selenium.webdriver.common.by import By
from DemoblazePages.base_page import BasePage


class ProdPage(BasePage):
    def __init__(self, driver):
        super().__init__('prod.html', driver)
        self.add_to_cart_button_locator = (By.XPATH, "//*[contains(@onclick,'addToCart')]")

    def add_to_chart(self):
        super().wait_page_url()
        super().wait_page_ready()
        super().scroll_and_click(self.add_to_cart_button_locator)


