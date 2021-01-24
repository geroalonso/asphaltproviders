from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd

names = []
member_numbers = []
page = 1

def crawler(page):
	url = "https://www.floridaridesonus.org/members//?Page="+ str(page)
	chrome_options = Options()  
	chrome_options.add_argument("--headless") 
	chrome_options.add_argument("user-agent= G.Alonso Scraper contact me if my bot is behaving intrusively: geronimoalonso@icloud.com")
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) #set the search engine
	driver.get(url)

	members = driver.find_elements_by_xpath("//strong[contains(@class, 'name')]")
	
	for member in members:
		name = member.text
		names.append(name)


	
	member_phones = driver.find_elements_by_xpath("//div[@class = 'member']//div[@class = 'social-icons']/a[1]")
	for phone in member_phones:
		number = phone.get_attribute("data-original-title")
		member_numbers.append(number)

	driver.quit()




for i in range(1,8):
	crawler(i)

dic = dict(zip(names, member_numbers))	
print(dic)

