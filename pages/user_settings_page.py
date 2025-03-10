import allure
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from config.links import Links


class UserSettingsPage(BasePage):
    PAGE_URL = Links.USER_SETTINGS

    PHONE_FIELD = ("xpath", "//input[@name='PERSONAL_PHONE']")
    SAVE_BUTTON = ("xpath", "//input[@name='save']")
    
    @allure.step("Enter phone")
    def enter_phone(self, PHONE):
        enter_phone_field = self.wait.until(EC.element_to_be_clickable(self.PHONE_FIELD))
        enter_phone_field.clear()
        enter_phone_field.send_keys(PHONE)
    
    @allure.step("Click save button")
    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Check phone change")
    def is_phone_changes(self, PHONE):
        self.wait.until(EC.text_to_be_present_in_element_value(self.PHONE_FIELD, PHONE))