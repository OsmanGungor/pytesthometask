from selenium.webdriver.common.by import By
import re
from DemoblazePages.base_page import BasePage


class MonitorsPage(BasePage):
    def __init__(self, driver):
        super().__init__('#', driver)
        self.prices_locator = (By.XPATH, "//h4[@class='card-title']/following-sibling::h5")

    def choose_highest_price(self):
        super().wait_page_url()
        super().wait_page_ready()

        price_elements = self.driver.find_elements(*self.prices_locator)
        price_texts = [float(re.sub(r'[^\d.]', '', price.text)) for price in price_elements]
        if not price_texts:
            raise Exception("No prices found.")
        max_price = max(price_texts)
        max_price_index = price_texts.index(max(price_texts))
        max_price_element = price_elements[max_price_index]
        title_element = max_price_element.find_element(By.XPATH, "./preceding-sibling::h4/a")
        max_title = title_element.text
        super().click_element(title_element)
        return max_price, max_title
