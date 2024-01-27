from getMetaComps import getComps
import time
from checarLoja import checarLoja
from checarItens import checarItens
from checarStatus import checarGold,checarNivel,checarEstagio
from receitaItems import itemsList

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
        checarItens()
        checarNivel()
        checarGold()
        checarEstagio()
        time.sleep(2.5)

except KeyboardInterrupt:
    print('\nPrograma interrompido pelo usuário.')
