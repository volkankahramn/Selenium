from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pathlib import Path
from constants import *

class Test_swagLabs:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def teardown_method(self):
        self.driver(quit)

    #DOĞRU KULLANICI İSMİ VE PAROLA GİRİLİR İSE
    def test_login(self):
        self.driver.get(BASE_DOMAIN_URL)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_ID )))
        username = self.driver.find_element(By.ID, USERNAME_ID)
        username.send_keys("problem_user")
        password = self.driver.find_element(By.ID, PASSWORD_ID)
        password.send_keys("secret_sauce")
        loginBtn = self.driver.finde_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/input")
        loginBtn.click()

        x = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")
        assert x.text == "PRODUCTS"

       #YANLIŞ KULLANICI İSMİ GİRİLİR İSE
    def test_loginErrorMessage(self):
        self.driver.get(BASE_DOMAIN_URL)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_ID)))
        username = self.driver.find_element(By.ID, USERNAME_ID)
        username.send_keys("problems_user")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        loginBtn = self.driver.finde_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/input")
        loginBtn.click()

        wrongLogin = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")


        assert wrongLogin.text == "Epic sadface: Username and password do not match any user in this service"
