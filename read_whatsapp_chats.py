from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument(
    "user-data-dir=C:\\Users\\ryash\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
)  # To prevent having to sign in again later (make a new profile and set path accordingly)

options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(60)

stealth(
    driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

web_url = "https://web.whatsapp.com/"

driver.get(web_url)

gc_names = [
    "Yash Raj",
]

elements = {}

for name in gc_names:
    element = driver.find_element(By.XPATH, f"//span[@title='{name}']")
    element.click()
    unread_element_holder = driver.find_element(By.XPATH, "//span[text()[contains(., 'unread message')]]/../../following-sibling::*[1]")
    time.sleep(2)
    text_elems = unread_element_holder.find_elements(By.XPATH, ".//span[contains(@class, 'selectable-text copyable-text')]/span")
    for text_elem in text_elems:
        with open(f"{name}.txt", "w") as outfile:
            outfile.write(text_elem.text + '\n')

