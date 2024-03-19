import allure
from data import Urls

@allure.story('Тесты: переход на другие страницы')
class TestHeaderPage:

    @allure.title('Тест: переход на главную страницу через кнопку логотипа самоката')
    def test_logo_scooter(self, main_page, header_page):
        main_page.click_cookie()
        header_page.go_to_logo_scooter()
        assert header_page.get_text()

    @allure.title('Тест: переход на страницу Дзена через кнопку логотипа Яндекса')
    def test_logo_yandex(self, header_page, main_page):
        main_page.click_cookie()
        header_page.go_to_yandex_logo()
        header_page.switch_to_dzen()
        assert Urls.DZEN_URL in header_page.get_current_url()
