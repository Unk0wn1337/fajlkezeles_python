def beolvas():
    from Szemely import  Szemely
    sorokLista = []
    szemelyekLista = [] #Itt tárolom a létrehozott osztálypéldányokat
    fajlom = open("teszt.txt","r",encoding="utf-8")
    fajlom.readline()
    stirngLista = fajlom.readlines()
    index = 0
    while index < len(stirngLista):
        aktSor:str = stirngLista[index].strip() #Eltávolitsuk a sorok végéről a sortörtést
        #Béla, férfi, 23
        sorLista = aktSor.split(",")
        print(sorLista[0])
        print(sorLista[1])
        print(sorLista[2])
        szemely = Szemely(sorLista[0], sorLista[1], int(sorLista[2]))
        szemelyekLista.append(szemely)
        index+=1

    for i in range(0,len(szemelyekLista),1):
        print(f"{szemelyekLista[i].nev}, {szemelyekLista[i].nem}, {szemelyekLista[i].kor} ")