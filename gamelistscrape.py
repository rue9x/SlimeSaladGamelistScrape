import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

BASE_URL = "https://www.slimesalad.com/forum/viewforum.php?f=4"
PAGINATION = "&start="
# &start=50

def setup_driver():
    options = Options()
    options.add_argument('--disable-javascript')
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument('--disable-extensions')
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    options.add_argument("--disable-logging")
    options.add_argument('--log-level=OFF')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    try:
        driver = webdriver.Chrome(options=options)
    except:
        driver = webdriver.Chrome(options=options, executable_path="c:\\chromedriver\\chromedriver.exe")
    return driver

def scrape(driver):
	print ("OK")
	results = dict()
	time_to_stop = False
	for x in range(0, 1000, 50):
		driver.get(BASE_URL+PAGINATION+str(x))
		topics = driver.find_elements_by_xpath("//a[@class='topictitle']")
		for each in topics:
			gamename = each.text
			gameurl = each.get_attribute('href')
			if gameurl in results:
				time_to_stop = True
			else:
				results[gameurl] = gamename	
			if time_to_stop == True: 
				print ("Time to stop 1")
				break
		if time_to_stop == True:
			print ("Time to stop 2")
			break
	print ("Returning")
	return (results)

def main():
	driver = setup_driver()
	results = scrape(driver)
	for each in results:
		print (each+"\n"+results[each])
main()