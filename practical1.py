from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

details = {893: "jksdl", 
           8943: "JLK", 
           712: "LJK"}

for id, password in details.items():
    try:
            driver : webdriver = webdriver.Chrome()
            driver.get("https://www.google.com")
            driver.maximize_window()
            element : webelement = driver.find_element(By.NAME, "q")
            element.send_keys("Ganpat university erp login", Keys.ENTER)
            driver.find_element(By.PARTIAL_LINK_TEXT, "E-Governance").click()
            driver.find_element(By.NAME, "txtUserName").send_keys(id)
            driver.find_element(By.NAME, "txtPassword").send_keys(password)
            driver.find_element(By.XPATH, '//*[@id="ibtnLogin"]').click()
            print(id, " ---> ", driver.title)
            print("URL:  ", driver.current_url)
            print("Page Source:  ", driver.page_source[:10])

            # verifying the page title
            assert "E-Governance" in driver.title
            print("Success!")
            
    except:
        print("Error Occurred!")

    finally:
        driver.close()