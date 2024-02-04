import win32api
import win32con
import pyautogui
import time
import click

def roletar():
    pyautogui.press('d')

def comprarXP():
    pyautogui.press('f')

def vender(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.1)
    pyautogui.press('e')

def colocarItem(x,y,item):
    try:
        item = pyautogui.locateOnScreen(f'./images/items/{item}.png')
        click.clickAndDrag(item.left,item.top,x,y)
        
    except:
        print('Nao foi Possivel colocar o item pois nao foi encontrado')
        pass

