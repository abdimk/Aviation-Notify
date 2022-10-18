import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from requests_html import HTMLSession


URL = 'https://www.flightstats.com/v2/flight-tracker/arrivals/ADD'
session = HTMLSession()
request = session.get(URL)
request.html.render(timeout=20)

arrivals = request.html.xpath('//*[@id="__next"]/div/section/div/div[2]/div[2]', first=True)

options = Options()
options.headless = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.set_window_size(1300, 700)
start = time.time()
os.chdir(os.path.join(os.getcwd(),'images'))
i = 0
for links in arrivals.absolute_links:
    driver.get(links)
    driver.execute_script("window.scrollTo(0, 80)") 
    i = i + 1
    elements = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section/div[1]/div/div[2]/div/div[1]/div[1]')
   
    elements.screenshot(f'status{i}.png')

end = time.time() - start
sys.stdout.write(str(end))
    
    


# xpath for the map time.time()
# //*[@id="__next"]/div/section/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div