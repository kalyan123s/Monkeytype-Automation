import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pyautogui

url='https://monkeytype.com/'

driverPath="D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"

#this three lines are used for preventing automatically quit the chrome
browserOptions = webdriver.ChromeOptions()                                   
browserOptions.add_experimental_option('detach', True)                               
browserOptions.add_experimental_option('excludeSwitches', ['enable-logging'])       


chromeService=Service(driverPath)
#service=chromeService specifies that we want to use the custom ChromeDriver service whose path is in driver path
#inside the bracket we have to necessarily give argument as browserOptions so that chrome don't quit automatically
browser=webdriver.Chrome(service=chromeService, options = browserOptions)    
browser.maximize_window()
browser.get(url)


# if there is accept cookie button, click it
accept_cookie_btn = browser.find_element(By.CSS_SELECTOR, ".button.active.acceptAll")
accept_cookie_btn.click()


time.sleep(1)
# id with name 'words' will be found and assigned to the variable all_words
all_words=browser.find_element(By.ID, "words")

# all html elemnt inside the id 'words' will be parsed to soup, hence div with class 'word' also be parsed to the soup 
# since this div is also inside the id 'words'
soup=BeautifulSoup(all_words.get_attribute('innerHTML'), 'html.parser')

# time.sleep(0.5)
# Now inside that inner html file soup will find a div with class 'word' and this will be assigned to words
words=soup.find_all('div', 'word')

# for word in words:
#     print(word.text)

# first loop inside join will run then one space will be added, 2nd time again loop inside join will run then one space will be added 
# like that till all word of words get printed 
text_blocks=' '.join(word.text for word in words)


# this loop is required to write more paragraphs as monkeytype will provide more paragraphs after completing one paragraph
while True:
    try:
        pyautogui.write(text_blocks, interval=0.008)
        
        old_text_block=text_blocks
        serching_strings=old_text_block[-10:]
        
        all_words=browser.find_element(By.ID, "words")
        soup=BeautifulSoup(all_words.get_attribute('innerHTML'), 'html.parser')
        words=soup.find_all('div', 'word')
        text_blocks=' '.join(word.text for word in words)
        

        browser.implicitly_wait(10)
        text_blocks=text_blocks[text_blocks.index(serching_strings):].replace(serching_strings,'')
        time.sleep(0.9)
    except:
        time.sleep(20)
        browser.close()
        
    
