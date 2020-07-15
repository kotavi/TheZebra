from behave import step
from nose.tools import assert_equal
from features.pages.auto_insurance_page import AutoInsurancePage


@step('"Auto Insurance" page with correct title will be opened')
def step_impl(context):
    page = AutoInsurancePage(context)
    page.wait_for_page_load(page.locator_dictionary['insurances_list'])
    assert_equal(AutoInsurancePage(context).TITLE, page.title())

