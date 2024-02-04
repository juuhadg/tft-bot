# 1- open league client 
# 2- login with the account 
# 3- click play to launch league
# 4- go to TFT and search for a match
# 5- accept the match
# 6- keep playing after a game ends
import os
import subprocess
import pyautogui
import time

def abrirLol():
    usuario = input("Usuario a Logar: ")
    senha = input("Senha: ")
    print('Abrindo Cliente..')
    dir = r"D:\Riot Games\Riot Client\RiotClientServices.exe"
    subprocess.run([dir], shell=True)
    time.sleep(8)
    pyautogui.typewrite(usuario)
    print("Realizando login...")
    pyautogui.press('TAB')
    pyautogui.typewrite(senha)
    pyautogui.press('ENTER')
    time.sleep(5)
    pyautogui.press('TAB')
    time.sleep(0.1)
    pyautogui.press('TAB')
    time.sleep(0.1)
    pyautogui.press('TAB')
    time.sleep(0.1)
    pyautogui.press('TAB')
    time.sleep(0.1)
    pyautogui.press('TAB')
    time.sleep(0.3) 
    pyautogui.press('ENTER')
    time.sleep(0.5)
    pyautogui.press('TAB')
    time.sleep(0.1)
    pyautogui.press('TAB')
    time.sleep(0.1)
    pyautogui.press('TAB')
    time.sleep(0.1)
    pyautogui.press('TAB')
    time.sleep(0.1)
    pyautogui.press('TAB')
    time.sleep(0.3)
    pyautogui.press('ENTER')
    time.sleep(35)
    print(f'Logado e Iniciado em {usuario} !')

def buscarEAceitarPartida():
    time.sleep(3)
    print('Navegando para Jogar...')
    jogar = pyautogui.locateOnScreen('./images/misc/jogar.png',confidence=0.8)
    pyautogui.click(jogar.left,jogar.top)
    time.sleep(1)
    ranqueada = pyautogui.locateOnScreen('./images/misc/normal.png',confidence=0.8)
    pyautogui.click(ranqueada.left,ranqueada.top)
    time.sleep(1)
    confirmar = pyautogui.locateOnScreen('./images/misc/confirmar.png',confidence=0.8)
    pyautogui.click(confirmar.left,confirmar.top)
    time.sleep(1)
    print('Buscando Partida')
    pyautogui.click(confirmar.left,confirmar.top)
    time.sleep(1)
    pyautogui.click(confirmar.left,confirmar.top)
    print('Na fila...')

    while True:
        try:
            if pyautogui.locateOnScreen('./images/misc/aceitarPartida.png',confidence=0.8):
                print('Partida Encontrada!')
                break
        except :
            pass




abrirLol()
buscarEAceitarPartida()