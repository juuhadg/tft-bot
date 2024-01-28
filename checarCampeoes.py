import os
import time
import pyautogui

def checarCampeoes():

    pasta_champions = './images/champions/'

    champions = []
    for arquivo in os.listdir(pasta_champions):
        
        caminho_imagem = os.path.join(pasta_champions, arquivo)
        elemento_encontrado = pyautogui.locateOnScreen(caminho_imagem, confidence=0.9)
                

        if elemento_encontrado:
            champ_name = arquivo.split('.')[0]
                    
            champions.append(champ_name)

    print(f'Itens Atuais : {champions}')
    return champions


