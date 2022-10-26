from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Download from https://chromedriver.storage.googleapis.com/index.html?path=107.0.5304.62/ and store locally
service = Service("C:\\Users\lenovo\Documents\\random-apps\chromedriver_win32\chromedriver.exe")


def get_driver():
    # Options that make web browsing work smoother
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars") # no boxes popping up when you hover on something
    options.add_argument("start-maximized") # maximised window
    options.add_argument("disable-dev-shm-usage") # avoid some issues when using from a linux machine
    options.add_argument("no-sandbox") # grants us better access privileges on a browser
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) # options to help selenium avoid detection
    # by webpages that don't like scripts hitting them. Both ^ and below are for this
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def main():
    driver = get_driver()
    # xpath is taken by inspecting element on the webpage and copying xpath from part we want
    # XPATh is referncing xml format of html on webpage, we're finding it via that
    element = driver.find_elements(by="xpath", value="/html/body/div[1]/div/h1[1]")
    #element = driver.find_elements(By.XPATH, "/html/body/div[1]/div/h1[1]")
    # The elements variable is a list, so need to access the text attribute of each object in element list.
    # But the list is length 1, could have pulled more elements if we wanted I presume
    return element[0].text

if __name__=="__main__":
    print(main())

