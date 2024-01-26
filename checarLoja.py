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


            
