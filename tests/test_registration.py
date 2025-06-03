from locators.locators import MainPageLocators, RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data import user_data

def test_successful_registration(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru")
    driver.find_element(*MainPageLocators.SIGN_IN_BTN).click()
    driver.find_element(*RegistrationPageLocators.NO_ACCOUNT_BTN).click()

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(user_data.email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(user_data.password)
    driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_INPUT).send_keys(user_data.password)
    driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BTN).click()

    avatar = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPageLocators.USERNAME_TEXT)
    )
    assert driver.find_element(*MainPageLocators.PLACE_AD_BTN)

def test_registration_invalid_email(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru")
    driver.find_element(*MainPageLocators.SIGN_IN_BTN).click()
    driver.find_element(*RegistrationPageLocators.NO_ACCOUNT_BTN).click()

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("invalidemail")
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("AnyPass123")
    driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_INPUT).send_keys("AnyPass123")
    driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BTN).click()

    error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
    )

    email_class = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).find_element(By.XPATH, "..").get_attribute("class")
    password_class = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).find_element(By.XPATH, "..").get_attribute("class")
    repeat_password_class = driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_INPUT).find_element(By.XPATH, "..").get_attribute("class")
    email_error_text = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE).text

    assert "Error" in email_class
    assert "Error" in password_class
    assert "Error" in repeat_password_class
    assert email_error_text == "Ошибка"

def test_registration_existing_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru")
    driver.find_element(*MainPageLocators.SIGN_IN_BTN).click()
    driver.find_element(*RegistrationPageLocators.NO_ACCOUNT_BTN).click()

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(user_data.email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(user_data.password)
    driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_INPUT).send_keys(user_data.password)
    driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BTN).click()

    error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
    )

    email_class = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).find_element(By.XPATH, "..").get_attribute("class")
    password_class = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).find_element(By.XPATH, "..").get_attribute("class")
    repeat_password_class = driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_INPUT).find_element(By.XPATH, "..").get_attribute("class")
    email_error_text = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE).text

    assert "Error" in email_class
    assert "Error" in password_class
    assert "Error" in repeat_password_class
    assert email_error_text == "Ошибка"
