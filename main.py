from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login
import getpages

username = 'python_bot_oop'
password = 'pythonbotoop'
driver = 0
refs = ['/meme_coding/','/debugging_life/','/agemo_vectors/']
max_likes = 350
max_follows = 50

def main():
    global driver
    print('running script..')
    driver = webdriver.Chrome('C://Users/vranda/Desktop/chromedriver.exe')
    l = login.Login(driver, username, password)
    l.signin()
    print('signin done')
    time.sleep(3)
    gp = getpages.Getpages(driver)
    print('getting followers')
    #refs = gp.get_followers()
    time.sleep(3)
    print('follower count:')
    print(gp.get_num_flw())
    time.sleep(30)
    print('Bot')
    run_bot(refs, driver, gp)
    
def run_bot(refs, driver, gp):
    print('run_bot function')
    #print(len(gp.get_followers()))
    print('accounts targeted')
#    t = time.time()
    L = 0 #pages liked
    F = 0 #pages followed
    for r in refs:
        driver.get('https://www.instagram.com' + r)
        time.sleep(2)
        if gp.get_num_flw() < 3000:
            if gp.is_public():
                print('public account')
                print('current likes: ' + str(L))
                if L < max_likes:
                    try:
                        gp.follow_page()
                        time.sleep(3)
                        print('page followed successfully')
                        F += 1
                        print('Post like')
                        gp.like_post()
                        time.sleep(30)
                        L += 1
                        print("Total Likes: " + str(L))
                        print("POST LIKED")
                    # except:
                    #     print('could not like..lets follow instead')
                        # try:
                        
                    except:
                            # try:
                            #     gp.followed()
                            #     time.sleep(3)
                            #     # print('Already Following')
                            # except:
                        print('Could not Follow or Already Following')
                else:
                    print('number of likes are greater than max likes')
                    time.sleep(36)
            else:
                print('account is private')
                print('current follows: ' + str(F))
                if F < max_follows:
                    time.sleep(2)
                    try:
                        gp.follow_page()
                        print('page followed successfully')
                        F += 1
                    except:
                        print('could not follow')
                    
                else:
                    print('number of followers are greater than maximum followers')
                    time.sleep(36)
        else:
            print('too many followers')

if __name__ == '__main__':
    main()    
