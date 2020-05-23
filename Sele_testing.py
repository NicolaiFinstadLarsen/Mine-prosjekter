from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromedriver = r"C:\Users\nicol\Documents\chromedriver"
driver = webdriver.Chrome(chromedriver)

url = "https://www.aftenposten.no/"
#url2 = "https://www.nrk.no/"
driver.get(url)

driver.find_element_by_css_selector("body").send_keys(Keys.CONTROL+"t");
driver.get("http://www.bing.com")

#driver.get(url2)