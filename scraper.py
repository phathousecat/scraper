from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_to_chromedriver = '/Users/Guest/Downloads/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'https://www.google.com/flights/explore/#explore;f=PDX;t=r-Europe-0x46ed8886cfadda85%253A0x72ef99e6b3fcf079;li=3;lx=5;d=2016-12-10'
browser.get(url)
elem = browser.find_elements_by_xpath("//*[contains(text(), '$')]")

element = WebDriverWait(browser, 5).until((EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '$')]"))))


bool = element.get_attribute('innerHTML')
print element
