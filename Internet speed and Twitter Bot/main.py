from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL = ""
PASS = ""


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("user-data-dir=C:/Users/Fagner/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=options)
driver.get("https://www.speedtest.net/")
wait = WebDriverWait(driver, 10)

go_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[1]/a')))
go_button.click()

time.sleep(80)
down_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
up_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
print("Download speed:", down_speed)
print("Upload speed:", up_speed)

driver.quit()

if float(down_speed) < 650 or float(up_speed) < 300:
    tt_driver = webdriver.Chrome(options=options)
    tt_driver.get("https://x.com/")
    wait = WebDriverWait(tt_driver, 5)

    try:
        login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div')))
        login.click()
    except TimeoutException:
        pass
    else:
        email = wait.until(EC.visibility_of_element_located((By.NAME, "text")))
        email.send_keys(EMAIL, Keys.ENTER)
        user = wait.until(EC.visibility_of_element_located((By.NAME, "text")))
        user.send_keys("@Username", Keys.ENTER)
        password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys(PASS, Keys.ENTER)
    finally:
        tweet = f"Hey Internet Provider, why is my internet speed {down_speed} down / {up_speed} up when I pay for 650 down / 300up?"
        twit = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')))
        twit.send_keys(tweet)
        button = tt_driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        button.click()