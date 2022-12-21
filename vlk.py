from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.trendyol.com/")
driver.maximize_window()
sleep(5)
loginBtn = driver.find_element(By.XPATH,"//*[@id='account-navigation-container']/div/div[1]/div[1]/p")
loginBtn.click()
input()
#loginBtn = driver.find_element(By.XPATH,"//*[@id='navbar']/div/div/div/ul/li[3]/a")
x = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/div[1]/input")
x.click()
x.send_keys("berk.kaldar@etiya.com")

y = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/div[2]/div/div/input")
y.click()
y.send_keys("Abc123456")

input()