import selenium.common.exceptions

import timely3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


coding_timer = timely3.CodingTimer("time_main.txt")
# coding_timer.start_time()
# coding_timer.pause_time()
# coding_timer.unpause_time()
# coding_timer.stop_time()


URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_JT=I&geoId=103644278&keywords=python%20developer&location=United%20States"


#Create Chrome Driver
CHROME_EXEC_PATH = "C:/Users/T852/DeveloperFoo/chromedriver_win32/chromedriver.exe"
servicer = webdriver.chrome.service.Service(CHROME_EXEC_PATH)
driver = webdriver.Chrome(service=servicer)


#Connect Driver to Website
driver.get(URL)


#Create selenim.webdriver.remote.webelement.WebElement
time.sleep(2)
sign_we = driver.find_element(by=By.CLASS_NAME, value="cta-modal__primary-btn")


#Program Flow
#--Click Sign in
sign_we.click()


#----Create WebElements for login
time.sleep(6)
user_we = driver.find_element(by=By.ID, value="username")
password_we = driver.find_element(by=By.ID, value="password")
agree_we = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')

#----Login
user_we.send_keys(os.environ.get("USER"))
password_we.send_keys(os.environ.get("PASS"))
agree_we.click()


#--Get Number of Search Results
time.sleep(5)
number_of_job_listings_we = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/header/div[1]/small')
num_of_job_listings = int(number_of_job_listings_we.text.split(" ")[0])
print(num_of_job_listings)
for index in range(1, num_of_job_listings + 1):
    #Select Next Job Listing
    time.sleep(2)
    job_title2_we = driver.find_element(by=By.XPATH, value=f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{index}]')
    job_title2_we.click()


    #Save Company
    time.sleep(5)
    save_we = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
    if save_we.text.split("\n")[0] != "Saved":
        save_we.click()
    print(save_we.text.split("\n")[0])

    #Select Company Link
    time.sleep(2)
    company2_we = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/span[1]/a')
    company_name = company2_we.text
    company2_we.click()


    #Follow Company
    time.sleep(3)
    try:
        follow_we = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[3]/div[1]/div[1]/button')
        if follow_we.text != "Following":
            follow_we.click()
    except selenium.common.exceptions.NoSuchElementException as error_message:
        print(f'Could NOT find a follow button for the company, "{company_name}".')


    #Go Back to Search Results Page
    time.sleep(4)
    driver.back()


#Quit Driver
time.sleep(5)
driver.quit()


