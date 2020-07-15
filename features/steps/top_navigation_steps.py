from time import sleep

from behave import step
from nose.tools import assert_equal, assert_true
from features.pages.top_navigation import TopNavigationHeaderPage


@step('Top navigation items are present')
def step_impl(context):
    page = TopNavigationHeaderPage(context)
    assert_true(page.find_element(*page.locator_dictionary['header_brand']).is_displayed())
    assert_true(page.find_element(*page.locator_dictionary['compare_menu']).is_displayed())
    assert_true(page.find_element(*page.locator_dictionary['tools_tips_menu']).is_displayed())
    assert_true(page.find_element(*page.locator_dictionary['company_menu']).is_displayed())
    assert_true(page.find_element(*page.locator_dictionary['help_phone']).is_displayed())


@step('User opens "{menu_name}" menu')
def step_impl(context, menu_name):
    page = TopNavigationHeaderPage(context)
    page.open_menu(menu_name)


@step('User clicks on "{menu_name}" link')
def step_impl(context, menu_name):
    page = TopNavigationHeaderPage(context)
    page.click_menu_item(menu_name)
    # sleep(1)


@step('Page with title "{title}" will be opened')
def step_impl(context, title):
    page = TopNavigationHeaderPage(context)
    assert_equal(title, page.title())


@step('User scrolls down the page')
def step_impl(context):
    page = TopNavigationHeaderPage(context)
    page.scroll_down()


@step('"Get Quotes" button appears')
def step_impl(context):
    page = TopNavigationHeaderPage(context)
    sleep(1)
    assert_true(page.find_element(*page.locator_dictionary['get_quotes']).is_displayed())
