from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from configs.config import settings


class QuestionnairePage(BasePage):

    TITLE = "Compare Car Insurance Rates: Fast, Free, Simple | The Zebra"

    locator_dictionary = {
        # currently_insured
        "currently_insured": (By.XPATH, "//span[text()='Yes']"),
        "currently_not_insured": (By.XPATH, "//span[text()='No']"),

        # residence_ownership
        "own_home": (By.XPATH, "//span[text()='I own my home']"),
        "own_condo": (By.XPATH, "//span[text()='I own my condo']"),
        "rent": (By.XPATH, "//span[text()='I rent']"),
        "other": (By.XPATH, "//span[text()='Other']"),

        # user_intent
        "need_insurance_now": (By.XPATH, "//span[text()='I need car insurance now']"),

        # vehicleInfo
        "vehicle_dropdown": (By.XPATH, "//input[@id='yearYear-0Input-0']"),
        "vehicle_2020_year": (By.XPATH, "//div[@id='year-0-2020-0']"),
        "vehicle_cadillac": (By.XPATH, "//div[@id='make-0-Cadillac-0']"),
        "vehicle_model": (By.XPATH, "//div[@id='model-0-Xt4-0']"),
        "vehicle_trim": (By.XPATH, "//div[@id='submodel-0-4x4Luxury4drCrossover-0']"),

        # ownership
        "ownership_div": (By.XPATH, "//div[@id='ownership-0']"),
        "ownership_paid_full": (By.XPATH, "//span[text()='Own - paid in full']"),

        # primary_use
        "personal": (By.XPATH, "//span[text()='Personal/Commuting']"),

        # annual_mileage
        "miles_input_field": (By.XPATH, "//input[@id='miles-input-0']"),
        "frequency_dropdown": (By.XPATH, "//input[@id='mileage_periodMileage_periodInput-0']"),
        "frequency_per_year": (By.XPATH, "//div[@id='mileage_period-PerYear-0']"),

        # personal information
        "driver_div": (By.XPATH, "//div[@id='driverPII-0']"),
        "driver_first_name": (By.XPATH, "//input[@id='first_name-0']"),
        "driver_last_name": (By.XPATH, "//input[@id='last_name-0']"),
        "driver_date_of_birth": (By.XPATH, "//input[@id='date_of_birth-0']"),
        "driver_address": (By.XPATH, "//input[@id='garaging_addressInput']"),
        "list_of_addresses": (By.XPATH, "//div[@class='pac-item fs-block']"),

        # gender
        "gender_div": (By.XPATH, "//div[@id='gender-0']"),
        "gender_male": (By.XPATH, "//span[text()='Male']"),
        # "gender_male": (By.XPATH, "//input[@id='gender-0-0']"),
        "gender_female": (By.XPATH, "//input[@id='gender-1-0']"),

        # marital_status
        "marital_status_section": (By.XPATH, "//div[@class='section-page-question item-0 marital_status']"),
        "marital_status": (By.XPATH, "//div[@id='marital_status-0']"),
        "marital_status_single": (By.XPATH, "//span[text()='Single']"),
        "marital_status_married": (By.XPATH, "//span[text()='Married']"),

        # credit_score
        "credit_score_section": (By.XPATH, "//div[@class='section-page-question item-0 credit_score']"),
        "credit_score_div": (By.XPATH, "//div[@id='credit_score-0']"),
        "credit_score_excellent": (By.XPATH, "//span[text()='Excellent (720+)']"),

        # education
        "education_section": (By.XPATH, "//div[@class='section-page-question item-0 education']"),
        "education_div": (By.XPATH, "//div[@id='education-0']"),
        "education_no_diploma": (By.XPATH, "//span[text()='No diploma']"),

        # violations
        "violations_section": (By.XPATH, "//div[@class='section-page-question item-0 violations']"),
        "violations_div": (By.XPATH, "//div[@id='violations-0']"),
        "violations_no": (By.XPATH, "//label[@for='violations-0-0']//span[text()='No']"),
        # "violations_no": (By.XPATH, "//input[@id='violations-0-0']"),

        # email
        "email_section": (By.XPATH, "//div[@class='section-page-question item-0 email']"),
        "email_div": (By.XPATH, "//div[@id='email-0']"),
        "email_text_field": (By.XPATH, "//input[@id='email-0']"),

        # applicable discount  -->  skipped

        # add another driver
        "add_another_driver": (By.XPATH, "//div[@id='add_another-0']"),
        "add_another_no": (By.XPATH, "//input[@id='add_another-0-0']"),

        # page with quotes
        "quotes_result_h2": (By.XPATH, "//h2[text()='Choose the quote that’s best for you!']"),

        # buttons
        "start_save_button": (By.XPATH, "//button[@id='startSaveBtn']"),
        "vehicle_save_button": (By.XPATH, "//button[@id='vehiclesSelectSaveBtn']"),
        "vehicle_details_save_button": (By.XPATH, "//button[@id='vehiclesDetailsSaveBtn']"),
        "drivers_details_save_button": (By.XPATH, "//button[@id='driversSelectSaveBtn']"),
        "summary_show_quotes_button": (By.XPATH, "//button[@id='summaryShowQuotesBtn']"),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=settings['url'])

    def click_object(self, name):
        switcher = {
            "currently_insured": self.find_element(*self.locator_dictionary['currently_insured']),
            "currently_not_insured": self.find_element(*self.locator_dictionary['currently_not_insured']),
            "own_home": self.find_element(*self.locator_dictionary['own_home']),
            "start_save_button": self.find_element(*self.locator_dictionary['start_save_button']),
            "need_insurance_now": self.find_element(*self.locator_dictionary['need_insurance_now']),
        }
        return switcher[name].click()
