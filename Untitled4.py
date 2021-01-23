#!/usr/bin/env python
# coding: utf-8

# In[59]:


import math


# In[3]:


import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome('C:/11/chromedriver.exe')

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()


# In[19]:


from selenium import webdriver
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome('C:/11/chromedriver.exe')
    browser.get(link)
    #f = browser.find_element_by_link_text("224592")
    #f.click()
    input1 = browser.find_element_by_name('first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


# In[ ]:


browser.quit()


# In[20]:


from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome('C:/11/chromedriver.exe')
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element_by_id('treasure')
    x_element1 = x_element.get_attribute('valuex')
    
    x = x_element1
    print(x)
    y = calc(x)
    r = browser.find_element_by_id('answer')
    r.send_keys(y)
    button = browser.find_element_by_id('robotCheckbox')
    button.click()
    button1 = browser.find_element_by_id('robotsRule')
    button1.click()
    button2 = browser.find_element_by_css_selector('[type="submit"]')
    button2.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


# In[ ]:


from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome('C:/11/chromedriver.exe')
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    input3.send_keys("Smolensk")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


# In[51]:


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
 
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome('C:/11/chromedriver.exe')
browser.get(link)

    # Ваш код, который заполняет обязательные поля
x = browser.find_element_by_id('num1')
x1 = x.text
y = browser.find_element_by_id('num2')
y1 = y.text
b = str(int(x1)+int(y1))
select = browser.find_element_by_class_name('custom-select')
for option in select.find_elements_by_tag_name('option'):
    if option.text == b:
        option.click()

    # Отправляем заполненную форму
button = browser.find_element_by_css_selector("body > div.container > form > button")
button.click()


# In[52]:


browser.quit()


# In[67]:


from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome('C:/11/chromedriver.exe')
    browser.get("http://suninjuly.github.io/execute_script.html")
    x_element = browser.find_element_by_id('input_value')
    x_element1 = x_element.text
    
    x = int(x_element1)
    
    y = str(math.log(abs(12*math.sin(x))))
    r = browser.find_element_by_id('answer')
    r.send_keys(y)
    button = browser.find_element_by_id('robotCheckbox')
    button.click()
    browser.execute_script("window.scrollBy(0, 150);")
    button1 = browser.find_element_by_id('robotsRule')
    button1.click()
    button2 = browser.find_element_by_css_selector('[type="submit"]')
    button2.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


# In[72]:


from selenium import webdriver
import time
import os 


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome('C:/11/chromedriver.exe')
    browser.get(link)
    #f = browser.find_element_by_link_text("224592")
    #f.click()
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("Smolensk")
    browser.execute_script("window.scrollBy(0, 150);")

    #current_dir = os.path.abspath(os.path.dirname(__file__))     
    file_path = ('C:/Users/user/file.txt')           # добавляем к этому пути имя файла 
    button = browser.find_element_by_id('file')
    button.send_keys(file_path)
    
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


# In[3]:


from selenium import webdriver
import time
import os 
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome('C:/11/chromedriver.exe')
    browser.get(link)
    
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_id('input_value')
    x_element1 = x_element.text
    
    x = int(x_element1)
    
    y = str(math.log(abs(12*math.sin(x))))
    r = browser.find_element_by_id('answer')
    r.send_keys(y)
    button2 = browser.find_element_by_css_selector('[type="submit"]')
    button2.click()
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


# In[19]:


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import os 
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome('C:/11/chromedriver.exe')
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    #button.click()
    button = browser.find_element_by_id('book')
    button.click()
    
    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)
    browser.execute_script("window.scrollBy(0, 150);")

    
    x_element = browser.find_element_by_id('input_value')
    x_element1 = x_element.text
    
    x = int(x_element1)
    
    y = str(math.log(abs(12*math.sin(x))))
    r = browser.find_element_by_id('answer')
    r.send_keys(y)
    button2 = browser.find_element_by_css_selector('[type="submit"]')
    button2.click()
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


# In[15]:


browser.quit()


# In[ ]:




