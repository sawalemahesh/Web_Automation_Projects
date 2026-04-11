from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_login():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.linkedin.com/in/mahesh-sawale/")
    driver.close(3)
