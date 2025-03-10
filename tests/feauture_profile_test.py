import allure
import random
import pytest
from base.base_test import BaseTest

@allure.feature("Profile funtionality")
class TestProfileFeauture(BaseTest):

    @allure.title("Change phone")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_phone(self):
        self.main_page.open()
        self.main_page.click_login_button()
        self.main_page.enter_email(self.data.EMAIL)
        self.main_page.enter_password(self.data.PASSWORD)
        self.main_page.click_enter_button()
        self.user_settings_page.open()
        self.user_settings_page.is_opened()
        self.user_settings_page.enter_phone(f"{self.data.PHONE}{random.randint(1000, 9999)}")
        self.user_settings_page.click_save_button()
        # self.user_settings_page.is_phone_changes()
