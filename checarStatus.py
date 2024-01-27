from PIL import ImageGrab
from lerImage import lerImagem
import time
def checarGold():
    esquerda_cima = (828, 857)
    direita_cima = (927, 857)
    esquerda_baixo = (818, 937)
        

    regiao_da_tela = (esquerda_cima[0], esquerda_cima[1], direita_cima[0], esquerda_baixo[1])


    imagem = ImageGrab.grab(bbox=regiao_da_tela)

    caminho_do_arquivo = "./images/temp/gold.png"
    imagem.save(caminho_do_arquivo)
    gold = lerImagem(caminho_do_arquivo)
    try:
        if gold and len(gold) > 0:
            gold = int(gold.strip()[1:])
        else:
            gold = "menos que 10"
        print(f'Gold Atual : {gold}')
        return gold
    except:
        pass




def checarNivel():
    esquerda_cima = (265, 875)
    direita_cima = (350, 875)
    esquerda_baixo = (271, 907)
        

    regiao_da_tela = (esquerda_cima[0], esquerda_cima[1], direita_cima[0], esquerda_baixo[1])


    imagem = ImageGrab.grab(bbox=regiao_da_tela)
    try:
        caminho_do_arquivo = "./images/temp/level.png"
        imagem.save(caminho_do_arquivo)
        nivel = lerImagem(caminho_do_arquivo)
        nivel = int(nivel.split('.')[1].strip())
        print(f'Nivel Atual : {nivel}')
        return nivel
    except:
        pass
    


