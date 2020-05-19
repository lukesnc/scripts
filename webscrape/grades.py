#!/usr/bin/python3

# ===GOAL===
# Log into school account and return this semester's grades.

# Imports
import sys

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# Settings
URL = "https://my.ncedcloud.org"

# Get args
if sys.argv[1] == '--help':
    print("Usage: python3 grades.py [NCED USERNAME]", end=' ') 
    print("[NCED PASSWORD] [WAKEID USERNAME] [WAKEID PASSWORD]")
    exit(0)

if len(sys.argv) < 5:
    print("Usernames and passwords not supplied in command line")
    exit(1)

nced_username = sys.argv[1]
nced_password = sys.argv[2]
wakeid_username = sys.argv[3]
wakeid_password = sys.argv[4]

# Start
print("Starting...")
driver = webdriver.Chrome()
driver.get(URL)
assert "RapidIdentity" in driver.title

# Input username
elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "identification")))
elem.clear()
elem.send_keys(nced_username)

driver.find_element_by_id("authn-go-button").click()

# Input password
elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ember539")))
elem.clear()
elem.send_keys(nced_password)

driver.find_element_by_id("authn-go-button").click()

# Pick student - NEXT PAGE
assert "WakeID Portal" in driver.title

chooser = Select(driver.find_element_by_id("ember468"))
chooser.select_by_visible_text("Student")

driver.close()
exit(0)
