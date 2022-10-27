from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def build_options(arg: list,exp_arg: list):
    options = webdriver.ChromeOptions()
    for setting in arg:
        options.add_argument(setting)
    for exp_setting in exp_arg:
        options.add_experimental_option(*exp_setting)
    return options


def get_driver(url):
    options = build_options(["disable-infobars","start-maximized","disable-dev-shm-usage",
                             "disable-blink-features=AutomationControlled"],
                            [("excludeSwitches", ["enable-automation"])])
    service = Service("C:\\Users\lenovo\Documents\\random-apps\chromedriver_win32\chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    return driver


def auto_login(driver,by,by_user,by_pwd,user,pwd, wait=True):
    driver.find_element(by=by, value=by_user).send_keys(user)
    driver.find_element(by=by, value=by_pwd).send_keys(pwd + Keys.RETURN)
    if wait:
        time.sleep(2)


def main():
    driver = get_driver("http://automated.pythonanywhere.com/login")
    auto_login(driver,By.ID, "id_username", "id_password", "automated", "automatedautomated")
    return driver.find_element(by=By.XPATH, value="/html/body/div[1]/h1[2]").text


if __name__ == "__main__":
    print(main())