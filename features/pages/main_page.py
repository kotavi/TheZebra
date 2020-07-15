from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage
from configs.config import settings


class MainPage(BasePage):

    TITLE = "The Zebra: Instantly Compare Insurance Quotes"

    locator_dictionary = {
        "auto_funnel_selection": (By.XPATH, "//label[@data-cy='auto-funnel-selection']"),
        "homeowners_funnel_selection": (By.XPATH, "//label[@data-cy='homeowners-funnel-selection']"),
        "zip_code_input": (By.XPATH, "//input[@data-cy='zipcode-form-control']"),
        "submit_button": (By.XPATH, "//button[@data-cy='zipcode-submit-button']"),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=settings['url'])

    def click_object(self, name):
        switcher = {
            "auto_selection": self.find_element(*self.locator_dictionary['auto_funnel_selection']),
            "home_selection": self.find_element(*self.locator_dictionary['homeowners_funnel_selection']),
            "submit_button": self.find_element(*self.locator_dictionary['submit_button']),
            "zip_code_input": self.find_element(*self.locator_dictionary['zip_code_input']),
        }
        return switcher[name].click()
