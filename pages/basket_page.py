import time
import pytest
from .base_page import BasePage
from .locators import BasePageLocators,BasketPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):

	def basket_is_empty(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
			"Basket not empty"

	def basket_message_empty(self):
		assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE_EMPTY), \
			"Message in basket not EMPTY"