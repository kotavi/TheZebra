import os
from selenium import webdriver
from datetime import datetime
from configs.config import settings


def before_all(context):
    print("\n[%s] Started feature test run..." % datetime.now())


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    if str(settings['browser']).lower() == "firefox":
        context.browser = webdriver.Firefox()
    elif str(settings['browser']).lower() == "chrome":
        context.browser = webdriver.Chrome()
    elif str(settings['browser']).lower() == "safari":
        context.browser = webdriver.Safari()
    else:
        context.browser = webdriver.Firefox()
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()


def after_scenario(context, scenario):
    print("\nFinished scenario '%s'" % scenario.name)
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.mkdir("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")
    os.chdir("../")
    context.browser.quit()


def after_feature(context, feature):
    pass


def after_all(context):
    print("\n[%s] Finished feature test run..." % datetime.now())