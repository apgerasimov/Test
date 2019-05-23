
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import allure

def test_google():

    driver = webdriver.Chrome('D:/awd/chromedriver.exe')
    driver.get('https://google.com')
    search_input = driver.find_element_by_name('q')
    search_button = driver.find_element_by_class_name('gNO89b')
    search_input.send_keys('Prod.ua')
    driver.implicitly_wait(5)
    search_button.click()
    driver.implicitly_wait(5)
    prod_button = driver.find_element_by_class_name('LC20lb')
    driver.implicitly_wait(5)
    prod_button.click()
    driver.set_script_timeout(10)
    login_button = driver.find_element_by_xpath('/html/body/div[3]/ul/div/li[1]/span')
    driver.implicitly_wait(5)
    login_button.click()
    phone_number_input = driver.find_element_by_xpath('//*[@id="phone-block__phone-auth"]')
    phone_number_input.send_keys('0506007780')
    password_input = driver.find_element_by_xpath('//*[@id="auth-block__pass"]')
    password_input.send_keys('Uni321321321')
    login_button_prod = driver.find_element_by_xpath('//*[@id="form_login"]/button')
    login_button_prod.click()
