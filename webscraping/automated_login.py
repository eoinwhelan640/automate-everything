# Script to open a browser, login and move to the homepage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "http://automated.pythonanywhere.com/login/"
password= "automatedautomated"

def build_options(arg: list,exp_arg: list):
    options = webdriver.ChromeOptions()
    for setting in arg:
        options.add_argument(setting)
    for exp_setting in exp_arg:
        options.add_experimental_option(*exp_setting)
    return options

def get_driver():
    options = build_options(["disable-infobars","start-maximized","disable-dev-shm-usage",
                             "disable-blink-features=AutomationControlled"],
                            [("excludeSwitches", ["enable-automation"])])
    service = Service("C:\\Users\lenovo\Documents\\random-apps\chromedriver_win32\chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com/login")
    return driver

def auto_login():
    driver = get_driver()
    # not assigninging a variable because we're not returning anything, we're sending info
    # sending the username "automated" to the input box for id_username on the webpage
    driver.find_element(by=By.ID, value="id_username").send_keys("automated")
    # time.sleep(2) - if want to see the input box get filled
    # This time send the password
    #driver.find_element(by="id", value="id_password").send_keys("automatedautomated")
    # Send password AND trigger the enter button so that the values of user + pwd are entered on the site
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    # If want to, show where we are to verify the login worked. Remember it's an attribute not a method.
    print(driver.current_url)
    time.sleep(2)

    # From there, pick out "Home" and navigate to it, also click it
    driver.find_element(by=By.XPATH, value="/html/body/nav/div/a").click() #send_keys(Keys.RETURN) is same as click here
    print(driver.current_url)


if __name__=="__main__":
    auto_login()