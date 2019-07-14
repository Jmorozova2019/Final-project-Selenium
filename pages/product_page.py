from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def click_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def read_product_name(self):
        #Запомнить название продукта
        self.PRODUCT_NAME = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ELEM).text

    def read_product_cost(self):
        #Запомнить стоимость продукта - цена + неразрывный пробел + валюта. 
        self.PRODUCT_COST = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_ELEM).text

    def should_be_cost_basket_equal_cost_product(self):
        # Сообщение со стоимостью корзины
        #time.sleep(60)
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_ALL_COST), "No basket cost reported"
        #Стоимость корзины совпадает с ценой продукта.
        message_basket_cost_text = self.get_text_element(*ProductPageLocators.MESSAGE_BASKET_COST)
        assert self.PRODUCT_COST == message_basket_cost_text, "{} not equal {}".format(self.PRODUCT_COST, message_basket_cost_text)

    def should_be_message_about_adding(self):
        #Сообщение о добавлении в корзину есть
        #time.sleep(60)
        assert self.is_element_present(*ProductPageLocators.MESSAGE_IN_BASKET), "No message added to basket"

        #Название продукта совпадет с тем товаром, который добавили
        message_text = self.get_text_element(*ProductPageLocators.MESSAGE_IN_BASKET)
        assert self.PRODUCT_NAME == message_text, "{} not equal message {}".format(self.PRODUCT_NAME, message_text)

    def should_be_not_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_IN_BASKET), "Should be no message added to basket"