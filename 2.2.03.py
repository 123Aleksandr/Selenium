from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
     
    number1 = browser.find_element_by_id("num1")
    a = number1.text
    number2 = browser.find_element_by_id("num2")
    b = number2.text
    x = str(int(a) + int(b))
    
    browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector("[value='" + x + "']").click()
    
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

    # end
