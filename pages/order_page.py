import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import random

class OrderPage(BasePage):

    @allure.step('Сделат заказ: заполнить данными поля заказа и подтвердить создание заказа')
    def set_form_to_order(self, rent, checkbox, comment):

        # заполнить форму заказа №1
        self.set_text_to_element(OrderPageLocators.NAME, 'Иван')
        self.set_text_to_element(OrderPageLocators.SURNAME, 'Иванов')
        self.set_text_to_element(OrderPageLocators.ADDRESS, 'Москва, ул. Рябкина, д.12')
        self.select_element_from_menu(OrderPageLocators.METRO_STATION_BUTTON,
                                        self.set_number_to_locator(OrderPageLocators.METRO_STATION,
                                                                   random.randint(0, 224)))
        self.set_text_to_element(OrderPageLocators.PHONE, random.randint(00000000000, 99999999999))
        self.click_on_element(OrderPageLocators.BUTTON_TO_NEXT)

        # заполнить форму заказа №2
        self.set_text_to_element(OrderPageLocators.DATE, random.randint(1, 99999))
        self.click_on_element(OrderPageLocators.ACCEPT_DATE)
        self.select_element_from_menu(OrderPageLocators.RENT_TIME, rent)
        self.click_on_element(checkbox)
        self.set_text_to_element(OrderPageLocators.COMMENT, comment)
        self.find_element_with_wait(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

        # подтвердить создание заказа
        self.click_on_element(OrderPageLocators.BUTTON_YES)
