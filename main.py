from selenium import webdriver 
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.kodlama.io/")
driver.maximize_window()

loginBtn = driver.find_element(By.XPATH,"//*[@id='navbar']/div/div/div/ul/li[3]/a")
#Login butonu text i giriş yap olmalıdır.
loginBtnText = loginBtn.text

if loginBtnText == "Giriş Yap":
    print("Test başarılı 😎")
else:
    print("Test Başarısız ❌")

loginBtn.click()

input()