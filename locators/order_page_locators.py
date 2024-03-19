from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = By.XPATH, '//input[@placeholder="* Имя"]'
    SURNAME = By.XPATH, '//input[@placeholder="* Фамилия"]'
    ADDRESS = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_STATION_BUTTON = By.XPATH, '//div[@class="select-search__value"]'
    METRO_STATION = By.XPATH, '//div[@class="select-search__select"]/ul/li[@data-index="{}"]'
    PHONE = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    BUTTON_TO_NEXT = By.XPATH, '//button[text()="Далее"]'

    DATE = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    ACCEPT_DATE = By.XPATH, '//div[@class="Order_Header__BZXOb" and text()="Про аренду"]'
    RENT_TIME = By.XPATH, '//div[@class="Dropdown-root"]'
    RENT_TO_ONE_DAY = By.XPATH, '//div[@class="Dropdown-option" and text()="сутки"]'
    RENT_TO_TWO_DAYS = By.XPATH, '//div[@class="Dropdown-option" and text()="двое суток"]'
    BLACK_CHECKBOX = By.XPATH, '//input[@id="black"]'
    GREY_CHECKBOX = By.XPATH, '//input[@id="grey"]'
    COMMENT = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    ORDER_BUTTON = By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]'

    BUTTON_YES = By.XPATH, '//button[text()="Да"]'
    CHECK_ORDER_BUTTON = By.XPATH, '//button[text()="Посмотреть статус"]'

    ORDER_BUTTON_UP = By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]'
    ORDER_BUTTON_DOWN = By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]'
