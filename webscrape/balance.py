#!/usr/bin/python3

# ===GOAL===
# Log into bank account and return checking and savings balances.
# To log: balances, date/time, IP of user, time of completion.

# Imports
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Settings
URL = "https://www.coastal24.com/"
LOG_FILE = "history.txt"

# Get args
if len(sys.argv) < 3:
    print("Username and password not supplied in command line")
    exit(1)

username = sys.argv[1]
password = sys.argv[2]

# Start
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)
assert "Coastal Credit Union" in driver.title

# Open login box
elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ngLoginApp")))
elem.click()

# Find and insert username/password
elem = driver.find_element_by_id("header-login-username")
elem.clear()
elem.send_keys(username)

elem = driver.find_element_by_id("header-login-password")
elem.clear()
elem.send_keys(password)

# Press submit button
driver.find_element_by_id("Submit").click()


# driver.close()
