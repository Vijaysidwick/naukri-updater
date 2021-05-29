from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#from apscheduler.schedulers.blocking import BlockingScheduler
import os
import time

#sched = BlockingScheduler()
passw = "XXXX"                             # change to u r mail password
mail  = "vijaysidwick95@gmail.com"         # change to u r mail id
Resume_Headline = "B. E with 2 Years of experience in Data Analysis | Tableau | Mysql | Excel | Python | Data Visualization"


#@sched.scheduled_job('interval', minutes=3)
def executor():
    driver = webdriver.Chrome()

    driver.get("https://www.naukri.com/nlogin/logout")


    main_window = driver.current_window_handle
    element = WebDriverWait(driver,10).until(
       EC.presence_of_element_located((By.ID,"usernameField"))
    )

    inputElement = driver.find_element_by_id("usernameField")
    inputElement.send_keys(mail)

    inputElement = driver.find_element_by_id("passwordField")
    inputElement.send_keys(passw)
    inputElement.submit()
    time.sleep(2)

    element = WebDriverWait(driver,10).until(
       EC.presence_of_element_located((By.ID,"qsb-keyskill-sugg"))
    )



    Keyskill = driver.find_element_by_id("qsb-keyskill-sugg")
    Keyskill.send_keys("Data Analyst,Tableau Developer")

    Location = driver.find_element_by_id("qsb-location-sugg")
    Location.send_keys("Bangalore")

    driver.find_element_by_id("expDroope-experienceFor").click()
    driver.find_element_by_partial_link_text("2 Year").click()

    driver.find_element_by_css_selector("button.col.search.l2.btn.btn-mid").click()

    element = WebDriverWait(driver,20).until(
     EC.presence_of_element_located((By.CLASS_NAME,"desig"))
    )


    drpdown = driver.find_element_by_xpath(".//div[@class='sortBy']/div/ul/li[1]")
    driver.execute_script("arguments[0].click();", drpdown)

    time.sleep(2)
    driver.find_element_by_css_selector("div.acord_cont.open").find_element_by_partial_link_text("Bengaluru").click()

    jobs = driver.find_elements_by_class_name("desig")
    print("jobs Length : "+str(len(jobs)))

    counter = 0
    for job in jobs:
        if counter > 2:
            break
        job.click()
        element = WebDriverWait(driver,10).until(
           EC.presence_of_element_located((By.CLASS_NAME,"blueBtn"))
        )
        try:
            driver.switch_to.window(driver.window_handles[1])
            apply = driver.find_element_by_class_name("blueBtn").text
            if str(apply) == "Apply":
                driver.find_element_by_class_name("blueBtn").click()
                time.sleep(2)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#pspSubmit.lightCyanBtn"))).click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#skip_qup.skipLink"))).click()
                time.sleep(2)
                driver.close()
                counter +=1
            else:
                driver.close()
            time.sleep(2)
            driver.switch_to_window(main_window)
            
        except Exception as e:
            print(e)

    driver.get("https://www.naukri.com/mnjuser/homepage?id=")
    driver.find_element_by_partial_link_text("UPDATE PROFILE").click()
    driver.find_element_by_css_selector("span.edit.icon").click()
    headline = WebDriverWait(driver,10).until(
       EC.presence_of_element_located((By.TAG_NAME,"textarea"))
    )
    headline = driver.find_element_by_tag_name("textarea").clear()
    headline1 = driver.find_element_by_tag_name("textarea")
    headline1.send_keys(Resume_Headline)
    headline1.submit()
        
executor()

