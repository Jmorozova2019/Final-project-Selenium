from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators
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

    def should_be_message_about_adding(self, product_name):
        #Сообщение о добавлении в корзину есть
        assert self.is_element_present(*BasketPageLocators.MESSAGE_IN_BASKET), "No message added to basket"
        
        #Название продукта совпадет с тем товаром, который добавили
        message_text = self.get_text_element(*BasketPageLocators.MESSAGE_IN_BASKET)
        assert product_name in message_text, "{} not in message {}".format(product_name, message_text)

    def should_be_cost_basket_equal_cost_product(self, product_cost):
        # Сообщение со стоимостью корзины
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_ALL_COST), "No basket cost reported"
        
        #Стоимость корзины совпадает с ценой продукта.
        message_basket_cost_text = self.get_text_element(*BasketPageLocators.MESSAGE_BASKET_ALL_COST)
        assert product_cost in message_basket_cost_text, "{} not equal {}".format(product_cost, message_basket_cost_text)
