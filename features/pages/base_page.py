from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback
import time
from configs.config import settings


def method_missing(what):
    print("No %s here!" % what)


class BasePage(object):

    def __init__(self, browser, base_url=settings['url']):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 10

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def find_elements(self, *loc):
        return self.browser.find_elements(*loc)

    def title(self):
        return self.browser.title

    def visit(self, url):
        self.browser.get(url)

    def hover(self, element):
        ActionChains(self.browser).move_to_element(element).perform()
        time.sleep(5)

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def wait_for_page_load(self, page_object, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(page_object))
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(page_object))
        except Exception as e:
            print(e)

    def wait_for_scroll_to_finish(self, section_name, time_wait=30):
        while time_wait:
            value = self.find_element(*section_name).get_attribute("style")
            if value == "transform: none; opacity: 1;":
                return
            time.sleep(1)
            time_wait -= 1

    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                return self.find_element(*self.locator_dictionary[what])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)
