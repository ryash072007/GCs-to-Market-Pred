from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument(
    "user-data-dir=C:\\Users\\ryash\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
)  # To prevent having to sign in again later (make a new profile and set path accordingly)

# options.add_argument("--headless")

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

gc_names = [
    "Ayush PATRO",
]

driver.get(web_url)
element = driver.find_element(By.XPATH, f"//span[@title='{gc_names[0]}']")
element.click()

time.sleep(300)
