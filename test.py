from selenium import webdriver

searchInput = input("Enter what you want to know about: ")

browser = webdriver.Chrome()

browser.get("https://wikipedia.org")

searchBar = browser.find_element_by_css_selector('#searchInput')
searchBar.send_keys(searchInput)
searchBar.submit()

firstPara = browser.find_element_by_css_selector('#mw-content-text > div.mw-parser-output > p:nth-child(4)')
print(firstPara.text)


