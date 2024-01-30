from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

def obterAugments():
   
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=chrome_options)


    driver.get("https://www.metatft.com/augments")
    definirLinguagem = "localStorage.setItem('language', 'pt_br');"
    driver.execute_script(definirLinguagem)
    time.sleep(1)
    driver.refresh()
    print("Getting Augments data from metatft...")
    time.sleep(2)
    

    tabelaAugments = driver.find_element(By.ID, 'AugmentTable')
    tabelaAugments = tabelaAugments.find_element(By. TAG_NAME,'tbody')
    augments_list = tabelaAugments.find_elements(By.TAG_NAME, 'tr')
    augments_placements = []

 
    for augment in augments_list:
        driver.execute_script("arguments[0].scrollIntoView();", augment)
        elements = augment.find_elements(By.TAG_NAME,'td')
        nome = elements[0].text
        placement = float(elements[1].text)

        data = {
            "nome" : nome,
            "placement" : placement
            }

        augments_placements.append(data)
       
    
    return augments_placements
    

