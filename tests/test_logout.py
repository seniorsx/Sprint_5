from locators.locators import MainPageLocators, AuthPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import user_data
from data import urls

class TestUserLogout:

    def test_user_logout(self, driver):
        driver.get(urls.app)
        driver.find_element(*MainPageLocators.SIGN_IN_BTN).click()

        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(user_data.user_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(user_data.password)
        driver.find_element(*AuthPageLocators.LOGIN_BTN).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.USERNAME_TEXT)
        )


        driver.find_element(*MainPageLocators.LOGOUT_BTN).click()
        sign_in_btn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.SIGN_IN_BTN)
        )
        assert sign_in_btn.is_displayed()
