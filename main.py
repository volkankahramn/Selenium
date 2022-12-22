from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://www.kodlama.io/")
driver.maximize_window()
loginBtnFinder = (By.XPATH,"//*[@id='navbar']/div/div/div/ul/li[3]/a")#neye göre locate olacağım.
WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(loginBtnFinder))#defansif kodlama
loginBtn = driver.find_element(loginBtnFinder)
#Login butonu text i giriş yap olmalıdır.
#Condition max kaç sn beklesin?

#WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(By.XPATH,"//*[@id='navbar']/div/div/div/ul/li[3]/a"))
loginBtnText = loginBtn.text
#WebDriverWait => condition bazlı çalışır 
#login btn görüne kadar 5 sn beklemeli

if loginBtnText == "Giriş Yap":
    print("Test başarılı 😎")
else:
    print("Test Başarısız ❌")

loginBtn.click()

input()
#pytest =>  pytest dosyalaarı"test_" prefixi(ön ek) ile başlar.
#pytest classları => "Test_" prefixi ile başlar.
#pytest fonksiyonları =>"test_" prefixi ile başlar. 