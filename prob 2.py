def creare_liste():
    n=int(input('n= '))
    lista_locala=[]
    for i in range(n):
        elem=input('elementul'+float(i)+'este ')
        if isinstance(elem,float)== True:
            lista_locala.append(float(elem))
        else:
            print('scrie un nr intreg')
    return lista_locala
lista1= creare_liste()
print(lista1)
