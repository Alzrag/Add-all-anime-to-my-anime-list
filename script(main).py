import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
count = 0
driver.get("https://myanimelist.net/login.php?from=%2F")

username = str(input('username: '))
password = str(input('password: '))

driver.find_element("id", 'loginUserName').send_keys(username)
driver.find_element("id", 'login-password').send_keys(password)
time.sleep(2.5)
driver.find_element(By.XPATH, '//*[@id="gdpr-modal-bottom"]/div/div/div[2]/button').click()

driver.find_element("xpath", '//*[@id="dialog"]/tbody/tr/td/form/div/p[6]/input').click()
activearea = ''
time.sleep(3)
driver.get("https://myanimelist.net/anime.php")

for iterater1 in range(0, 10000, 1):
    if iterater1 == 0:
        returnURL = ("https://myanimelist.net/anime.php?o=9&c%5B0%5D=a&c%5B1%5D=d&cv=2&w=" + str(iterater1 + 1))
        driver.get(returnURL)
    else:
        returnURL = ("https://myanimelist.net/anime.php?o=9&c%5B0%5D=a&c%5B1%5D=d&cv=2&w=1&show=" + str(iterater1 * 50))
        driver.get(returnURL)
    buttons = driver.find_elements(By.CLASS_NAME, 'title')
    print(buttons)
    count = 0
    isAdd = driver.find_elements(By.XPATH,"//tbody/tr/td[2]/div/a[@class='Lightbox_AddEdit button_add ga-click ml8 addtolist']")
    isAddSize = len(isAdd)
    print(isAdd)
    if len(isAdd) > 0:
        counter = 0;
        for iterater2 in range(0, isAddSize, 1):
            isAdd = driver.find_elements(By.XPATH,"//tbody/tr/td[2]/div/a[@class='Lightbox_AddEdit button_add ga-click ml8 addtolist']")
            if counter < (isAddSize):
                print(iterater2)
                print(isAdd[0].get_attribute("href"))
                idBraker = list(isAdd[0].get_attribute("href"))
                print(idBraker)
                id = (str(idBraker[61]) + str(idBraker[62]) + str(idBraker[63]) + str(idBraker[64]) + str(idBraker[65]))
                print(id)
                driver.get('https://myanimelist.net/anime/' + str(id))
                print("clicked item number" + (str(count + 1)))
                count = count + 1
                time.sleep(3)
                addbutton = driver.find_elements("id", 'showAddtolistAnime')
                if len(addbutton) > 0:
                    addbutton[0].click()
                    time.sleep(3)
                    addbutton1 = driver.find_element("name", 'myinfo_submit')
                    addbutton1.click()
                    time.sleep(1)
                    print("added 1 anime")
                    driver.get(returnURL)
                    time.sleep(2)
                else:
                    time.sleep(1)
                    print("anime was allready added")
                    driver.get(returnURL)
                    time.sleep(2)

                iterater2 = 0
                counter = counter + 1
                print(len(isAdd))
                print(counter)
                #counter to count up to total instead of iterater 2 but not a looper
