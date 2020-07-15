from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage
from configs.config import settings


class TopNavigationHeaderPage(BasePage):

    locator_dictionary = {
        "header_brand": (By.XPATH, "//div[@class='header header-black ']"),
        # Menus
        "compare_menu": (By.XPATH, "//a//span[text()='Compare']"),
        "auto_insurance": (By.XPATH, "//ul//li//a[text()='Auto Insurance']"),
        "home_insurance": (By.XPATH, "//ul//li//a[text()='Home Insurance']"),

        "company_menu": (By.XPATH, "//a//span[text()='Company']"),

        "tools_tips_menu": (By.XPATH, "//a//span[text()='Tools & Tips']"),

        "help_phone": (By.XPATH, "//a//span[@class='cta-phone-display']"),
        "get_quotes": (By.XPATH, "//div//a[text()='Get Quotes']"),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=settings['url'])

    def open_menu(self, name):
        switcher = {
            "Compare": self.find_element(*self.locator_dictionary['compare_menu']),
            "Tools & Tips": self.find_element(*self.locator_dictionary['tools_tips_menu']),
            "Company": self.find_element(*self.locator_dictionary['company_menu']),
        }
        return switcher[name].click()

    def click_menu_item(self, name):
        switcher = {
            "Auto Insurance": self.find_element(*self.locator_dictionary['auto_insurance']),
            "Home Insurance": self.find_element(*self.locator_dictionary['home_insurance']),
        }
        return switcher[name].click()