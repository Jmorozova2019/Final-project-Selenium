from pages.base_page import BasePage

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

import pytest

#@pytest.mark.skip
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

    #Выполнить проверки на той же странице
    product_page.should_be_message_about_adding()
    product_page.should_be_cost_basket_equal_cost_product()

#@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    #Проверить, что ссылка на страницу логина существует
    page.should_be_login_link()

#@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    #Перейти по ссылке на страницу логина
    page.go_to_login_page()

    #Проверить, что попали на нужную страницу по адресу
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

#@pytest.mark.skip
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    #Перейти в корзину
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)

    #Ожидаем, что в корзине нет товаров
    cart_page.should_be_no_any_product_in_cart()

    #Ожидаем, что есть текст о том что корзина пуста
    cart_page.should_be_message_empty_cart()
