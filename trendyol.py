from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.trendyol.com/")
#driver2 = driver.get("https://www.trendyol.com/")
#driver2.find_Element(By.XPATH, '//*[@id="gender-popup-modal"]/div/div/div[1]/svg')
sleep(3)
popup = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/div/div/div/div[2]/div[2]/a/span[1]/img")
popup.click()
searchBtn = driver.find_element(By.XPATH, "//*[@id='account-navigation-container']/div/div[1]/div[1]/p")
searchBtn.click() #Giriş Yap
email= driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/div[1]/input")
email.click()
email.send_keys("berk.kaldar@etiya.com")
sleep(1)
password = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/div[2]/div/div/input")
password.click()
password.send_keys("Abc123456")
sleep(2)

searchBtn = driver.find_element(By.XPATH, "//*[@id='login-register']/div[3]/div[1]/form/button/span")
searchBtn.click()

# searchBtn = searchBtn.text
# if searchBtn =="GIRIŞ YAP":
#     print("Test Başarılı 😍")
# else:
#     print("Test Başarısız 😒")

# input()
asilBaslik=driver.title
if  asilBaslik=="Sepete En Çok Eklenenler":
    print("Giriş başarılı")
else:
    print("Giriş başarısız!") 
input()