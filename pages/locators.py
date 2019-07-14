from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    #Кнопка выбора языка
    language_xpath = "//select[@name = 'language']"
    LANGUAGE_LINK = (By.XPATH, language_xpath)

    #Кнопка Выполнить(переключить язык интерфейса)
    go_xpath = "//form[@id = 'language_selector']/button"
    GO_LINK = (By.XPATH, go_xpath)

class BasketPageLocators(object):
    #Товары в корзине
    products_in_basket_xpath = "//div[@class = 'basket-items']/div"
    PRODUCTS_IN_BASKET_LINK = (By.XPATH, products_in_basket_xpath)

    #Сообщение, что корзина пуста
    message_empty_xpath = "//*[contains(text(), 'корзина пуста')]"
    MESSAGE_EMPTY_LINK = (By.XPATH, message_empty_xpath)

class LoginPageLocators(object):
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class MainPageLocators(object):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

class ProductPageLocators(object):
    #Кнопка Добавить в корзину
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")    #Название продукта

    PRODUCT_NAME_ELEM = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/h1")

    #Цена продукта
    PRODUCT_COST_ELEM = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/p")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".message")

    #Кнопка Посмотреть корзину
    basket_link_xpath = "//div[@class = 'basket-mini pull-right hidden-xs']/span/a"
    BASKET_LINK = (By.XPATH, basket_link_xpath)

    #Сообщение "Стоимость корзины теперь составляет" - часть, относящиеся к цене
    cost_basket_xpath = "//div[@id = 'messages']/div/div[@class = 'alertinner ']/p/strong"
    MESSAGE_BASKET_COST = (By.XPATH, cost_basket_xpath)

    #Элемент Корзина Итого:
    message_basket_all_cost_xpath = "//div[@class = 'basket-mini pull-right hidden-xs']"
    MESSAGE_BASKET_ALL_COST = (By.XPATH, message_basket_all_cost_xpath)

    #Сообщение с названием добавленного товара
    mess_node_xpath = "//div[@id = 'messages' and @style = 'visibility: visible;']/descendant::strong"
    MESSAGE_IN_BASKET = (By.XPATH, mess_node_xpath)