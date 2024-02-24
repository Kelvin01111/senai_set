
def adicionar_em_lista(tam_lista):
    lista = []

    for i in range(tam_lista):
        item = int(input("Informe o elemento da lista: "))
        lista.append(item)

    return lista

def conjunto_elementos_comuns(lista1,lista2):
    conjunto = set()

    if not lista1 and not lista2:
        print("Listas vazias")
    else:
        conjunto = set(lista1).intersection(lista2)

    return conjunto




def main():
    tam_lista1 = int(input("Informe o tamanho da lista 1: "))
    tam_lista2 = int(input("Informe o tamanho da lista 2: "))

    print("Elementos da Primeira Lista")
    lista1 = adicionar_em_lista(tam_lista1)
    print("Elementos da Segunda Lista")
    lista2 = adicionar_em_lista(tam_lista2)

    conjunto_final = conjunto_elementos_comuns(lista1,lista2)
    if not conjunto_final:
        print("Não esxistes elementos comuns")
    else:
        print("Conjunto Final: ",conjunto_final)

    adicionar_em_lista(tam_lista1)



if __name__=="__main__":
    main()