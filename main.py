from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup as b 
import time

driver = 0
def main():
	global driver
	print('running script..')
	driver = webdriver.Chrome('C://Users/vranda/Desktop/chromedriver.exe')

if __name__ =='__main__':
	main()
