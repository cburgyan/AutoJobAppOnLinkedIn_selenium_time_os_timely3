import timely3
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time


coding_timer = timely3.CodingTimer("time_main.txt")
# coding_timer.start_time()
# coding_timer.pause_time()
# coding_timer.unpause_time()
# coding_timer.stop_time()


URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_JT=I&geoId=103644278&keywords=python%20developer&location=" \
      "United%20States"

WAIT_THIS_MANY_SECONDS = 10


#Create Chrome Driver
CHROME_EXEC_PATH = 'C:/Users/T852/DeveloperFoo/chromedriver_win32/chromedriver.exe'

servicer = webdriver.chrome.service.Service(CHROME_EXEC_PATH)
driver = webdriver.Chrome(service=servicer)


#Connect Driver to Website
driver.get(URL)


#Click Button to Go to Login Form
click_to_sign_in_we = WebDriverWait(driver, WAIT_THIS_MANY_SECONDS).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
click_to_sign_in_we.click()


#Fill Out Login Form
user_we = WebDriverWait(driver, WAIT_THIS_MANY_SECONDS).until(expected_conditions.element_to_be_clickable((By.ID, "username")))
user_we.send_keys(os.environ.get("USER"))

pass_we = WebDriverWait(driver, WAIT_THIS_MANY_SECONDS).until(expected_conditions.element_to_be_clickable((By.ID, "password")))
pass_we.send_keys(os.environ.get("PASS"))

sign_in_button = WebDriverWait(driver, WAIT_THIS_MANY_SECONDS).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "btn__primary--large")))
sign_in_button.click()


#Get Number of Search Results
num_of_search_results_we = WebDriverWait(driver, WAIT_THIS_MANY_SECONDS).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/header/div[1]/small')))
num_of_search_results = int(num_of_search_results_we.text.split(" ")[0])


#Loop for Saving Job Listing and Following Company
for index in range(1, num_of_search_results + 1):
    #Get Job Listing
    try:
        job_listing_we = WebDriverWait(driver, WAIT_THIS_MANY_SECONDS).until(expected_conditions.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{index}]')))
        job_listing_we.click()
    except Exception:

        # Cancel Save-status-change Alert Message
        try:
            save_status_message_we = WebDriverWait(driver, WAIT_THIS_MANY_SECONDS).until(
                expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div/div/button')))
            save_status_message_we.click()
        except Exception as error_message:
            pass
        else:
            #Try to click Job listing AFTER closing the Pop Alert Message
            job_listing_we = WebDriverWait(driver, WAIT_THIS_MANY_SECONDS).until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{index}]')))
            job_listing_we.click()



    #Save Job Listing
    save_we = WebDriverWait(driver, WAIT_THIS_MANY_SECONDS).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'jobs-save-button')))
    if save_we.text.split("\n")[0] == "Save":
        save_we.click()


    #Get Company of Job Listing
    company_we = WebDriverWait(driver, WAIT_THIS_MANY_SECONDS).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/span[1]/a')))
    company_name = company_we.text
    company_we.click()


    #Click Follow Company
    try:
        follow_we = WebDriverWait(driver, WAIT_THIS_MANY_SECONDS).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'follow')))
        if follow_we.text != "Following":
            follow_we.click()
    except Exception:
        print(f'Could NOT follow the company, "{company_name}"!!')
    else:
        print(f'Following "{company_name}"')


    #Return to Previous Page of Search Results
    time.sleep(1)
    driver.back()


#Quit Driver
driver.quit()