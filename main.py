from getMetaComps import getComps
import time
from checarLoja import checarLoja
from checarItens import checarItens
from checarStatus import checarGold,checarNivel,checarEstagio
from receitaItems import itemsList
from selecionarComp import selecionarComp

print("Fetching the TFT Meta Comps...")
comps = getComps()

print('\n')


test = comps[0]
carry = next((champion for champion in test['comp'] if champion.get('carry') == True), None)
componentes_necessarios = []
for item in carry['itemsList']:
    componentes = itemsList[item.lower()]
    componentes_necessarios.append(componentes)


print('Comp Selecionada:')
print(test)
print('\n')
print(f'Componentes principais para {carry["name"]} :')
print(componentes_necessarios)
try:
    while True:
        checarLoja(test['comp'])
        itens_atuais = checarItens()
        nivel_atual = checarNivel()
        gold_atual = checarGold()
        estagio_atual = checarEstagio()
        
        if estagio_atual.strip().replace('-','') == '21':
            selecionarComp(comps,itens_atuais)

        for indice, conjunto in enumerate(componentes_necessarios):
            if all(item in itens_atuais for item in conjunto) and len(itens_atuais) > 1:
                print(f"É possível buildar {carry['itemsList'][indice]} para {carry['name']}")
        



        time.sleep(2.5)

except KeyboardInterrupt:
    print('\nPrograma interrompido pelo usuário.')
