from selenium.webdriver.common.by import By

class HeaderPageLocators:
    LOGO_SCOOTER = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'
    LOGO_YANDEX = By.CLASS_NAME, 'Header_LogoYandex__3TSOI'
    TEXT = By.CLASS_NAME, 'Home_Header__iJKdX'
    BUTTON_FIND = By.XPATH, '//button[text()="Найти"]'
