from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_LOCATOR = By.ID, 'accordion__heading-{}'
    DOWN_QUESTION_LOCATOR = By.ID, 'accordion__heading-7'
    ANSWER_LOCATOR = By.ID, 'accordion__panel-{}'
    COOKIE_BUTTON = By.ID, 'rcc-confirm-button'
