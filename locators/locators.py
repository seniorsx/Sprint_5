from selenium.webdriver.common.by import By

class MainPageLocators:
    SIGN_IN_BTN = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    PLACE_AD_BTN = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    USERNAME_TEXT = (By.XPATH, "//h3[contains(text(), 'User.')]")
    LOGOUT_BTN = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    NEED_AUTH_TEXT = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
    MY_ADS_TITLE = (By.XPATH, "//h2[contains(text(), 'Тестовое объявление')]")
    SEARCH_INPUT = (By.NAME, "name")
    SEARCH_BTN = (By.XPATH, "//button[contains(text(), 'Применить')]")

class RegistrationPageLocators:
    NO_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    REPEAT_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    ERROR_MESSAGE = (By.XPATH, "//span[contains(text(), 'Ошибка')]")

class AuthPageLocators:
    SIGN_IN_BTN = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(), 'Войти')]")

class AdPageLocators:
    AD_NAME_INPUT = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")
    PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.NAME, "category")
    TECHNO_CATEGORY = (By.XPATH, "//span[contains(text(), 'Технологии')]")
    CITY_DROPDOWN = (By.NAME, "city")
    PETER_CITY = (By.XPATH, "//span[contains(text(), 'Санкт-Петербург')]")
    PUBLISH_BTN = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    MODAL_TITLE = (By.XPATH, "//div[contains(text(), 'To place an ad, log in')]")
