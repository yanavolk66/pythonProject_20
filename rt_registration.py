from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
from tests_data import Valid_Data
from tests_data import Invalid_Data
from locators import RTRegistrationLocators
from locators import RTRegistrationsAllerts
import allure

fake_name = Faker().name()
fake_email = Faker().email()
fake_password = Faker().password()


@allure.story('Тесты Регистрации на RT')
class TestValidRegistrationRT:

    def setup(self):
        self.open()

    def open(self):
        self.driver = webdriver.Chrome('/Users/yanavolk66/webdriver/chromedriver_107')
        self.driver.get("https://b2c.passport.rt.ru")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_REGISTER)))
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_REGISTER).click()

    def close(self):
        self.driver.quit()

    def teardown(self):
        self.close()

    # eto_baza
    def test_eto_baza(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_ENTER_CODE)

    # 1
    @allure.feature('Регистрация с паролем из 21 символа')
    def test_registration_user_with_pass_21char(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.password_21_char)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.password_21_char)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

    # 2
    @allure.feature('Регистрация с Email без домена')
    def test_registration_user_with_email_without_domain(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.email_without_domain)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

    # 3
    @allure.feature('Регистрация с именем из 31 символа')
    def test_registration_user_with_firstname_31char(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Invalid_Data.first_name_31_char)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

    # 4
    @allure.feature('Регистрация с именем из 1 символа')
    def test_registration_user_with_firstname_1char(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Invalid_Data.first_name_1_char)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

    # 5
    @allure.feature('Регистрация с незаполненным обязательным полем Email или Телефон')
    def test_registration_user_with_not_filled_email_or_mobile(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

    # 6
    @allure.feature('Регистрация с незаполненным обязательным полем Фамилия')
    def test_registration_user_with_not_filled_lastname(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

    # 7
    @allure.feature('Регистрация с незаполненным обязательным полем Имя')
    def test_registration_user_with_not_filled_firstname(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

    # 8
    @allure.feature('Регистрация с несовпадающими паролями')
    def test_registration_user_with_non_matching_passwords(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Valid_Data.valid_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

    # 9
    @allure.feature('Регистрация с паролем не содержащем цифру')
    def test_registration_user_with_password_not_contain_digit(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.password_not_contain_digit)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.password_not_contain_digit)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

    # 10
    @allure.feature('Регистрация с фамилией из 31 символа')
    def test_registration_user_with_lastname_31char(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Invalid_Data.last_name_31_char)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)
