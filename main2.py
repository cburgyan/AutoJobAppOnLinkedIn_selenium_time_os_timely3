import selenium.common.exceptions

import timely3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import os


coding_timer = timely3.CodingTimer("time_main.txt")
# coding_timer.start_time()
# coding_timer.pause_time()
# coding_timer.unpause_time()
# coding_timer.stop_time()


URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_JT=I&geoId=103644278&keywords=python%20developer&location=" \
      "United%20States"


#Create Chrome Driver
CHROME_EXEC_PATH = "C:/Users/T852/DeveloperFoo/chromedriver_win32/chromedriver.exe"
servicer = webdriver.chrome.service.Service(CHROME_EXEC_PATH)
driver = webdriver.Chrome(service=servicer)


#Connect Driver to Website
driver.get(URL)


#Create selenium.webdriver.remote.webelement.WebElements
time.sleep(5)
go_to_sign_in_form_button_we = driver.find_element(by=By.LINK_TEXT, value="Sign in")
go_to_sign_in_form_button_we.click()


#Fill Out Login Form
time.sleep(4)
user_we = driver.find_element(by=By.ID, value="username")
user_we.send_keys(os.environ.get("USER"))
password_we = driver.find_element(by=By.ID, value="password")
password_we.send_keys(os.environ.get("PASS"))
sign_in_button_we = driver.find_element(by=By.CLASS_NAME, value="btn__primary--large")
sign_in_button_we.click()
# WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "btn__primary--large")))


#Get Number of results
time.sleep(5)
num_of_results_we = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/'
                                                           'header/div[1]/small')
num_of_results = int(num_of_results_we.text.split(" ")[0])


#Program Flow
for index in range(1, num_of_results + 1):
    #Click Job Listing
    time.sleep(3)
    job_listing_we = driver.find_element(by=By.XPATH, value=f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/'
                                                            f'div/ul/li[{index}]')
    job_listing_we.click()
    # WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{index}]'))).click()


    #Save Job Listing
    time.sleep(3)
    save_we = driver.find_element(by=By.CLASS_NAME, value="jobs-save-button")
    if save_we.text.split("\n")[0] == "Save":
        save_we.click()


    #Click Company Name
    time.sleep(3)
    company_we = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[3]/div[3]/div[2]/div/section[2]/div/'
                                                        'div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/'
                                                        'span[1]/a')
    company_name = company_we.text
    company_we.click()


    #Click Follow Button
    try:
        time.sleep(3)
        follow_company_we = driver.find_element(by=By.CLASS_NAME, value='follow')
        print(follow_company_we.text)
        if follow_company_we.text != "Following":
            follow_company_we.click()
    except selenium.common.exceptions.NoSuchElementException:
        print(f'Could NOT follow company, "{company_name}"!')


    #Return to Search Results Page
    time.sleep(2)
    driver.back()


    #Cancel Alert Message
    # time.sleep(2)
    # cancel_alert_button_we = driver.find_element(by=By.CLASS_NAME, value='artdeco-button__icon')
    # cancel_alert_button_we.click()


#Quit Driver
driver.quit()
