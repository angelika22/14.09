def creare_liste():
    n=int(input('n= '))
    lista_locala=[]
    for i in range(n):
        elem=input('elementul'+int(i)+'este ')
        if isinstance(elem,int)== True:
            lista_locala.append(int(elem))
        else:
            print('scrie un nr intreg')
    return lista_locala
lista1= creare_liste()
print(lista1)
