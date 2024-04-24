from selenium import webdriver
from selenium.webdriver.common.by import By

# base_url = "https://erp.ganpatuniversity.ac.in/"
base_url = "https://mail.google.com/"
driver = webdriver.Chrome()
driver.get(base_url)
driver.save_screenshot("screenshots/gmail_homepage.png")  # Corrected file path
element = driver.find_element(By.XPATH, '//*[@id="headingText"]/span')
element.screenshot("screenshots/gmail_element.png")  # Corrected file path
driver.quit()
