from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromedriver = r"C:\Users\nicol\Documents\chromedriver"
driver = webdriver.Chrome(chromedriver)

url = "https://www.aftenposten.no/"
#url2 = "https://www.nrk.no/"
driver.get(url)

elem = driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
driver.get("www.bing.com")

#driver.get(url2)