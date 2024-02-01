import os
import pyautogui
import time


def checarLoja(comp):
    esquerda_cima = (475, 921)
    direita_cima = (1481, 922)
    esquerda_baixo = (474, 1070)
   

    largura = direita_cima[0] - esquerda_cima[0]

    altura = esquerda_baixo[1] - esquerda_cima[1]

    regiao_da_tela = (esquerda_cima[0], esquerda_cima[1], largura, altura)


    for champion in comp:

        
        elemento_encontrado = pyautogui.locateOnScreen(champion['shopImg'], region=regiao_da_tela,confidence=0.8)

                    
        if elemento_encontrado:
            print(f"{champion['name']} na Loja !")


def checarTodaLoja():
    time.sleep(1)
    esquerda_cima = (475, 921)
    direita_cima = (1481, 922)
    esquerda_baixo = (474, 1070)
   

    largura = direita_cima[0] - esquerda_cima[0]

    altura = esquerda_baixo[1] - esquerda_cima[1]

    regiao_da_tela = (esquerda_cima[0], esquerda_cima[1], largura, altura)


    pasta_loja = './images/shop/'

    champions = []

    for arquivo in os.listdir(pasta_loja):
        
        caminho_imagem = os.path.join(pasta_loja, arquivo)
        elemento_encontrado = pyautogui.locateOnScreen(caminho_imagem, region=regiao_da_tela, confidence=0.8)
                

        if elemento_encontrado:
            champion_name = arquivo.split('.')[0]   
            champions.append(champion_name.lower())

    
    return champions

print(checarTodaLoja())