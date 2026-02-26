import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_error_occurs_if_description_less_than_ten_char():
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/notes/add/')
    driver.find_element(By.NAME, 'title').send_keys('Some notes')
    driver.find_element(By.NAME, 'description').send_keys('descri')
    driver.find_element(By.NAME, 'submit').click()
    time.sleep(2)
    error = driver.find_element(By.TAG_NAME, 'li').text
    assert'Description must by at least 10 char long' in error
    driver.quit()
