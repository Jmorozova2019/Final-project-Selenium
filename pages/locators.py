from selenium.webdriver.common.by import By

class MainPageLocators(object):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

class LoginPageLocators(object):
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class ProductPageLocators(object):
    #Название продукта
    PRODUCT_NAME_ELEM = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/h1")

    #Цена продукта
    PRODUCT_COST_ELEM = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/p")

    #Кнопка Добавить в корзину
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".message")

class BasketPageLocators(object):
    #Сообщение с названием добавленного товара
    mess_node_xpath = "//div[@id = 'messages' and @style = 'visibility: visible;']/descendant::strong"
    MESSAGE_IN_BASKET = (By.XPATH, mess_node_xpath)

    #Элемент Корзина Итого:
    all_cost_xpath = "//div[@class = 'basket-mini pull-right hidden-xs']"
    MESSAGE_BASKET_ALL_COST = (By.XPATH, all_cost_xpath)
    
    #Сообщение "Стоимость корзины теперь составляет" - часть, относящиеся к цене
    cost_basket_xpath = "//div[@id = 'messages']/div/div[@class = 'alertinner ']/p/strong"
    MESSAGE_BASKET_COST = (By.XPATH, cost_basket_xpath)