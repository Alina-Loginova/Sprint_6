from data import Urls
from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators

class TestHeaderPage:
    def test_logo_scooter(self, main_page, header_page):
        main_page.click_on_element(MainPageLocators.COOKIE_BUTTON)
        header_page.make_order()
        header_page.click_on_element(HeaderPageLocators.LOGO_SCOOTER)
        assert header_page.get_text_from_element(HeaderPageLocators.TEXT)

    def test_logo_yandex(self, main_page, header_page):
        main_page.click_on_element(MainPageLocators.COOKIE_BUTTON)
        header_page.make_order()
        header_page.click_on_element(HeaderPageLocators.LOGO_YANDEX)
        header_page.tab_switch(HeaderPageLocators.SEARCH_INPUT)
        assert Urls.DZEN_URL in header_page.get_current_url()

