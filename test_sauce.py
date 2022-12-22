from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pathlib import Path
from constants import *

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    self.driver.get(BASE_DOMAIN_URL)
    self.driver.set_window_size(1274, 800)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,USERNAME)))
    username = self.driver.find_element(By.CSS_SELECTOR, USERNAME)
    username.send_keys("standard_user")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD)))
    password = self.driver.find_element(By.CSS_SELECTOR, PASSWORD)
    password.send_keys("secret_sauce")
    loginBtn = self.driver.find_element(By.CSS_SELECTOR, LOGINBTN)
    loginBtn.click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, INVENTORY_ITEMNAME)))
    x = self.driver.find_elements(By.CSS_SELECTOR, INVENTORY_ITEMNAME)
    assert len(x) > 0
  #hatalı giriş
  def test_loginfail(self):
    self.driver.get(BASE_DOMAIN_URL)
    self.driver.set_window_size(1274, 800)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, USERNAME)))
    username = self.driver.find_element(By.CSS_SELECTOR, USERNAME)
    username.click()
    username = self.driver.find_element(By.CSS_SELECTOR, USERNAME)
    username.send_keys("standard_user1")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD)))
    password = self.driver.find_element(By.CSS_SELECTOR, PASSWORD)
    password.click()
    password = self.driver.find_element(By.CSS_SELECTOR, PASSWORD)
    password.send_keys("1")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, LOGINBTN)))
    loginBtn = self.driver.find_element(By.CSS_SELECTOR, LOGINBTN)
    loginBtn.click()

    assert self.driver.find_element(By.CSS_SELECTOR, ERROR).text == "Epic sadface: Username and password do not match any user in this service"
  
  def test_inventor_item(self):
        
        self.driver.get(BASE_DOMAIN_URL)
        self.driver.set_window_size(1274, 800)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, USERNAME)))
        username = self.driver.find_element(By.CSS_SELECTOR, USERNAME)
        username.send_keys("standard_user")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD)))
        password = self.driver.find_element(By.CSS_SELECTOR, PASSWORD)
        password.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.CSS_SELECTOR, LOGINBTN)
        loginBtn.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, INVENTORY_ITEM )))
        image = self.driver.find_elements(By.XPATH, INVENTORY_ITEM )
        assert len(image)  == 6

  def test_remove(self):
    self.driver.get(BASE_DOMAIN_URL)
    self.driver.set_window_size(1278, 806)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, USERNAME)))
    username = self.driver.find_element(By.CSS_SELECTOR, USERNAME)
    username.click()
    username = self.driver.find_element(By.CSS_SELECTOR, USERNAME)
    username.send_keys("standard_user")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD)))
    password = self.driver.find_element(By.CSS_SELECTOR, PASSWORD)
    password.click()
    password = self.driver.find_element(By.CSS_SELECTOR, PASSWORD)
    password.send_keys("secret_sauce")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, LOGINBTN)))
    loginBtn = self.driver.find_element(By.CSS_SELECTOR, LOGINBTN)
    loginBtn.click()
    addBtn = self.driver.find_element(By.CSS_SELECTOR, DATA_TEST_ADD)
    addBtn.click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, DATA_TEST_REMOVE)))
    assert self.driver.find_element(By.CSS_SELECTOR, DATA_TEST_REMOVE).text == "REMOVE"
    
  def test_number(self):
    self.driver.get(BASE_DOMAIN_URL)
    self.driver.set_window_size(1278, 806)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, USERNAME)))
    username = self.driver.find_element(By.CSS_SELECTOR, USERNAME)
    username.click()
    username = self.driver.find_element(By.CSS_SELECTOR, USERNAME)
    username.send_keys("standard_user")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD)))
    password = self.driver.find_element(By.CSS_SELECTOR, PASSWORD)
    password.click()
    password =self.driver.find_element(By.CSS_SELECTOR, PASSWORD)
    password.send_keys("secret_sauce")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, LOGINBTN)))
    loginBtn = self.driver.find_element(By.CSS_SELECTOR, LOGINBTN)
    loginBtn.click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, INVENTORY_ITEMNAME)))
    assert self.driver.find_element(By.CSS_SELECTOR, INVENTORY_ITEMNAME).text == "Sauce Labs Backpack"
    addBtn = self.driver.find_element(By.CSS_SELECTOR, DATA_TEST_ADD)
    addBtn.click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")))
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
    assert len(elements) == 1
