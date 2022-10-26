from simple_text import *
import time

service = Service("C:\\Users\lenovo\Documents\\random-apps\chromedriver_win32\chromedriver.exe")

def clean_text(text: str) -> float:
    """ Extract only the temperature from the text"""
    output = float(text.split(": ")[1])
    return output


# Alter script to pull a dynamic element0
def main():
    driver = get_driver()
    # Open the page and give it a chance to load a value
    time.sleep(2)
    element = driver.find_elements(By.XPATH, "/html/body/div[1]/div/h1[2]")
    return clean_text(element[0].text)

if __name__=="__main__":
    print(main())

