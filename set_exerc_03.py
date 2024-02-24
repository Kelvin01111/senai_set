
#3. Escreva um programa que receba uma frase do usuário e crie um set com
#   todas as letras únicas presentes na frase (ignorando espaços e letras
#   maiúsculas/minúsculas) (estude o o método replace).


def letras_unicas(frase_entrada):
    frase_entrada = frase_entrada.lower()
    frase_entrada = frase_entrada.replace(" ","")
    
    conjunto_letras_diferentes = set(frase_entrada)
    return  conjunto_letras_diferentes

  

def main():
    frase_entrada = input("Escreva uma frase: ")
    saida = letras_unicas(frase_entrada)
    print(saida)


if __name__ =="__main__":
    main()