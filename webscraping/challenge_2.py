import time

from scraping_utils import *


url = "https://leetcode.com/accounts/login/"
user = "whelan.eoin6@gmail.com"
# pwd=
help_centre = "/html/body/div[2]/div/div[2]/footer/div/div/div/div/nav/ul/li[1]/a"


def main():
    driver = get_driver(url)
    auto_login(driver, By.ID, "id_login", "id_password", user, pwd=None)
    driver.find_element(by=By.XPATH, value=help_centre).click()
    time.sleep(5)

if __name__ == "__main__":
    main()
