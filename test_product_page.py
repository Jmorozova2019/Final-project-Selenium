from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.base_page import BasePage
import pytest

PRODUCT_PAGE_URL_1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
PRODUCT_PAGE_URL_2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

product_1_name = 'The shellcoder\'s handbook'
product_1_cost = '9,99 £'

product_2_name = 'Coders at Work'
product_2_cost = '19,99 £'

@pytest.mark.parametrize('PAGE_URL, product_name, product_cost', [(PRODUCT_PAGE_URL_1, product_1_name, product_1_cost), (PRODUCT_PAGE_URL_2, product_2_name, product_2_cost)])
def test_guest_can_add_product_to_cart(browser, PAGE_URL, product_name, product_cost):
    page = MainPage(browser, PAGE_URL)
    page.open()
    product_page = ProductPage(browser, PAGE_URL)

    #Запомнить название продукта
    product_page.read_product_name()
    #Запомнить стоимость продукта
    product_page.read_product_cost()

    #Добавить в корзину и отправить код
    product_page.click_add_to_basket()
    product_page.solve_quiz_and_get_code()

    #Выполнить проверки
    product_page.should_be_message_about_adding(product_name)
    product_page.should_be_cost_basket_equal_cost_product(product_cost)

