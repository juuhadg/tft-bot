import pyautogui
import time
import os
from receitaItems import itemsList
def checarItens():

    esquerda_cima = (237, 562)
    direita_cima = (570, 662)
    esquerda_baixo = (192, 858)
    

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

    print(f'Itens Atuais : {items}')
    return items


def checarSePodeBuildarItem(comp,itens):
    carry = next((champion for champion in comp['comp'] if champion.get('carry') == True), None)
    componentes_necessarios = []
    buildaveis = []
    for item in carry['itemsList']:
        componentes = itemsList[item.lower()]
        componentes_necessarios.append(componentes)
        
            

    #checar para itens completos possiveis
    for conjunto in componentes_necessarios:
       

        if all(conjunto.count(item) <= itens.count(item) for item in conjunto):
                buildaveis.append(conjunto)
   
    return buildaveis


