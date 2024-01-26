import pyautogui
import time
import os

def checarItens():

    esquerda_cima = (304, 599)
    direita_cima = (514, 606)
    esquerda_baixo = (240, 848)
    

    largura = direita_cima[0] - esquerda_cima[0]
    altura = esquerda_baixo[1] - esquerda_cima[1]

    regiao_da_tela = (esquerda_cima[0], esquerda_cima[1], largura, altura)

    pasta_items = './images/items/'

    items = []
    for arquivo in os.listdir(pasta_items):
        
        caminho_imagem = os.path.join(pasta_items, arquivo)
        elemento_encontrado = pyautogui.locateOnScreen(caminho_imagem, region=regiao_da_tela, confidence=0.7)
                

        if elemento_encontrado:
            item_name = arquivo.split('.')[0]
                    
            items.append(item_name)

    print(items)


