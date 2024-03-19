import allure
import pytest
from locators.order_page_locators import OrderPageLocators

@allure.story('Тест: заказ самоката')
class TestOrderPage:

    @allure.title('Тест: корректный заказ самоката через кнопку "Заказать"')
    @pytest.mark.parametrize("button, rent, checkbox, comment",
                             [(OrderPageLocators.ORDER_BUTTON_UP,
                               OrderPageLocators.RENT_TO_ONE_DAY,
                               OrderPageLocators.BLACK_CHECKBOX,
                               'сампирк432'),
                              (OrderPageLocators.ORDER_BUTTON_DOWN,
                               OrderPageLocators.RENT_TO_TWO_DAYS,
                               OrderPageLocators.GREY_CHECKBOX,
                               'ABCD123')
                              ])
    def test_to_order(self, main_page, order_page, button, rent, checkbox, comment):
        main_page.click_cookie()
        order_page.scroll_page(button)
        order_page.click_on_element(button)
        order_page.set_form_to_order(rent, checkbox, comment)
        assert main_page.check_order_button()
