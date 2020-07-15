from behave import step
from nose.tools import assert_equal
from configs.config import settings
from features.pages.main_page import MainPage


@step('User navigates to main page')
def step_impl(context):
    page = MainPage(context)
    page.visit(settings['url'])
    assert_equal(MainPage(context).TITLE, page.title())


@step('User chooses "Car insurance" option')
def step_impl(context):
    page = MainPage(context)
    page.click_object('auto_selection')


@step('User chooses "Home insurance" option')
def step_impl(context):
    page = MainPage(context)
    page.click_object('home_selection')


@step('User clicks on "Zip code" field')
def step_impl(context):
    page = MainPage(context)
    page.click_object('zip_code_input')


@step('User types zip code "{code}"')
def step_impl(context, code):
    page = MainPage(context)
    page.click_object('zip_code_input')
    page.zip_code_input.send_keys(code)


@step('User clicks "Start" button')
def step_impl(context):
    page = MainPage(context)
    page.wait_for_page_load(page.locator_dictionary['submit_button'])
    page.click_object('submit_button')
