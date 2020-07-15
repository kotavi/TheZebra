from behave import step
from nose.tools import assert_equal
from features.pages.home_insurance_page import HomeInsurancePage


@step('"Home Insurance" page with correct title will be opened')
def step_impl(context):
    page = HomeInsurancePage(context)
    page.wait_for_page_load(page.locator_dictionary['header_h1'])
    assert_equal(HomeInsurancePage(context).TITLE, page.title())

