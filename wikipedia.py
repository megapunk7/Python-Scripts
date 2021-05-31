#v1.0
#unstable
#doesnt work on every search item

import sys
from selenium import webdriver

sys.argv

searchInput = sys.argv[1]
browser = webdriver.Chrome()

browser.get("https://wikipedia.org")

searchBar = browser.find_element_by_css_selector('#searchInput')
searchBar.send_keys(searchInput)
searchBar.submit()

firstPara = browser.find_element_by_css_selector('#mw-content-text > div.mw-parser-output > p:nth-child(4)')
print(firstPara.text)

browser.quit()


