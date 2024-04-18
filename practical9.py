import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


try:
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/dragdrop")
    image = driver.find_element(By.ID, "image")
    box = driver.find_element(By.ID, "box")

    actions = ActionChains(driver=driver)
    actions.drag_and_drop(image, box)
    actions.perform()

    # verify the drop is success
    assert "Dropped!" in box.text
    print("Dropped successfully!")
    # time.sleep(10)
    
except Exception as e:
    print(e)

finally:
    driver.quit()