from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup as b 
import time

class Login:
	def __init__(self, driver, username, password):
		self.driver = driver
		self.username = username
		self.password = password
	def signin(self):
		driver.get('')
