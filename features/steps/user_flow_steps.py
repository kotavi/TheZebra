from time import sleep

from behave import step
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.keys import Keys

from features.pages.questionnaire_page import QuestionnairePage


@step('User is referred to page1 of questionnaire')
def step_impl(context):
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary['currently_insured'])
    assert_equal(QuestionnairePage(context).TITLE, page.title())


@step('User selects "{insured}" for having car insurance as of today')
def step_impl(context, insured):
    page = QuestionnairePage(context)
    if insured == 'Yes':
        page.click_object('currently_insured')
    else:
        page.click_object('currently_not_insured')


@step('User selects "{choice}"')
def step_impl(context, choice):
    page = QuestionnairePage(context)
    if choice == "I need car insurance now":
        page.click_object('need_insurance_now')
    if choice == "I own my home":
        page.click_object('own_home')


@step('User clicks Save button')
def step_impl(context):
    page = QuestionnairePage(context)
    page.click_object('start_save_button')


@step('User clicks Save vehicle button')
def step_impl(context):
    page = QuestionnairePage(context)
    page.find_element(*page.locator_dictionary['vehicle_save_button']).click()


@step('User clicks Save vehicle details button')
def step_impl(context):
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary['vehicle_details_save_button'])
    page.find_element(*page.locator_dictionary['vehicle_details_save_button']).click()


@step('User clicks Save driver details button')
def step_impl(context):
    page = QuestionnairePage(context)
    page.find_element(*page.locator_dictionary['drivers_details_save_button']).click()


@step('User clicks Show my quotes button')
def step_impl(context):
    page = QuestionnairePage(context)
    page.find_element(*page.locator_dictionary['summary_show_quotes_button']).click()


@step('User is referred to page2 of questionnaire')
def step_impl(context):
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary['vehicle_dropdown'])
    assert_true(page.find_element(*page.locator_dictionary['vehicle_dropdown']).is_displayed())


@step('User chooses "{year}" for a vehicle year')
def step_impl(context, year):
    data = {'2020': 'vehicle_2020_year'}
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary[data[year]])
    page.find_element(*page.locator_dictionary['vehicle_dropdown']).send_keys(year)
    page.find_element(*page.locator_dictionary['vehicle_dropdown']).send_keys(Keys.ENTER)


@step('User chooses "{make}" for a vehicle make')
def step_impl(context, make):
    data = {'Cadillac': 'vehicle_cadillac'}
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary[data[make]])
    page.find_element(*page.locator_dictionary[data[make]]).click()


@step('User chooses "{model}" for a vehicle model')
def step_impl(context, model):
    data = {'Xt4': 'vehicle_model'}
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary[data[model]])
    page.find_element(*page.locator_dictionary[data[model]]).click()


@step('User chooses "{trim}" for a vehicle trim')
def step_impl(context, trim):
    data = {'Luxury4drCrossover': 'vehicle_trim'}
    page = QuestionnairePage(context)
    page.find_element(*page.locator_dictionary[data[trim]]).click()


@step('User is referred to page3 of questionnaire')
def step_impl(context):
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary['ownership_div'])
    assert_true(page.find_element(*page.locator_dictionary['ownership_div']).is_displayed())


@step('User chooses "{ownership}" for a type of ownership')
def step_impl(context, ownership):
    data = {'Own - paid in full': 'ownership_paid_full'}
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary['ownership_paid_full'])
    sleep(1)
    page.find_element(*page.locator_dictionary[data[ownership]]).click()


@step('User chooses "{use}" for primary use')
def step_impl(context, use):
    data = {'Personal/Commuting': 'personal'}
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary[data[use]])
    sleep(1)
    page.find_element(*page.locator_dictionary[data[use]]).click()


@step('User enters "{mileage}" for mileage')
def step_impl(context, mileage):
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary['miles_input_field'])
    page.find_element(*page.locator_dictionary['miles_input_field']).send_keys(mileage)


@step('User selects "{frequency}" for frequency')
def step_impl(context, frequency):
    page = QuestionnairePage(context)
    page.find_element(*page.locator_dictionary['frequency_dropdown']).send_keys(frequency)
    page.find_element(*page.locator_dictionary['frequency_dropdown']).send_keys(Keys.ENTER)


@step('User is referred to page4 of questionnaire')
def step_impl(context):
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary['driver_div'])
    assert_true(page.find_element(*page.locator_dictionary['driver_div']).is_displayed())


@step('User enters personal information: "{first_name}", "{last_name}", "{dob}", "{address}"')
def step_impl(context, first_name, last_name, dob, address):
    page = QuestionnairePage(context)
    page.find_element(*page.locator_dictionary['driver_first_name']).click()
    page.find_element(*page.locator_dictionary['driver_first_name']).send_keys(first_name)
    page.find_element(*page.locator_dictionary['driver_last_name']).click()
    page.find_element(*page.locator_dictionary['driver_last_name']).send_keys(last_name)
    page.find_element(*page.locator_dictionary['driver_date_of_birth']).send_keys(dob)
    page.find_element(*page.locator_dictionary['driver_address']).send_keys(address)
    page.find_elements(*page.locator_dictionary['list_of_addresses'])[0].click()


@step('User is referred to page5 of questionnaire')
def step_impl(context):
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary['gender_div'])
    assert_true(page.find_element(*page.locator_dictionary['gender_div']).is_displayed())


@step('User provides information: "{gender}", "{marital_status}", "{score}", "{diploma}", "{violations}", "{email_addr}", "{add_another}"')
def step_impl(context, gender, marital_status, score, diploma, violations, email_addr, add_another):
    data = {"Male": "gender_male", "Female": "gender_female",
            "Single": "marital_status_single", "Married": "marital_status_married",
            "Excellent": "credit_score_excellent",
            "No diploma": "education_no_diploma",
            "No violations": "violations_no",
            "No": "add_another_no"}
    page = QuestionnairePage(context)

    page.wait_for_page_load(page.locator_dictionary[data[gender]])
    page.find_element(*page.locator_dictionary[data[gender]]).click()

    page.wait_for_scroll_to_finish(page.locator_dictionary['marital_status_section'])
    page.wait_for_page_load(page.locator_dictionary['marital_status'])
    page.find_element(*page.locator_dictionary[data[marital_status]]).click()

    page.wait_for_scroll_to_finish(page.locator_dictionary['credit_score_section'])
    page.wait_for_page_load(page.locator_dictionary['credit_score_div'])
    page.find_element(*page.locator_dictionary[data[score]]).click()

    page.wait_for_scroll_to_finish(page.locator_dictionary['education_section'])
    page.wait_for_page_load(page.locator_dictionary['education_div'])
    page.find_element(*page.locator_dictionary[data[diploma]]).click()

    page.wait_for_scroll_to_finish(page.locator_dictionary['violations_section'])
    page.wait_for_scroll_to_finish(page.locator_dictionary['education_section'])

    page.wait_for_page_load(page.locator_dictionary['violations_no'])
    page.find_element(*page.locator_dictionary[data[violations]]).click()

    page.wait_for_scroll_to_finish(page.locator_dictionary['email_section'])
    page.wait_for_page_load(page.locator_dictionary['email_div'])
    page.find_element(*page.locator_dictionary['email_text_field']).send_keys(email_addr)

    page.hover(page.find_element(*page.locator_dictionary[data[add_another]]))
    page.wait_for_page_load(page.locator_dictionary['add_another_driver'])
    page.find_element(*page.locator_dictionary[data[add_another]]).send_keys(add_another)


@step('User is referred to final page of questionnaire')
def step_impl(context):
    page = QuestionnairePage(context)
    page.wait_for_page_load(page.locator_dictionary['quotes_result_h2'])
    assert_true(page.find_element(*page.locator_dictionary['quotes_result_h2']).is_displayed())
