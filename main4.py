import timely3
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time


coding_timer = timely3.CodingTimer("time_main.txt")
# coding_timer.start_time()
# coding_timer.pause_time()
# coding_timer.unpause_time()
# coding_timer.stop_time()


URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_JT=I&geoId=103644278&keywords=python%20developer&location=" \
      "United%20States"


WEBELEMENT_WAIT_TIME = 10


#Create Chrome Driver
CHROME_EXEC_PATH = 'C:/Users/T852/DeveloperFoo/chromedriver_win32/chromedriver.exe'
servicer = webdriver.chrome.service.Service(CHROME_EXEC_PATH)
driver = webdriver.Chrome(service=servicer)


#Connect Driver to Website
driver.get(URL)


#Click Button to go to Login Form
button_to_login_form_we = WebDriverWait(driver, WEBELEMENT_WAIT_TIME).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Sign in')))
button_to_login_form_we.click()


#Fill Out Login Form
user_we = WebDriverWait(driver, WEBELEMENT_WAIT_TIME).until(expected_conditions.element_to_be_clickable((By.ID, 'username')))
user_we.send_keys(os.environ.get("USER"))

password_we = WebDriverWait(driver, WEBELEMENT_WAIT_TIME).until(expected_conditions.element_to_be_clickable((By.ID, 'password')))
password_we.send_keys(os.environ.get("PASS"))

sign_in_btn_we = WebDriverWait(driver, WEBELEMENT_WAIT_TIME).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'btn__primary--large')))
sign_in_btn_we.click()


#Get of Job Listings
num_of_search_results_we = WebDriverWait(driver, WEBELEMENT_WAIT_TIME).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/header/div[1]/small')))
num_of_search_results = int(num_of_search_results_we.text.split(" ")[0])

for index in range(1, num_of_search_results + 1):
    #Click Next Job Listing
    try:
        job_listing_we = WebDriverWait(driver, WEBELEMENT_WAIT_TIME).until(expected_conditions.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{index}]')))
        job_listing_we.click()
    except Exception:
        #Remove Save-Status Pop-up Message
        try:
            save_status_pop_up_close_btn_we = WebDriverWait(driver, WEBELEMENT_WAIT_TIME).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div/div/button')))
            save_status_pop_up_close_btn_we.click()
        except Exception as error_message:
            print(f"Something went wrong:\n{error_message}")
        else:
            #Try clicking job listing again
            job_listing_we.click()

    #Save Job Listing
    save_we = WebDriverWait(driver, WEBELEMENT_WAIT_TIME).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'jobs-save-button')))
    if save_we.text.split("\n")[0] == "Save":
        save_we.click()


    #Click on Company
    company_we = WebDriverWait(driver, WEBELEMENT_WAIT_TIME).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/span[1]/a')))
    company_name = company_we.text
    company_we.click()


    #Follow Company
    try:
        follow_btn_we = WebDriverWait(driver, WEBELEMENT_WAIT_TIME).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'follow')))
        if follow_btn_we.text != "Following":
            follow_btn_we.click()
        print(f'Following the company, {company_name}')
    except Exception:
        print(f'Could NOT follow the company, "{company_name}"!!')


    #Return to search Results
    time.sleep(1)
    driver.back()

#Quit Driver
driver.quit()