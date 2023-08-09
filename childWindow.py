from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")

# Opens tab in new window
driver.find_element(By.LINK_TEXT, "Click Here").click()

#Grabbing Window Names
windows = driver.window_handles

# Switching Window parent to child
driver.switch_to.window(windows[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()

# Switching window child to parent
driver.switch_to.window(windows[0])
assert driver.find_element(By.XPATH, "//h3[text()='Opening a new window']").text == "Opening a new window"
driver.close()


