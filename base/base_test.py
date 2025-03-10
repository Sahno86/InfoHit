import pytest
from config.data import Data


from pages.favorite_page import FavoritePage
from pages.main_page import MainPage
from pages.user_settings_page import UserSettingsPage

class BaseTest:
    data: Data
    favorite_page: FavoritePage
    main_page: MainPage
    user_settings_page: UserSettingsPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.favorite_page = FavoritePage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.user_settings_page = UserSettingsPage(driver)
