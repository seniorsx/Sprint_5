from locators.locators import MainPageLocators, AuthPageLocators, AdPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import user_data

def test_create_ad_unauthorized(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru")
    driver.find_element(*MainPageLocators.PLACE_AD_BTN).click()

    modal_title = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPageLocators.NEED_AUTH_TEXT)
    )
    assert modal_title.text == "Чтобы разместить объявление, авторизуйтесь"

def test_create_ad_authorized(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru")

    driver.find_element(*MainPageLocators.SIGN_IN_BTN).click()
    driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(user_data.user_email)
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(user_data.password)
    driver.find_element(*AuthPageLocators.LOGIN_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPageLocators.USERNAME_TEXT)
    )

    driver.find_element(*MainPageLocators.PLACE_AD_BTN).click()
    driver.find_element(*AdPageLocators.AD_NAME_INPUT).send_keys("Тестовое объявление")
    driver.find_element(*AdPageLocators.DESCRIPTION_INPUT).send_keys("Описание товара")
    driver.find_element(*AdPageLocators.PRICE_INPUT).send_keys("1234")
    driver.find_element(*AdPageLocators.PUBLISH_BTN).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPageLocators.USERNAME_TEXT)
    ).click()

    driver.find_element(*MainPageLocators.SEARCH_INPUT).send_keys("Тестовое объявление")
    driver.find_element(*MainPageLocators.SEARCH_BTN).click()

    ad_title = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPageLocators.MY_ADS_TITLE)
    )
    assert "Тестовое объявление" in ad_title.text