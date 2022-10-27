from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(executable_path="c:\chromedriver\chromedriver.exe")
#browser.implicitly_wait(2)
browser.get("http://suninjuly.github.io/explicit_wait2.html")
#time.sleep(2)

x_element = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

print(x_element)

button = browser.find_element(By.TAG_NAME, "button")
button.click()


xx_element = browser.find_element(By.ID, "input_value")

def calc(xx):
    return str(math.log(abs(12*math.sin(int(xx)))))

yy = calc(xx_element.text)


answer = browser.find_element(By.ID, "answer")
answer.send_keys(str(yy))

submit=browser.find_element(By.ID, "solve")
submit.click()