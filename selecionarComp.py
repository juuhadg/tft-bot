from receitaItems import itemsList

def selecionarComp(comps,itens_atuais):
    pontuacao = {}

    for comp in comps:
        temp = itens_atuais.copy()
        pontos = 0
        carry = next((champion for champion in comp['comp'] if champion.get('carry') == True), None)
        componentes_necessarios = []

        for item in carry['itemsList']:
            componentes = itemsList[item.lower()]
            componentes_necessarios.append(componentes[0])
            componentes_necessarios.append(componentes[1])

        for item in temp:
            if item in componentes_necessarios:
                pontos += 1
                
                temp.remove(item)

        pontuacao[comp['name']] = pontos

    print(pontuacao)

# mock =>
compes = [{'name': 'Punk Rapidfire', 'playstyle': 'Slow Roll (6)', 'comp': [{'name': 'Jinx', 'itemsList': ['Deathblade', 'GuinsoosRageblade', 'LastWhisper'], 'shopImg': './images/shop/Jinx.png', 'carry': True}, {'name': 'Vi', 'itemsList': [], 'shopImg': './images/shop/Vi.png'}, {'name': 'Pantheon', 'itemsList': ['BrambleVest', 'DragonsClaw', 'WarmogsArmor'], 'shopImg': './images/shop/Pantheon.png'}, {'name': 'Twitch', 'itemsList': [], 'shopImg': './images/shop/Twitch.png'}, {'name': 'Amumu', 'itemsList': [], 'shopImg': './images/shop/Amumu.png'}, {'name': 'Neeko', 'itemsList': [], 'shopImg': './images/shop/Neeko.png'}, {'name': 'Vex', 'itemsList': [], 'shopImg': './images/shop/Vex.png'}, {'name': 'Thresh', 'itemsList': [], 'shopImg': './images/shop/Thresh.png'}]},


{'name': 'Big Shots', 'playstyle': 'Fast 8', 'comp': [{'name': 'Bard', 'itemsList': [], 'shopImg': './images/shop/Bard.png'}, {'name': 'Miss Fortune', 'itemsList': [], 'shopImg': './images/shop/Miss Fortune.png'}, {'name': 'Sett', 'itemsList': [], 'shopImg': './images/shop/Sett.png'}, {'name': 'Ezreal', 'itemsList': ['BlueBuff', 'InfinityEdge', 'RedBuff'], 'shopImg': './images/shop/Ezreal.png', 'carry': True}, {'name': 'Thresh', 'itemsList': [], 'shopImg': './images/shop/Thresh.png'}, {'name': 'Jhin', 'itemsList': [], 'shopImg': './images/shop/Jhin.png'}, {'name': 'Illaoi', 'itemsList': ['BrambleVest', 'DragonsClaw', 'WarmogsArmor'], 'shopImg': './images/shop/Illaoi.png'}, {'name': 'Yorick', 'itemsList': [], 'shopImg': './images/shop/Yorick.png'}]},


{'name': 'Country Moshers', 'playstyle': 'Slow Roll (7)', 'comp': [{'name': 'Tahm Kench', 'itemsList': [], 'shopImg': './images/shop/Tahm Kench.png'}, {'name': 'Amumu', 'itemsList': [], 'shopImg': './images/shop/Amumu.png'}, {'name': 'Samira', 'itemsList': ['GiantSlayer', 'InfinityEdge', 'LastWhisper'], 'shopImg': './images/shop/Samira.png', 'carry': True}, {'name': 'Sett', 'itemsList': [], 'shopImg': './images/shop/Sett.png'}, {'name': 'Urgot', 'itemsList': ['Bloodthirster', 'SteraksGage', 'TitansResolve'], 'shopImg': './images/shop/Urgot.png'}, {'name': 'Vex', 'itemsList': [], 'shopImg': './images/shop/Vex.png'}, {'name': 'Thresh', 'itemsList': [], 'shopImg': './images/shop/Thresh.png'}, {'name': 'Illaoi', 'itemsList': [], 'shopImg': './images/shop/Illaoi.png'}]},


{'name': 'Emo Executioners', 'playstyle': 'Slow Roll (7)', 'comp': [{'name': 'Pantheon', 'itemsList': [], 'shopImg': './images/shop/Pantheon.png'}, {'name': 'Twitch', 'itemsList': [], 'shopImg': './images/shop/Twitch.png'}, {'name': 'Amumu', 'itemsList': ['BrambleVest', 'DragonsClaw', 'WarmogsArmor'], 'shopImg': './images/shop/Amumu.png'}, {'name': 'Samira', 'itemsList': [], 'shopImg': './images/shop/Samira.png'}, {'name': 'Vex', 'itemsList': ['ArchangelsStaff', 'JeweledGauntlet', 'SpearofShojin'], 'shopImg': './images/shop/Vex.png', 'carry': True}, {'name': 'Akali K/DA', 'itemsList': [], 'shopImg': './images/shop/Akali K/DA.png'}, {'name': 'Karthus', 'itemsList': [], 'shopImg': './images/shop/Karthus.png'}]}
,

{'name': 'K/DA', 'playstyle': 'Standard', 'comp': [{'name': 'Kennen', 'itemsList': [], 'shopImg': './images/shop/Kennen.png'}, {'name': 'Lillia', 'itemsList': [], 'shopImg': './images/shop/Lillia.png'}, {'name': 'Kaisa', 'itemsList': [], 'shopImg': './images/shop/Kaisa.png'}, {'name': 'Seraphine', 'itemsList': [], 'shopImg': './images/shop/Seraphine.png'}, {'name': 'Ekko', 'itemsList': [], 'shopImg': './images/shop/Ekko.png'}, {'name': 'Neeko', 'itemsList': ['GargoyleStoneplate', 'WarmogsArmor'], 'shopImg': './images/shop/Neeko.png'}, {'name': 'Ahri', 'itemsList': ['BlueBuff', 'NashorsTooth'], 'shopImg': './images/shop/Ahri.png', 'carry': True}, {'name': 'Akali K/DA', 'itemsList': ['Bloodthirster', 'TitansResolve'], 'shopImg': './images/shop/Akali K/DA.png'}]}]

items = ['RecurveBow','BfSword','GiantsBelt']





selecionarComp(compes,items)