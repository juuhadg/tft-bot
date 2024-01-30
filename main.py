from getMetaComps import getComps
import time
from checarLoja import checarLoja,checarTodaLoja
from checarItens import checarItens
from checarStatus import checarGold,checarNivel,checarEstagio
from receitaItems import itemsList
from selecionarComp import selecionarComp
from checarCampeoes import checarCampeoes
from obterDadosAugments import obterAugments
import pyautogui
from selecionarAprimoramento import selecionarMelhorAprimoramento

print("Fetching the TFT Meta Comps...")
comps = getComps()
augments = obterAugments()

print('\n')

compSelecionada = None

try:
    while True:
        if compSelecionada != None:
            checarLoja(compSelecionada['comp'])
            for indice, conjunto in enumerate(componentes_necessarios):
                if all(item in itens_atuais for item in conjunto) and len(itens_atuais) > 1:
                    print(f"É possível buildar {carry['itemsList'][indice]} para {carry['name']}")

        itens_atuais = checarItens()
        nivel_atual = checarNivel()
        gold_atual = checarGold()
        estagio_atual = checarEstagio()
        
        # decidir a comp no fim dos estagios PVE
        if estagio_atual.strip().replace('-','') == '21':

            if compSelecionada == None:
                loja = checarTodaLoja()
                campeoes = checarCampeoes()
                melhorCompAseguir = selecionarComp(comps,itens_atuais,loja,campeoes)
                compSelecionada = next((comp for comp in comps if comp.get('name') == melhorCompAseguir), None)

                carry = next((champion for champion in compSelecionada['comp'] if champion.get('carry') == True), None)
                componentes_necessarios = []

                for item in carry['itemsList']:
                    componentes = itemsList[item.lower()]
                    componentes_necessarios.append(componentes)

                print('Comp Selecionada:')
                print(compSelecionada)
                print('\n')
                print(f'Componentes principais para {carry["name"]} :')
                print(componentes_necessarios)
        
        if pyautogui.locateOnScreen('./images/misc/selecionarAprimoramento.png'):
            selecionarMelhorAprimoramento()
        
        



        time.sleep(2.5)

except KeyboardInterrupt:
    print('\nPrograma interrompido pelo usuário.')
