import cv2
import pytesseract


def lerImagem(img):
    pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'

    imagem = cv2.imread(img)
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    _, imagem_binaria = cv2.threshold(imagem_cinza, 128, 255, cv2.THRESH_BINARY)
    texto_reconhecido = pytesseract.image_to_string(imagem_binaria)
    return texto_reconhecido