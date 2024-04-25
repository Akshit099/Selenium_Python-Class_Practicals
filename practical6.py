import time
from selenium import webdriver
from selenium.webdriver.common.by import By


base_url = "https://en.wikipedia.org/wiki/Gluon"

driver = webdriver.Chrome()
driver.get(base_url)
print(driver.title)

url = driver.find_element(By.XPATH, '(//a[@title="Elementary particle"])[3]').get_attribute("href")

driver.get(url)
time.sleep(3)
print(driver.title)
driver.back()
driver.forward()
