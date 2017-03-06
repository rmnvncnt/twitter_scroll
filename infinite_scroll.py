from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time, random, requests

def get_tweets(account, lang):
    
    # initate browser
    url = 'https://twitter.com/{}?lang={}'.format(account, lang)
    browser = webdriver.Firefox()
    browser.get(url)
    elements = browser.find_element_by_tag_name('html')
    tzero = time.time()
    
    # Scrolling loop
    running = True
    previous_page = 0
    while running:
        elements.send_keys(Keys.END)
        time.sleep(random.randrange(1, 5, 1))
        current_page = len(browser.page_source)
        if previous_page == current_page:
            running = False
        previous_page = current_page
        print ("Scrolling...")

    # saving
    with open('source.html', 'w') as file:
        file.write(browser.page_source)
        print ("Saving...")

    # closing
    end = time.time() - tzero