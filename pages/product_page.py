import time
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def push_btn_to_basket(self):
        btn_add_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_BASKET)
        btn_add_basket.click()
        #self.solve_quiz_and_get_code()
        #self.check_name_product()
        #self.check_price_product()
        #self.should_not_be_success_message()
        #self.disappeared_success_message()
        #time.sleep(120)




    def should_be_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_BASKET), "Button basket is not presented"

    def check_name_product(self):
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME_ADD)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert message_product_name.text == product_name.text, "The product name in the shopping cart does not match the name in the card"

    def check_price_product(self):
        message_product_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE_ADD)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert message_product_price.text == product_price.text, "The product price in the shopping cart does not match the price in the card"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS), \
            "Success message is presented, but should not be"

    def disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_SUCCESS), \
            "The message is displayed, but should be disappeared"