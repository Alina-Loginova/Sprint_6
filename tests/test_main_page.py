import pytest
from locators.main_page_locators import MainPageLocators
from data import Answers, Urls

class TestMainPage:

    @pytest.mark.parametrize(
        "q_num,expected_result",
        [
            (0, Answers.ANSWER_Q_0),
            (1, Answers.ANSWER_Q_1),
            (2, Answers.ANSWER_Q_2),
            (3, Answers.ANSWER_Q_3),
            (4, Answers.ANSWER_Q_4),
            (5, Answers.ANSWER_Q_5),
            (6, Answers.ANSWER_Q_6),
            (7, Answers.ANSWER_Q_7)
        ]
    )
    def test_questions(self, main_page, q_num, expected_result):

        # открыли стартовую страницу
        main_page.get_url(Urls.MAIN_URL)

        # нажали на кнопку куки
        main_page.click_on_element(MainPageLocators.COOKIE_BUTTON)

        # проскролили страницу вниз до последнего вопроса
        main_page.scroll_page(MainPageLocators.DOWN_QUESTION_LOCATOR)

        result = main_page.click_to_question_and_get_answer_text(
            MainPageLocators.QUESTION_LOCATOR,
            MainPageLocators.ANSWER_LOCATOR,
            q_num
        )

        assert main_page.check_answer(result, expected_result)
