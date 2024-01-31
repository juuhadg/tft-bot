import pyautogui
from PIL import ImageGrab
from lerImage import lerImagem
import time
from unidecode import unidecode
from obterDadosAugments import obterAugments
from tratarString import stringMatch
import win32api
import win32con

augments = obterAugments()


def selecionarMelhorAprimoramento(augment_data):

    time.sleep(2)
    esquerda_cima1 = (408,530)
    esquerda_baixo1 = (408,564)
    direita_cima1 = (700,530)

    esquerda_cima2 = (819,530)
    esquerda_baixo2 = (819,564)
    direita_cima2 = (1106,530)

    esquerda_cima3 = (1237,530)
    esquerda_baixo3 = (1237,564)
    direita_cima3 = (1501,530)

    regiao1 = (esquerda_cima1[0], esquerda_cima1[1], direita_cima1[0], esquerda_baixo1[1])
    regiao2 = (esquerda_cima2[0], esquerda_cima2[1], direita_cima2[0], esquerda_baixo2[1])
    regiao3 = (esquerda_cima3[0], esquerda_cima3[1], direita_cima3[0], esquerda_baixo3[1])

    imagem1 = ImageGrab.grab(bbox=regiao1)
    imagem2 = ImageGrab.grab(bbox=regiao2)
    imagem3 = ImageGrab.grab(bbox=regiao3)

   
    imagem1.save('./images/temp/augment1.png')
    imagem2.save('./images/temp/augment2.png')
    imagem3.save('./images/temp/augment3.png')

    aprimoramento1 = lerImagem('./images/temp/augment1.png')
    aprimoramento2 = lerImagem('./images/temp/augment2.png')
    aprimoramento3 = lerImagem('./images/temp/augment3.png')
    print(aprimoramento1)
    print(aprimoramento2)
    print(aprimoramento3)

   
    aprimoramento1 = next((augment for augment in augment_data if stringMatch(str(aprimoramento1), augment.get('nome'), minimumMatchRate=0.6) == True), None)

    aprimoramento2 = next((augment for augment in augment_data if stringMatch(str(aprimoramento2), augment.get('nome'), minimumMatchRate=0.6) == True), None)

    aprimoramento3 = next((augment for augment in augment_data if stringMatch(str(aprimoramento3), augment.get('nome'), minimumMatchRate=0.6) == True), None)


    print('\n')
    print(aprimoramento1)
    print(aprimoramento2)
    print(aprimoramento3)

    #aprimoramento2 = next((augment for augment in augment_data if tratarString(augment.get('nome')) == tratarString(aprimoramento2)), None)

    #aprimoramento3 = next((augment for augment in augment_data if tratarString(augment.get('nome')) == tratarString(aprimoramento3)), None)
    opcoes = []
    if aprimoramento1 != None:
        aprimoramento1['index'] = 1
        opcoes.append(aprimoramento1)

    if aprimoramento2 != None:
        aprimoramento2['index'] = 2
        opcoes.append(aprimoramento2)

    if aprimoramento3 != None:
        aprimoramento3['index'] = 3
        opcoes.append(aprimoramento3)

       

   
    vencedor = None
    melhorPlacement = 8

    for opcao in opcoes:
        if opcao.get('placement') < melhorPlacement:
            melhorPlacement = opcao.get('placement')
            vencedor = opcao
        
        
        
    selecionado = pyautogui.locateOnScreen(f'./images/temp/augment{vencedor["index"]}.png')

    print(f'selecionado : {selecionado}')
    
    if selecionado is not None:
        win32api.SetCursorPos((selecionado.left,selecionado.top))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.1)  
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        print(f' aprimoramento selecionado : {vencedor["nome"]} , com colocação média de {vencedor["placement"]} , clicado em {selecionado.left} , {selecionado.top}')
   


selecionarMelhorAprimoramento(augments)


