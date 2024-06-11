import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
paths = r"D:\Automation study\Python Programming\Requirement\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)
driver.get("https://www.cowin.gov.in/")
driver.maximize_window()
print("The First Window is:", driver.title)
first_window = driver.find_element(By.LINK_TEXT,"FAQ")
first_window.click()
second_window = (driver.find_element(By.XPATH, '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a'))
second_window.click()
secondwindow=driver.window_handles[-2]
driver.switch_to.window(secondwindow)
displayedelement=driver.find_element(By.LINK_TEXT,"FAQ")
print("The Second Window is displayed:", displayedelement.is_displayed())
print("The Second Window is:", displayedelement.text)
thirdwindow =driver.window_handles[-1]
driver.switch_to.window(thirdwindow)
displayedelement2 =(driver.find_element(By.XPATH, '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a'))
print("The Third Window is displayed:", displayedelement2.is_displayed())
print("The Third Window is:", displayedelement2.text)
thirdwindow =driver.window_handles[-1]
driver.switch_to.window(thirdwindow)
time.sleep(4)
driver.close()
secondwindow =driver.window_handles[-1]
driver.switch_to.window(secondwindow)
time.sleep(4)
driver.close()
time.sleep(5)
# driver.quit()