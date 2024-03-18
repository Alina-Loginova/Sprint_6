from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage

class HeaderPage(OrderPage):
    def make_order(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_UP)
        self.set_form_to_order(OrderPageLocators.RENT_TO_ONE_DAY, OrderPageLocators.BLACK_CHECKBOX, 'сампирк432')
        self.click_on_element(OrderPageLocators.CHECK_ORDER_BUTTON)
