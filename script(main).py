import selenium
from selenium import webdriver
import time
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import gmtime, strftime
from os import system
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as chrome_options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

count = 0
driver.get("https://myanimelist.net/login.php?from=%2F")

username = ''
password = ''

driver.find_element("id", 'loginUserName').send_keys(username)
driver.find_element("id", 'login-password').send_keys(password)
time.sleep(2.5)
driver.find_element(By.XPATH, '//*[@id="gdpr-modal-bottom"]/div/div/div[2]/button').click()

driver.find_element("xpath", '//*[@id="dialog"]/tbody/tr/td/form/div/p[6]/input').click()
activearea = ''
time.sleep(3)
driver.get("https://myanimelist.net/anime.php")

for iterater1 in range(27):
    print(iterater1)
    if iterater1 == 0:
        activearea = '#'
        print(activearea)
        driver.get("https://myanimelist.net/anime.php?letter=.")
        driver.get(driver.current_url)
    elif iterater1 == 1:
        activearea = 'U'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 2:
        activearea = 'Y'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 3:
        activearea = 'T'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 4:
        activearea = 'R'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 5:
        activearea = 'E'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 6:
        activearea = 'W'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 7:
        activearea = 'Q'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 8:
        activearea = 'A'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 9:
        activearea = 'S'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 10:
        activearea = 'D'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 11:
        activearea = 'F'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 12:
        activearea = 'G'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 13:
        activearea = 'H'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 14:
        activearea = 'J'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 15:
        activearea = 'K'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 16:
        activearea = 'L'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 17:
        activearea = 'M'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 18:
        activearea = 'N'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 19:
        activearea = 'B'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 20:
        activearea = 'V'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 21:
        activearea = 'C'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 22:
        activearea = 'X'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 23:
        activearea = 'Z'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 24:
        activearea = 'I'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 25:
        activearea = 'O'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)
    elif iterater1 == 26:
        activearea = 'P'
        driver.get("https://myanimelist.net/anime.php?letter=" + activearea)
        driver.get(driver.current_url)

    for i in range(1, 41, 1):
        driver.get("https://myanimelist.net/anime.php?letter=.&show=" + str(((i-1)*50)))
        returnurl = ("https://myanimelist.net/anime.php?letter=.&show=" + str(((i-1)*50)))
        driver.get(driver.current_url)
        buttons = driver.find_elements(By.CLASS_NAME, 'title')
        print(buttons)
        count = 0
        for btn in buttons:
            buttons = driver.find_elements(By.CLASS_NAME, 'title')
            if count == 17:
                count = 18
            if buttons[count].is_displayed():
                buttons[count].click()

                print("clicked item number" + (str(count + 1)))
                count = count + 1

                driver.get(driver.current_url)
                time.sleep(2)
                addbutton = driver.find_element("id", 'showAddtolistAnime')
                addbutton.click()
                time.sleep(2)
                addbutton1 = driver.find_element("name", 'myinfo_submit')
                addbutton1.click()
                time.sleep(1)
                print("added 1 anime")
                driver.get(returnurl)
                time.sleep(2)


