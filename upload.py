from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import random


# Variables
message = ["Have a fun, and follow 👇 @usanigthparty @night_life_usa @modelsagency999 ofr nice photography", "Have a fun, and follow 👇 @usanigthparty @night_life_usa @modelsagency999 ofr nice photography"]
message = random.choice(message)

# Post caption
text ="""
    😊
    •
    •
    •
    •
    Follow 👇
    @usanigthparty
    @night_life_usa
    @modelsagency999
    •
    •
    •
    •
"""

# Hashtags
hashtag_list=["#indoclubbers #party #sexy #clubbing #bigparty #ladysquare #woman #followme #boy #woman #usanigthparty #man #usa #indoclubbing #miami #florida", "#babyface #follow4follow #bigboobsproblems #usa #dj #man #girls #texas #california", "#dallas #hawaii #utah #nightphotography #instamoda #instaphotographer #foryou", "#Alabama #Alaska #colorado #Arkansas #nightclub #dj #bar #music #nightout #clublife", "#guam #Louisiana #nevada #Virginia #hookah #clubbing #photography #cocktail #smile #clubers #nightlife #nightclub #ladiesnight #nightparty #nightzone #sexy #kissing #hot #boobs #kis"]
hashtag=random.choice(hashtag_list)


# Random time 1
for index in range(1):
	sleep_time = (random.randint(10, 20))

# Random time 1
for index in range(1):
	sleep_time_comment = (random.randint(30, 60))

    
while True:
    # Values
    website = "https://www.instagram.com/accounts/login/?source=auth_switcher"
    username = ["usanightparty@we9designer.com", "nightlifeusa@we9designer.com", "photography@we9designer.com"]
    username = random.choice(username)
    password = "Kam125486*"


    # Share
    i = random.choice(range(1, 200))
    filename = ['/home/kamran/mega/Bots/Instagram/share-i-c/images/'+str(i)+'.jpg']


    # Open Firefox
    user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", user_agent)
    browser = webdriver.Firefox(profile)
    browser.set_window_size(360, 740)
    browser.get(website)
    time.sleep(sleep_time)

    # Username input
    user_name_elem = browser.find_element_by_xpath('/html/body/div[1]/section/main/div[1]/div/div/div/form/div[1]/div[1]/div/label/input')
    #user_name_elem = browser.find_element_by_css_selector("div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")
    user_name_elem.clear()
    user_name_elem.send_keys(username)


    # Password input
    passworword_elem = browser.find_element_by_xpath('/html/body/div[1]/section/main/div[1]/div/div/div/form/div[1]/div[2]/div/label/input')
    #passworword_elem = browser.find_element_by_css_selector('div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
    passworword_elem.clear()
    passworword_elem.send_keys(password)
    passworword_elem.send_keys(Keys.RETURN)
    time.sleep(sleep_time)
    browser.get("https://www.instagram.com")




    # UPLOAD IMAGE


    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[aria-label="New Post"]'))
        )

    finally:

        browser.find_elements_by_css_selector(
            '[aria-label="New Post"]')[0].click()

        try:
            ImageLoad = browser.find_element_by_css_selector(
                "input[type='file']")
            ImageLoad.send_keys(filename)
            pyautogui.press('esc')
        except:
            pass

        try:
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'Next')]"))
            )
        finally:

            Expand = browser.find_elements_by_xpath(
                "//*[contains(text(), 'Expand')]")

            if len(Expand) > 0:
                Expand[0].click()

            browser.find_elements_by_xpath(
                "//*[contains(text(), 'Next')]")[0].click()

            try:
                WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, "UP43G"))
                )

            finally:
                time.sleep(1)
                caption = browser.find_element_by_tag_name('textarea')
                time.sleep(2)
                caption.send_keys(text)
                pyautogui.press('enter')
                caption.send_keys(hashtag)

                button = browser.find_elements_by_class_name(
                    "UP43G")
                button[0].click()
                time.sleep(3)
    time.sleep(sleep_time_comment)





    # COMMENTING


    #Find hashtags
    hashtag_ = ["california", 'petaluma', 'hemp', 'cbdproducts', 'cbdcommunity', 'painrelief', 'brettfavre', 'cbdwellness', 'cbdmovement',  "cbd", "cannabis", "thcfree", "cannabiscommunity", "hemp", "cbdoil", "marijuana", "cbdhealth", "cannabisculture", "cbdproducts", "weedporn", "cbdlife", "sativa" "indica" ,"weedstagram" ,"hightimes", "cbdmovement", "vape", "medicalmarijuana", "cbdheals" ,"cbdcommunity", "hempoil","cbdvape","bhfyp" ]
    hashtag_=random.choice(hashtag_)
    browser.get("https://www.instagram.com/explore/tags/" +hashtag_)
    browser.set_window_size(1200, 1040)
    time.sleep(1)


    # Find images
    hashtag_image = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[2]/div[3]/a")
    hashtag_image_link = hashtag_image.get_attribute('href')
    browser.get(hashtag_image_link)
    time.sleep(sleep_time)


    # Comment
    for x in range(3):
        try:
            comment_box_elem = browser.find_element_by_css_selector(".Ypffh")
            comment_box_elem.clear()
            comment_box_elem.send_keys(message)
            comment_box_elem.send_keys(Keys.ENTER)
            print("username: ", username, " "*(50-len(username)))
        except:
            pass




    # FOLLOW    



    try:
        follow_button = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/header/div[2]/div[1]/div[2]/button').click()
    except:
        pass
    
    time.sleep(sleep_time_comment)
    

    # Close browser
    browser.close()