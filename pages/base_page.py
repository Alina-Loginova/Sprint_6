from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(
            self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

# добавить скрол в base_page
    def scroll_page(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def set_number_to_locator(self, locator_num, num):
        method, locator = locator_num
        locator = locator.format(num)
        return method, locator

    def select_element_from_menu(self, locator_menu, locator_item):
        self.click_on_element(locator_menu)
        self.scroll_page(locator_item)
        self.click_on_element(locator_item)

    def tab_switch(self, locator, time=10):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url
