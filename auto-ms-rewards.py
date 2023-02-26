##########################
# auto-ms-rewards v2.0 (https://github.com/d1by/auto-ms-rewards)      
# Author: Diby M. (github.com/d1by)
# Contact me: diby#9420
# Date: February 26 2023
##########################
##########################
# Edit these fields:
# (refer to README file or instructions on github)
userdata_path = r"C:\Users\Admin\AppData\Local\Microsoft\Edge\User Data"
num_of_searches = 10
##########################

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = EdgeOptions()
userdata_dir = "--user-data-dir=" + userdata_path
options.add_argument(r'{}'.format(userdata_dir))
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Edge(options=options)

websearches = []
driver.get("https://bing.com")

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"//*[@id='trending_now_tile']/li[1]/a"))
)

for k in range(num_of_searches):
    news_title = driver.find_element(By.XPATH, f"//*[@id='trending_now_tile']/li[{k+1}]/a").get_attribute("href")
    websearches.append(news_title)

print(websearches)
#search box xpath
search_xpath = "//*[@id='sb_form_q']"

for i in range(num_of_searches):
    #finding search box
    search_form = driver.find_element(By.XPATH, search_xpath)
    #clearing field
    if(i!=0):
        search_form.send_keys(Keys.CONTROL, "a")
        search_form.send_keys(Keys.DELETE)
    #waits for search bar to finish loading
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(search_form)).click()
    search_news = websearches[i]
    search_form.send_keys(search_news)
    search_form.send_keys(Keys.ENTER)
    
    #waits for page to finish loading
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located
    )

print(f"{num_of_searches} searches complete.")

#deleting history
#opens history page
driver.get("edge://history/all")

miss=0
for j in range(num_of_searches):
    #selecting checkboxes
    hist_xpath = f"//*[@id='list-item-card-checkbox-input-{j+7}']"
    try:
        hist_del = driver.find_element(By.XPATH, hist_xpath)
        hist_del.click()
    except:
        miss+=1
        continue

#delete button
del_xpath = "//*[@id='actionDialogCardPrimaryButton']"
driver.find_element(By.XPATH, del_xpath).click()
#confirm button
del_confirm_xpath = "//*[@id='confirmModalPrimaryButton']"
driver.find_element(By.XPATH, del_confirm_xpath).click()

if(miss!=0):
    print(f"Failed to clear {miss} elements in browser history.")
time.sleep(3)
for count in range(5):
    print(f"Exiting in {5-count}...")

driver.close()
