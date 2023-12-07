#Készíts metódust amely kiszámolja  a személyek átlag életkorát

def atlagEletKor(lista):
    osszeg = 0
    index = 0
    while index < len(lista):
        osszeg += lista[index].kor
        index+=1
    return osszeg/len(lista)

def osszesenNo(lista):
    db = 0
    index = 0
    while index < len(lista):
        if lista[index].nem == " nő":
            db+=1
        index+=1
    return db
