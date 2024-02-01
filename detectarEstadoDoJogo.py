import pyautogui
import time

def detectarEstado():
   
    if pyautogui.locateOnScreen('./images/misc/clientMenu.png',confidence=0.8):
        state = 'CLIENT'
        return state
    
    if pyautogui.locateOnScreen('./images/misc/loadingScreenPing.png',confidence=0.8,region=(0,0,45,29),):
        state = 'LOADING_SCREEN'
        return state
    
    
    if pyautogui.locateOnScreen('./images/misc/iconeCarrossel.png',confidence=0.8):
        state = 'CARROSSEL'
        return state
    
    if pyautogui.locateOnScreen('./images/misc/selecionarAprimoramento.png',confidence=0.8):
        state = 'AUGMENT_SELECT'
        return state
    
    if not pyautogui.locateOnScreen('./images/misc/iconeCarrossel.png',confidence=0.8) and pyautogui.locateOnScreen('./images/misc/ingameMenu.png',confidence=0.8):
        state = 'IN_GAME'
        return state
    
