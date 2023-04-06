from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from tests_data import Valid_Data
from tests_data import Invalid_Data
from locators import RTPanelNaviBar
from locators import RTAutorizationLocators
from locators import RTAutorizationAllerts
from locators import RTRegistrationLocators
import allure

fake_name = Faker().name()
fake_email = Faker().email()
fake_password = Faker().password()

allure.story ('Тесты Авторизации на RT')
class TestValidRegistrationRT:

    def setup(self):
        self.open()

    def open(self):
        self.driver = webdriver.Chrome('/Users/yanavolk66/webdriver/chromedriver_107')
        self.driver.get("https://b2c.passport.rt.ru")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_REGISTER)))


    def close(self):
        self.driver.quit()

    def teardown(self):
        self.close()


# 11
    @allure.feature('Проверка кликабельности выбора типа авторизации')
    def test_clicable_navi_bar(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, RTPanelNaviBar.LOCATOR_NAVI_BAR_LS))).click()
        assert self.driver.find_element(By.XPATH, RTPanelNaviBar.LOCATOR_FORM_LS)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, RTPanelNaviBar.LOCATOR_NAVI_BAR_MAIL))).click()
        assert self.driver.find_element(By.XPATH, RTPanelNaviBar.LOCATOR_FORM_MAIL)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, RTPanelNaviBar.LOCATOR_NAVI_BAR_LOGIN))).click()
        assert self.driver.find_element(By.XPATH, RTPanelNaviBar.LOCATOR_FORM_LOGIN)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, RTPanelNaviBar.LOCATOR_NAVI_BAR_TELEPHONE))).click()
        assert self.driver.find_element(By.XPATH, RTPanelNaviBar.LOCATOR_FORM_TELEPHONE)

# 12
    @allure.feature('Авторизация с не корректным Email')
    def test_autorization_invalid_email(self):
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_USER).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_BUTTON_LOGIN).click()
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_RT_AUTORIZATION_ALLERTS_ERROR)
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_ERROR_TEXT_INVALID_EMAIL)

# 13
    @allure.feature('Авторизация с не корректным номером телефона')
    def test_autorization_invalid_phoneNumber(self):
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_USER).send_keys(
            Invalid_Data.invalid_phoneNumber)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_BUTTON_LOGIN).click()
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_RT_AUTORIZATION_ALLERTS_ERROR)
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_ERROR_TEXT_INVALID_EMAIL)

# 14
    @allure.feature('Авторизация с некорректным паролем')
    def test_autorization_invalid_password(self):
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_USER).send_keys(
            Valid_Data.valid_phoneNumber)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_BUTTON_LOGIN).click()
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_RT_AUTORIZATION_ALLERTS_ERROR)
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_ERROR_TEXT_INVALID_EMAIL)

# 15
    @allure.feature('Авторизация с XSS инъекцией')
    def test_autorization_xss_in_login(self):
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_USER).send_keys(
            Invalid_Data.xss)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_BUTTON_LOGIN).click()
        assert WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, RTAutorizationAllerts.LOCATOR_ERROR_TEXT_XSS)))