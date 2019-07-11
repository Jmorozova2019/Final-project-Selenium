from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.base_page import BasePage
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, link):
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)

    #Запомнить название продукта
    product_page.read_product_name()
    #Запомнить стоимость продукта
    product_page.read_product_cost()

    #Добавить в корзину и отправить код
    product_page.click_add_to_basket()
    product_page.solve_quiz_and_get_code()
    print(link)
    #Выполнить проверки
    product_page.should_be_message_about_adding()
    product_page.should_be_cost_basket_equal_cost_product()

