def tratarString(string):
    string = string.strip()
    string = string.replace(' ','')
    string = string.replace('.','')
    string = string.replace('_','')
    string = string.replace('-','')
    string = string.replace(',','')
    string = string.replace('!','')
    string = string.replace('ã','a')
    string = string.replace('ç','c')
    string = string.replace('õ','o')
    string = string.replace('â','a')
    string = string.replace('é','e')
    string = string.replace('ê','e')
    string = string.replace('í','i')
    string = string.replace('ú','u')
    string = string.replace('á','a')
    string = string.lower()
    return string



def stringMatch(string1,string2, minimumMatchRate = 1):
    matches = 0
    menor = None
    string1 = tratarString(string1)
    string2 = tratarString(string2)

    if len(string1) < len(string2) : 
        menor = string1
    else :
        menor = string2
   

    for i in range(len(menor)):
        if string1[i] == string2[i] or ( i < len(string2) -1 and string1[i] == string2[i+1]):
            matches +=1
    
    matchRate = matches / len(string2)

    if matchRate >= minimumMatchRate:
        return True
    else:
        return False
    




