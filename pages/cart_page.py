from .base_page import BasePage
from .locators import BasketPageLocators

class CartPage(BasePage):
    def message_is_disappeared(self):
        assert self.is_disappeared(*BasketPageLocators.MESSAGE_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_be_message_empty_cart(self):
        self.switch_language_to("ru")
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_LINK), "No message about empty cart"

    def should_be_no_any_product_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET_LINK), "Cart is not empty"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_IN_BASKET), \
            "Success message is presented, but should not be"


