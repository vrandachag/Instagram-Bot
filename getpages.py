from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Getpages:
    def __init__(self, driver):  
        self.driver = driver
        self.driver.get('https://www.instagram.com/python.learning')
        self.hrefs = []

    def get_num_flw(self):
        flw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
        time.sleep(3)
        sflw = b(flw.get_attribute('innerHTML'), 'html.parser')
        time.sleep(3)
        followers = sflw.findAll('span', {'class':'g47SY'})
        f = followers[1].getText().replace(',', '')
        if 'k' in f:
            f = float(f[:-1]) * 10**3
            return f
        elif 'm' in f:
            f = float(f[:-1]) * 10**6
            return f
        else:
            return float(f)

    def get_followers(self):
        time.sleep(2)
        flw_btn = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span')))
        flw_btn.click()                                                                                 
        time.sleep(3)
        self.popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div')))
        for h in range(11):
            print('for loop h')
            time.sleep(1)
            print('scrolling')
            print(h)
            print('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)))
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)), self.popup)
        #    if h == 5:
        #        break
        time.sleep(30)
        for i in range(40):
            print('for loop i')
            time.sleep(2)
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', self.popup)
        self.popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/ul/div/li[6]')))
        b_popup = b(self.popup.get_attribute('innerHTML'), 'html.parser')
        for p in b_popup.findAll('li', {'class': 'wo9IH'}):
            print("for loop p")
            try:
                hlink = p.find_all('a')[0]['href']
                print("hlink:",hlink)
                if 'div' in hlink:
                    print('div found not adding to list')
                else:
                    self.hrefs.append(hlink)
            except:
                pass
        return self.hrefs
            
    def is_public(self):
        try:
            astate = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'rkEop')))
            if astate.text == 'This Account is Private':
                return False
            else:
                return True
        except:
            return True

    def like_post(self):
        post = self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a > div')
        # html = post.get_attribute('innerHTML')
        # h = b(html, 'html.parser')
        # href = h.a['href']
        post.click()
        # self.driver.get('https://www.instagram.com' + href)
        #self.driver.get('https://www.instagram.com/p/CGKel1wHewF/')
        like_btn = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')))
        like_btn.click()
        print('Post liked')
        time.sleep(30)

    def follow_page(self):
        follow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')))
        # message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div[1]/div/button')))
        f_text = follow.text
        # m_text = message.text
        if f_text == 'Follow' or f_text == 'Follow Back':
            follow.click()
        # elif m_text == 'Message':
        #     print('Already Following')
        time.sleep(1)
