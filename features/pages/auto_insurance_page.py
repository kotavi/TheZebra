from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage
from configs.config import settings


class AutoInsurancePage(BasePage):

    TITLE = "Compare 2020 Car Insurance Rates Side-by-Side | The Zebra"

    locator_dictionary = {
        "insurances_list": (By.XPATH, "//div[@class='hidden-md-down hero-animation-container']")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=settings['url'])
