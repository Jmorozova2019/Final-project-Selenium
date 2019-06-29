#-*-coding:cp1251-*-
from selenium import webdriver
import time


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/registration2.html"
browser.get(link)

# Ваш код, который заполняет обязательные поля
css_name = "[placeholder = 'Введите имя']"
name_elt = browser.find_element_by_css_selector(css_name)
name_elt.send_keys("Иван")

css_surname = "[placeholder = 'Введите фамилию']"
surname_elt = browser.find_element_by_css_selector(css_surname)
surname_elt.send_keys("Иванов")

css_email = "[placeholder = 'Введите Email']"
email_elt = browser.find_element_by_css_selector(css_email)
email_elt.send_keys("IvanovIvan@ya.ru")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text