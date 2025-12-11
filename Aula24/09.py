"""

texto_de_teste = "Olá mundo!" #string para teste

#funcao p inverter texto
def inverter(texto):
    return texto[::-1]#o -1 serve para inverter a ordem da funcao

print(inverter(texto_de_teste)) #chamando a funcao

def ex3_contar_letras():
    palavra = input("Escreva uma palavra: ").lower()
    contagem = {}

    for letra in palavra:
        if letra.isalpha(): # o isalpha serve para retirAar espaços e tudo que nao seja letra!
            contagem[letra] = contagem.get(letra, 0) + 1

        print("Contagem letras:")
        for letra, quantidade in contagem.items():
            print(f"{letra} -> {contagem[letra]}")
ex3_contar_letras()#chamando a funcao

def exerc3_contar_vogais(my_str: str) -> int:
    vogais = "aeiouAEIOU"  # inclui maiúsculas para contar corretamente
    quantidade = 0  # contador

    for letra in my_str:  # passa pelas letras da frase
        if letra in vogais:  # verifica se é vogal
            quantidade += 1
    return quantidade


frase = "Tentativa um."
numero_de_vogais = exerc3_contar_vogais(frase)

print(f"A frase é: {frase}")
print(f"O número de vogais na frase é: {numero_de_vogais}")
"""

def ex4(lst):
    """
    Recebe uma lista de números inteiros e separa em duas listas:
    - A primeira com os números pares
    - A segunda com os números ímpares
    Retorna uma lista imutável com as duas listas: (pares, impares)
    """

    pares = []
    impares = []

    # Percorre a lista
    for numero in lst:
        if numero % 2 == 0:
            pares.append(numero)  #O .append constroi listas dinamicas, Se for par, adiciona na lista de pares
        else:
            impares.append(numero)  # Caso contrário, adiciona na lista de ímpares

    return pares, impares  # Retorna as duas listas (na ordem: pares, impares)


# Exemplo de teste
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Chamando função ex4
lista_pares, lista_impares = ex4(numeros)

# Imprimindo resultados
print("Números pares:", lista_pares)
print("Números ímpares:", lista_impares)

