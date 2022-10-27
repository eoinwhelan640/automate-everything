from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from automated_login import build_options
import datetime as dt


## Challenge is to build an api scraping the temperature and write it to a txt file every 5 seconds.


def get_driver():
    options = build_options(["disable-infobars","start-maximized","disable-dev-shm-usage",
                             "disable-blink-features=AutomationControlled"],
                            [("excludeSwitches", ["enable-automation"])])
    service = Service("C:\\Users\lenovo\Documents\\random-apps\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=service,options=options)

    driver.get("http://automated.pythonanywhere.com/login")
    return driver


def auto_login(driver,user,pwd):
    driver.find_element(by=By.ID, value="id_username").send_keys(user)
    driver.find_element(by=By.ID, value="id_password").send_keys(pwd + Keys.RETURN)
    time.sleep(5)


def scrape_value(driver, path):
    s = driver.find_element(by=By.XPATH, value=path).text
    return float(s.split(": ")[1])


def main_app():
    driver = get_driver()
    auto_login(driver, "automated", "automatedautomated")
    x = 0
    file = str(dt.date.today().strftime("%Y_%m_%d")) + ".txt"
    with open(file,"w", newline='\n') as write_file:
        while x<25:
            print("Running x=", x)
            x += 1
            out = str(scrape_value(driver, "/html/body/div[1]/h1[2]"))
            write_file.write(out + " ")
            time.sleep(5)
    return out


if __name__ == "__main__":
    main_app()

