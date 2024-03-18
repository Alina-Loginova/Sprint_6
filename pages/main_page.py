from pages.base_page import BasePage

class MainPage(BasePage):

    def get_url(self, url):
        self.driver.get(url)

    def click_to_question_and_get_answer_text(self, question, answer, num):
        self.click_on_element(self.set_number_to_locator(question, num))
        return self.get_text_from_element(self.set_number_to_locator(answer, num))

    def check_answer(self, result, expected):
        return result == expected
