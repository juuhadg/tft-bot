from getMetaComps import getComps
import time
from checarLoja import checarLoja
from checarItens import checarItens

print("Fetching the TFT Meta Comps...")
comps = getComps()

print('\n')


test = comps[0]

print('Comp Selecionada:')
print(test)
try:
    while True:
        checarLoja(test['comp'])
        checarItens()
        time.sleep(2.5)

except KeyboardInterrupt:
    print('\nPrograma interrompido pelo usuário.')
