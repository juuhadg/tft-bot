from receitaItems import itemsList
from collections import Counter

def selecionarComp(comps,itens_atuais,loja,campeoes):
    pontuacao = {}

    for champ in loja:
        champ = champ.replace("'",'')
        champ = champ.lower()

    for champ in campeoes:
        champ = champ.replace("'",'')
        champ = champ.lower()

    for comp in comps:
        temp = itens_atuais.copy()
        pontos = 0
        carry = next((champion for champion in comp['comp'] if champion.get('carry') == True), None)
        componentes_necessarios = []

        for item in carry['itemsList']:
            componentes = itemsList[item.lower()]
            componentes_necessarios.append(componentes)
        
            

        #checar para itens completos possiveis
        for conjunto in componentes_necessarios:
            possui = True

            if not all(conjunto.count(item) <= temp.count(item) for item in conjunto):
                possui = False
               
            if possui:
                pontos += 3
                componentes_necessarios.remove(conjunto)
                for itemARemover in conjunto:
                    temp.remove(itemARemover)
                

        #segunda checagem por componenentes possiveis
        componentes_restantes = []

        for conjunto in componentes_necessarios:
            for item in conjunto:
                componentes_restantes.append(item)

        for item in componentes_restantes:
            if item in temp:
                temp.remove(item)
                componentes_restantes.remove(item)
                pontos += 1

        for champion in comp['comp']:
            if champion['name'].lower() in loja:
                pontos +=  (loja.count(champion['name'])  * 0.75)
                
            if champion['name'] in campeoes:
                pontos +=  ( campeoes.count(champion['name']) * 0.75 )


        pontuacao[comp['name']] = pontos

    maiores_pontuacoes = max(pontuacao.values())
    vencedor = ''
    for chave, pontos in pontuacao.items():
        if pontos == maiores_pontuacoes:
            vencedor = chave
    print(f'Melhor Comp para seguir: {vencedor}')
    return vencedor



