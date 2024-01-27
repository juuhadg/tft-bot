from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def getComps():

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=chrome_options)


    driver.get("https://tftactics.gg/tierlist/team-comps")
    time.sleep(1)
    print("Getting comps data from tftatics.gg ...")
    comps = driver.find_elements(By.CLASS_NAME,'team-portrait')[:5]
    sTierComps = []
    print("Filtering meta comps...")
    for comp in comps:
        rank = comp.find_element(By.CLASS_NAME,'team-rank')
        if rank.text == 'S':
            name = comp.find_element(By.CLASS_NAME,'team-name-elipsis').text.split('\n')[0]
            playStyle = comp.find_element(By.CLASS_NAME,'team-playstyle').text
            team_characters = comp.find_element(By.CLASS_NAME,'team-characters')
            champions = team_characters.find_elements(By.CLASS_NAME,'characters-item.s10')
            team_comp = []

            for champion in champions:
                champion_name = champion.find_element(By.CLASS_NAME,'team-character-name')
                champion_img = champion.find_element(By.CLASS_NAME,'character-icon')
                valor_outline = champion_img.value_of_css_property("outline")
                itemsList = []

                try:
                    itemsDiv = champion.find_element(By.CLASS_NAME,'character-items')
                    items = itemsDiv.find_elements(By.CLASS_NAME,'characters-item')

                    for item in items:
                        img = item.find_element(By.TAG_NAME, 'img').get_attribute('src')
                        img_parts = img.split('/')
                        img_name = img_parts[-1]
                        item_name = img_name[:-4]
                        itemsList.append(item_name)

                except NoSuchElementException:
                    pass
                
                character = {
                    "name" : champion_name.text,
                    "itemsList" : itemsList,
                    "shopImg" : f'./images/shop/{champion_name.text}.png'
                }

                champion_classes  = champion.get_attribute("class")
                if "chosen" in champion_classes:
                    character["carry"] = True

                team_comp.append(character)


            team = {
                "name" : name,
                "playstyle" : playStyle,
                "comp" : team_comp
            }

            sTierComps.append(team)
            filtered_data = [item for item in sTierComps if 'Slow Roll' in item['playstyle']] #optional filter for only slow roll comps


    print('\n')
    for comp in sTierComps:
        print(comp)
        print('\n')
    return filtered_data

