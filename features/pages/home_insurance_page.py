from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage
from configs.config import settings


class HomeInsurancePage(BasePage):

    TITLE = "Compare Home Insurance Rates Online (Updated 2020) | The Zebra"

    locator_dictionary = {
        "header_h1": (By.XPATH, "//h1[@class='jumbotron-h1']")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=settings['url'])
