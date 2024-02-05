from getMetaComps import getComps
import time
from checarLoja import checarLoja,checarTodaLoja
from checarItens import checarItens,checarSePodeBuildarItem
from checarStatus import checarGold,checarNivel,checarEstagio
from receitaItems import itemsList
from selecionarComp import selecionarComp
from checarCampeoes import checarCampeoes
from obterDadosAugments import obterAugments
import pyautogui
from selecionarAprimoramento import selecionarMelhorAprimoramento
from detectarEstadoDoJogo import detectarEstado
import funcoesBasicasTFT
import click



def slowRoll(nivel,comp,augments):
    carry = next((champion for champion in comp['comp'] if champion.get('carry') == True), None)
    try:
        while True:
            gameState = detectarEstado()
           
            if gameState == 'AUGMENT_SELECT':
                selecionarMelhorAprimoramento(augments)


            if gameState == 'IN_GAME':

                itens_atuais = checarItens()
                nivel_atual = checarNivel()
                gold_atual = checarGold()
                estagio_atual = checarEstagio()
                itens_buildaveis = checarSePodeBuildarItem(comp,itens_atuais)
                loja = checarLoja(comp)

                for champion in loja:
                    click.click(champion[0],champion[1])

                if nivel_atual < nivel and gold_atual >=54:
                    funcoesBasicasTFT.comprarXP()

                if nivel_atual >= nivel and gold_atual >= 52:
                    funcoesBasicasTFT.roletar()

                if itens_buildaveis and len(itens_buildaveis) > 0 : 
                    champsAtuais = checarCampeoes(campo_only=True, salvar_coordenadas=True)
                    
                    for champ in champsAtuais:
                        if champ[0] == carry['name']:
                            carryPositionX = champ[1]
                            carryPositionY = champ[2]
                            break


                    for conjunto in itens_buildaveis:
                        for item in conjunto:
                            funcoesBasicasTFT.colocarItem(item,carryPositionX,carryPositionY)

            time.sleep(1)

    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário.')
