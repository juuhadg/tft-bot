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

