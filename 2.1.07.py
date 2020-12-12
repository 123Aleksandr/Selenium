from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элемент-картинку, который является
    # изображением сундука с сокровищами, где спрятано
    # постоянно изменяющееся значение x
    x_element = browser.find_element_by_id("treasure")
    
    # Получим значение атрибута valuex с помощью встроенного
    # метода get_attribute, которое является значением x для задачи
    x = x_element.get_attribute("valuex")
    
    # Используем функцию calc(), которая рассчитает и вернет
    # значение функции, которое нужно ввести в текстовое поле
    y = calc(x)    

    # Находим поле для ввода и вводим ответ
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Найти и отметить checkbox "I'm the robot"
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # Найти и выбрать radiobutton "Robots rule!"
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Найти и нажать на кнопку "Submit
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла
