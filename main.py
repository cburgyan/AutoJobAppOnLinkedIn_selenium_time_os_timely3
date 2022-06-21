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
# user_we = driver.find_element(by=By.ID, value="email-or-phone")
# password_we = driver.find_element(by=By.ID, value="password")
# agree_we = driver.find_element(by=By.ID, value="join-form-submit")


#Program Flow
#--Login
sign_we.click()


#----Create WebElements for login
time.sleep(6)
user_we = driver.find_element(by=By.ID, value="username")
password_we = driver.find_element(by=By.ID, value="password")
agree_we = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')

#--Login
user_we.send_keys(os.environ.get("USER"))
password_we.send_keys(os.environ.get("PASS"))
agree_we.click()


#--Save Company
#----Create WebElement for Save
time.sleep(5)
save_we = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
save_we.click()


#--Select Company LinkedIn Page
time.sleep(2)
company_we = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[1]/div/div[1]/div[1]/div[2]/div[2]/a')
company_we.click()


#----Follow Company
time.sleep(3)
follow_we = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[3]/div[1]/div[1]/button')
follow_we.click()

#Quit Driver
#driver.quit()


