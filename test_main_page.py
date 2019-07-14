from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest

main_page_link = "http://selenium1py.pythonanywhere.com"

#@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = MainPage(browser, main_page_link)
    page.open()

    #Перейти в корзину по кнопке в шапке сайта
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    #Ожидаем, что в корзине нет товаров
    cart_page.should_be_no_any_product_in_cart()
    #Ожидаем, что есть текст о том что корзина пуста
    cart_page.should_be_message_empty_cart()