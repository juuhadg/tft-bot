from PIL import ImageGrab
from lerImage import lerImagem
import time
import pyautogui
import win32api
import win32con
from localizacoes import localizacoesBanco,localizacoesCampo
from click import click


def checarCampeoes():
    champions = []

    for casa,localizacao in localizacoesCampo.items():
        valores = localizacao
        x = valores[0]
        y = valores[1]
        campeao = clicarELerCampeao(x,y)
        if campeao and campeao not in champions:
            champions.append(campeao)
        
        
    for casa,localizacao in localizacoesBanco.items():
        valores = localizacao
        x = valores[0]
        y = valores[1]
        campeao = clicarELerCampeao(x,y)
        if campeao :
            champions.append(campeao)
        
            
    pyautogui.rightClick(484,650)
    return champions


def clicarELerCampeao(x,y):

    click(1194,246)
   
    time.sleep(0.1)

    click(x,y)
    

    esquerda_cima = (1705,317)
    direita_cima = (1833,317)
    esquerda_baixo = (1705,342)
        

    regiao_da_tela = (esquerda_cima[0], esquerda_cima[1], direita_cima[0], esquerda_baixo[1])


    imagem = ImageGrab.grab(bbox=regiao_da_tela)
    try:
        caminho_do_arquivo = "./images/temp/champ.png"
        imagem.save(caminho_do_arquivo)
        champion = lerImagem(caminho_do_arquivo)
        if champion and len(champion) > 0 and champion != '':
            return champion.strip()
    except:
        pass


