from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromedriver = r"C:\Users\nicol\Documents\chromedriver"
driver = webdriver.Chrome(chromedriver)

url = "https://www.youtube.no/"
#url2 = "https://www.nrk.no/"
driver.get(url)

driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
driver.get("http://www.google.com")

#driver.get(url2)