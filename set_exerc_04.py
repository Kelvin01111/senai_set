





def gerar_conjunto(tam_conj):
    conjunto = set()

    for i in range(tam_conj):
        item = input("Informe o item: ")

        conjunto.add(item)

    return conjunto

def verificar_se_subconjunto(conjunto_1,conjunto_2):
    return conjunto_1.issubset(conjunto_2)



def main():

    tam_conj1 = int(input("Informe o tamanho do conjunto 1: "))
    tam_conj2 = int(input("Informe o tamanho do conjunto 2: "))


    print("Informe o conjunto 1: ")
    conjunto_1 = gerar_conjunto(tam_conj1)
    print("Informe o conjunto 2: ")
    conjunto_2 = gerar_conjunto(tam_conj2)

    retorno_conjunto = verificar_se_subconjunto(conjunto_1,conjunto_2)

    if(retorno_conjunto == True):
        print("Conjunto 1 é subconjunto do 2")
    else:
        print("Conjunto 1 não é subconjunto do 2")

if __name__=="__main__":
    main()