import allure

from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage

class HeaderPage(BasePage):

    @allure.step('Нажать на логотип Яндекса')
    def go_to_yandex_logo(self):
        self.click_on_element(HeaderPageLocators.LOGO_YANDEX)

    @allure.step('Дождаться на другой странице логотип Дзена')
    def switch_to_dzen(self):
        self.tab_switch(HeaderPageLocators.BUTTON_FIND)

    @allure.step('Нажать на логотип Самоката')
    def go_to_logo_scooter(self):
        self.click_on_element(HeaderPageLocators.LOGO_SCOOTER)

    @allure.step('Получить текст на главной странице')
    def get_text(self):
        text = self.get_text_from_element(HeaderPageLocators.TEXT)
        return text
