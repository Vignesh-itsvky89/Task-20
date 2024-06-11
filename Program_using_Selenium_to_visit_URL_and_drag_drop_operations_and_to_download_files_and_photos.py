import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver path and options
paths = r"D:\Automation study\Python Programming\Requirement\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Open the Labour Ministry website
driver.get("https://labour.gov.in/")
time.sleep(3)

# Navigate to the "Documents" menu
documents_menu = driver.find_element(By.LINK_TEXT, "Documents")
actions = ActionChains(driver)
actions.move_to_element(documents_menu).perform()
time.sleep(2)  # Wait for the dropdown menu to appear

# Click on "Monthly Progress Report"
monthly_report_link = driver.find_element(By.LINK_TEXT, "Monthly Progress Report")
monthly_report_url = monthly_report_link.get_attribute('href')

# Download the monthly progress report
report_response = requests.get(monthly_report_url)
with open(r"D:\Automation study\Python Programming\Selenium\Selenium_Class_Files\Monthly_Progress_Report.pdf", 'wb') as file:
    file.write(report_response.content)

print("Monthly Progress Report downloaded successfully.")

media_menu = driver.find_element(By.LINK_TEXT, "Media")
media_menu.click()

allpreseerelease = driver.find_element(By.LINK_TEXT,"Click for more info of Press Releases")
allpreseerelease.click()

photo_gallery_menu = driver.find_element(By.LINK_TEXT, "Photo Gallery")
photo_gallery_menu.click()
time.sleep(5)  # Wait for the page to load

# Wait for the photo gallery page to load
driver.switch_to.window(driver.window_handles[1])
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".views-field-field-image img")))

# Create a folder to store the photos
photo_folder = r"\Automation study\Python Programming\Selenium\Selenium_Class_Files\Photo_Gallery"
if not os.path.exists(photo_folder):
    os.makedirs(photo_folder)

# Download the first 10 photos from the photo gallery
photos = driver.find_elements(By.CSS_SELECTOR, ".views-field-field-image img")[:10]
for index, photo in enumerate(photos):
    photo_url = photo.get_attribute('src')
    if not photo_url.startswith('http'):
        photo_url = "https://labour.gov.in" + photo_url  # Ensure the URL is absolute
    photo_response = requests.get(photo_url)
    with open(os.path.join(photo_folder, f"photo_{index + 1}.jpg"), 'wb') as file:
        file.write(photo_response.content)
    print(f"Downloaded photo {index + 1}")

print("Photos downloaded successfully.")