import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Открыть страницу (урл)')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Убрать окно про куки')
    def click_cookie(self):
        return self.click_on_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Прокрутить до списка "Вопросы о важном"')
    def scroll(self):
        self.scroll_page(MainPageLocators.DOWN_QUESTION_LOCATOR)

    @allure.step('Кликнуть на вопрос из списка и просмотреть ответ')
    def click_to_question_and_get_answer_text(self, question, answer, num):
        self.click_on_element(self.set_number_to_locator(question, num))
        return self.get_text_from_element(self.set_number_to_locator(answer, num))

    @allure.step('Проверить, что ответ корректный')
    def check_answer(self, result, expected):
        return result == expected

    @allure.step('"Посмотреть статус"')
    def check_order_button(self):
        return self.find_element_with_wait(OrderPageLocators.CHECK_ORDER_BUTTON)
