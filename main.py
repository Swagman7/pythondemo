from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

url = 'https://dashboard.stripe.com/login'
username = 'test1234'
password = '1234'

options = Options()
#options.add_argument('--headless')
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(options=options)
driver.get(url)
#driver.refresh() # 刷新
#driver.find_element(By.CLASS_NAME,'confirm').click()
usernameInput = driver.find_element(By.ID, 'email')
passwordInput = driver.find_element(By.ID, 'old-password')
usernameInput.send_keys(username)
passwordInput.send_keys(password)
driver.find_element(By.XPATH, '//*[@id="​"]/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/form/div/div/div/div[4]/div/div/div/div/div/div[1]/button').click()

time.sleep(5)

driver.get('https://dashboard.stripe.com/test/dashboard')
time.sleep(3)
statElement=driver.find_element(By.CSS_SELECTOR,'div.Padding-right--0:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)')
print(statElement)
# 关闭浏览器
#driver.quit()
