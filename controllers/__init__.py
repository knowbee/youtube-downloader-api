import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


# Function to get video links

endpoint = ""
def getVideo(link):
  options = Options()
  options.add_argument("--headless")
  options.add_argument("--disable-notifications")
  options.add_argument("--log-level=3");
  browser = webdriver.Chrome(chrome_options=options)
  browser.get(f"{endpoint}")
  start = datetime.datetime.now()
  browser.find_element_by_id("link").send_keys(f"{link}")
  browser.find_element_by_id("link").send_keys(Keys.RETURN)
  try:
    
    element = WebDriverWait(browser, 4).until(
        EC.presence_of_element_located((By.TAG_NAME, "table")))
    table = browser.find_elements_by_tag_name("table")[0]
    tbody = table.find_element_by_tag_name("tbody")
    rows = tbody.find_elements_by_tag_name("tr")
    results = []
    audios = []
    for row in rows:
      vtype = row.find_elements_by_tag_name("td")[0]
      vsize = row.find_elements_by_tag_name("td")[1]
      vlink = row.find_elements_by_tag_name("td")[2].find_element_by_class_name("btn").get_attribute('href')
      results.append({"type":  vtype.text, "size": vsize.text, "link": vlink})
    end = datetime.datetime.now()
    
    print(f"video time: {end - start}")
  finally: 
    browser.quit()
  return (results)


def getAudio(link):
  options = Options()
  options.add_argument("--headless")
  options.add_argument("--disable-gpu")
  options.add_argument("--log-level=3");
  options.add_argument("--disable-notifications");
  browser = webdriver.Chrome(chrome_options=options)
  browser.get(f"{endpoint}")
  start = datetime.datetime.now()
  browser.find_element_by_id("link").send_keys(f"{link}")
  browser.find_element_by_id("link").send_keys(Keys.RETURN)
  try:
    element = WebDriverWait(browser, 4).until(
        EC.presence_of_element_located((By.TAG_NAME, "table")))
    table2 = browser.find_elements_by_tag_name("table")[2]
    tbody2 = table2.find_element_by_tag_name("tbody")
    rows = tbody2.find_elements_by_tag_name("tr")
    audios = []
    for row in rows:
      autype = row.find_elements_by_tag_name("td")[0]
      ausize = row.find_elements_by_tag_name("td")[1]
      aulink = row.find_elements_by_tag_name("td")[2].find_element_by_class_name("btn").get_attribute('href')
      audios.append({"type":  autype.text, "size": ausize.text, "link": aulink})
    end = datetime.datetime.now()
    
    print(f"audio time: {end - start}")
    
  finally:
    browser.quit()
  return (audios)
