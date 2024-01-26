from PIL import ImageGrab
from lerImage import lerImagem
import time
def checarGold():
    time.sleep(2)
    esquerda_cima = (237, 562)
    direita_cima = (570, 662)
    esquerda_baixo = (192, 858)
        

    regiao_da_tela = (esquerda_cima[0], esquerda_cima[1], direita_cima[0], esquerda_baixo[1])


    imagem = ImageGrab.grab(bbox=regiao_da_tela)

    caminho_do_arquivo = "./images/temp/gold.png"
    imagem.save(caminho_do_arquivo)
    print(lerImagem(caminho_do_arquivo))

checarGold()