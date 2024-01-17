from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//div[contains(@class, "basket-mini")]//span//a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators():
    BTN_ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_PRODUCT_NAME_ADD = (By.XPATH, '//div[@id="messages"]//div[1]//div//strong')
    MESSAGE_PRODUCT_PRICE_ADD = (By.XPATH, '//div[@id="messages"]//div[3]//div//strong')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class, "product_main")]//h1')
    PRODUCT_PRICE = (By.XPATH, '//div[contains(@class, "product_main")]//p')
    MESSAGE_SUCCESS = (By.XPATH, '//div[contains(@class, "alert-success")]')


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_MESSAGE_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')