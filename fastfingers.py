from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

# Initialize
link = 'https://10fastfingers.com/multiplayer'
browser = webdriver.Chrome(r'CHROMEDRIVER PATH') # https://sites.google.com/a/chromium.org/chromedriver/
browser.get(link)

def start():

    browser.switch_to.default_content()
    
    browser.switch_to.frame(0)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    wordlist = soup.find(class_='place')
    wordlist = re.findall(">([a-z]*)</", str(wordlist))

    input_box = browser.find_element_by_xpath('//*[@id="game"]/div[3]/div[2]/div[2]/div[1]/input')

    start = input('> Press ENTER when the game started ')
    for word in wordlist:
        try:
            input_box.send_keys(word)
            input_box.send_keys(Keys.SPACE)
        except:
            print('You won!')

browser.switch_to.frame(0)
