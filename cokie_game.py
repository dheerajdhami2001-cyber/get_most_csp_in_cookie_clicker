from dataclasses import replace

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
cps = driver.find_element(By.ID, value="cps")

five_min = time.time() + 60*5
timeout = time.time() + 5

while time.time() < five_min:
    cookie.click()
    if timeout < time.time():
        earned_cookie = int(driver.find_element(By.ID, value="money").text.replace(",",""))
        cursor_cost = int(driver.find_element(By.XPATH, value ='//*[@id="buyCursor"]/b').text.split()[2].replace(",",""))
        grandma_cost = int(driver.find_element(By.XPATH,value = '//*[@id="buyGrandma"]/b').text.split()[2].replace(",",""))
        factory_cost = int(driver.find_element(By.XPATH,value = '//*[@id="buyFactory"]/b').text.split()[2].replace(",",""))
        mine_cost = int(driver.find_element(By.XPATH,value = '//*[@id="buyMine"]/b').text.split()[2].replace(",",""))
        shipment_cost = int(driver.find_element(By.XPATH,value = '//*[@id="buyShipment"]/b').text.split()[2].replace(",",""))
        alchemy_cost = int(driver.find_element(By.XPATH,value = '//*[@id="buyAlchemy lab"]/b').text.split()[3].replace(",",""))
        protal_cost = int(driver.find_element(By.XPATH,value = '//*[@id="buyPortal"]/b').text.split()[2].replace(",",""))
        time_machine_cost = int(driver.find_element(By.XPATH,value = '//*[@id="buyTime machine"]/b').text.split()[3].replace(",",""))
        if earned_cookie >= time_machine_cost:
            driver.find_element(By.ID,value ="buyTime machine").click()
        elif earned_cookie >= protal_cost:
            driver.find_element(By.ID,value ="buyPortal").click()
        elif earned_cookie >= alchemy_cost:
            driver.find_element(By.ID,value ="buyAlchemy lab").click()
        elif earned_cookie >= shipment_cost:
            driver.find_element(By.ID,value ="buyShipment").click()
        elif earned_cookie >= mine_cost:
            driver.find_element(By.ID,value ="buyMine").click()
        elif earned_cookie >= factory_cost:
            driver.find_element(By.ID,value ="buyFactory").click()
        elif earned_cookie >= grandma_cost:
            driver.find_element(By.ID,value ="buyGrandma").click()
        elif earned_cookie >= cursor_cost:
            driver.find_element(By.ID,value ="buyCursor").click()

        timeout = time.time() + 5

print(f"wow your cps are {cps} ")