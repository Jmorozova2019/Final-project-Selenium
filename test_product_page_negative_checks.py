from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.base_page import BasePage
import pytest
import time

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

def test_guest_cant_see_success_message(browser): 
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)

    start = time.time()
    #Проверяем, что нет сообщения об успехе
    product_page.should_not_be_success_message()
    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")