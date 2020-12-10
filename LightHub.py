import string
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

def get_link():
    randlist = string.ascii_lowercase+'1234567890'
    link = 'https://prnt.sc/'+random.choice(randlist)+random.choice(randlist)+random.choice(randlist)+random.choice(randlist)+random.choice(randlist)+random.choice(randlist)
    return link

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--disable-gpu")
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=options)
sv = input('Save Links? (Y/N): ')
if sv.lower() == 'y':
    saved = open('links.txt', 'a+')
print('\nCrawling...\n')

def crawl():
    while True:
        try:
            link = get_link()
            browser.get(link)
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/img')))
            src = browser.find_element_by_xpath('//*[@id="screenshot-image"]').get_attribute('src')
            if src != 'https://st.prntscr.com/2020/12/09/2233/img/0_173a7b_211be8ff.png':
                print(f'Link Found: {link}')
                if sv.lower() == 'y':
                    saved.write(link+'\n')
        except KeyboardInterrupt:
            print('\nQUIT | Exiting!')
            break
        except TimeoutException:
            print('\nERROR | Timeout! Retrying...\n')
            crawl()
        except NoSuchElementException:
            print('\nFATAL | No Such Element!')
            browser.quit()
            quit()
    browser.quit()
    quit()

crawl()