# Automate form-filling with Selenium from csv data
# 11 September 2021
# by Peanuto

# Selenium automates web browsers by providing an interface that allows you  to write test scripts. In this case I am using Python.
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import win32api
import time
import sys

driver = webdriver.Chrome() 
driver.implicitly_wait(0.5)

URL = "YOUR_URL"
# launch the webpage containing information to be processed
driver.get(URL)

############### LOGIN PAGE (comment this section out if no login page is involved) ###############
USERNAME_FIELD = 'USERNAME_FIELD'
PASSWORD_FIELD = 'PASSWORD_FIELD'
USERNAME = 'YOUR_USERNAME' 
PASSWORD = 'YOUR_PASSWORD' 
SUBMIT_BUTTON_NAME = 'SUBMIT_BUTTON_NAME'

# input e-mail
driver.find_element_by_id('USERNAME_FIELD').send_keys("YOUR_USERNAME")

# input password
driver.find_element_by_id('PASSWORD_FIELD').send_keys("YOUR_PASSWORD")

# click login button
driver.find_element_by_name("SUBMIT_BUTTON_NAME").click()

total_buttons = 0 # keep track of number of buttons on the page, useful if all the buttons have the same name & usage
total_pages = 'NUM_BUTTONS' # keep track of number of pages, useful if there are many pages to go through
button_name = 'BUTTON_NAME' 
# iterate through all pages
for page in range(total_pages):

    # get number of buttons on the page
    number_li_elems = len(WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, button_name))))
    print(number_li_elems, "buttons on this page now")

    # get all view buttons into array
    all_buttons = driver.find_elements_by_class_name(button_name)

    # iterate through all view buttons
    for x in range(number_li_elems):

        try: 
            # get all buttons into array, msut do this at every loop or else the element will become stale
            # this is only necessary if the buttons take you to another page
            all_buttons = driver.find_elements_by_class_name(button_name)

            all_buttons[x].click() 

            total_buttons += 1 # increment number of view buttons (for debugging purpose)

            # go back one page
            # this is only necessary if the buttons take you to another page
            driver.back() 

            driver.implicitly_wait(3)
            print("I am at button number", x)
        
        except NoSuchElementException:
            print("I can't find the button, check again please!")

    print(page) # print current page number 

    try: 
        driver.find_element_by_class_name('next').click()
    except NoSuchElementException:
        print("************ I can't find the next button so I'll assume I'm at the last page :) ************")
        sys.exit(0)


