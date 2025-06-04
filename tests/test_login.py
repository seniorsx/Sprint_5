from data import user_data
from data import urls
from locators.locators import MainPageLocators, AuthPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserLogin:

    def test_user_login(self, driver):
        driver.get(urls.app)
        driver.find_element(*MainPageLocators.SIGN_IN_BTN).click()

        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(user_data.user_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(user_data.password)
        driver.find_element(*AuthPageLocators.LOGIN_BTN).click()

        username = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.USERNAME_TEXT)
        )
        assert "User" in username.text
