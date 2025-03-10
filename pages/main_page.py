import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    PAGE_URL = Links.MAIN

    LOGIN_BUTTON = ("xpath", "//div[@class='header__nav__menu-actions__item h-100%']")
    EMAIL_FIELD = ("xpath", "//input[@name='user_auth_email']")
    PASSWORD_FIELD = ("xpath", "//input[@name='user_auth_password']")
    ENTER_BUTTON = ("xpath", "//input[@name='user_auth']")


    @allure.step("click on login link")
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
    
    @allure.step("Enter e-mail")
    def enter_email(self, EMAIL):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(EMAIL)

    @allure.step("Enter password")
    def enter_password(self, PASSWORD):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(PASSWORD)

    @allure.step("Click enter button")
    def click_enter_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_BUTTON)).click()
