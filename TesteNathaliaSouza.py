#
#Nome: Nathalia Lima de Souza
#Turma: CET104
#Data:26/09/2025
#



"""
Parte I
 Questão 1. Escreve uma função que peça ao utilizador o nome e a idade e imprima a mensagem: “Olá
 <nome>, daqui a 10 anos terás <idade+10> anos.”
 Questão 2. Escreve uma função que leia um número inteiro e verifique se é par ou ímpar
"""

#Questão 1
def ex1():
    nome = input("Digite seu nome: ") #Entrada do dado nome
    idade = int(input("Digite sua idade: ")) #Entrada do dado idade

    idade_futura = idade + 10 #Calculado a idade

    print(f"Olá {nome}, daqui a 10 anos terás {idade_futura} anos.") #imprime a mensagem pedida

#ex1() #chama a funcao, vou tentar o menu

#Questão 2

def ex2():

    numero = int(input("Digite um numero inteiro: ")) #pede o numero ao cliente
    if numero % 2 == 0: #criando a condicao
        print("O número é Par.")
    else:
        print("O número é impar.")

#ex2() #chamando a funcao

"""
Parte II
 Questão 3. Escreve uma função que peça ao utilizador três números e devolva o maior deles (sem
 usar max()).
 Questão 4. Escreve uma função que leia números até o utilizador digitar 0. No fim, mostra: a soma
 total, a média dos números introduzidos e o número de valores introduzidos.
 Questão 5. Escreve uma função que receba uma string e devolva o número de vogais existentes na
 mesma.
 Questão 6. Escreve uma função que receba uma lista de números e devolva outra lista apenas com
 os números pares.
 Questão 7. Escreve uma função que simule um menu com opções:- 1: Converter graus Celsius em
 Fahrenheit- 2: Converter graus Fahrenheit em Celsius O programa deve repetir até o
 utilizador escolher a opção de sair
"""
#Questão 3
def ex3():
    a = float(input("Digite o 1º número: "))
    b = float(input("Digite o 2º número: "))
    c = float(input("Digite o 3º número: "))

    if a >= b and a >= c: #criando a condicao
        maior = a
    elif b >= a and b >= c:
        maior = b
    else:
        maior = c

    print(f"O maior número é: {maior}")

#ex3() #sempre chamar a funcao

#Questão 4

def ex4():
    soma = 0
    contador = 0

    while True: #se colocar o true com letras minusculas nao funciona
        num = float(input("Digite um número ou zero para sair: ")) #entrada do dado
        if num == 0: break
        soma += num
        contador += 1

    if contador > 0:
        media = soma / contador
        print(f"Soma total: {soma}")
        print(f"A média é: {media}")
    else:
        print("Inválido. Tente novamente.")

#ex4()

# Questao 5

def ex5():
    # contar vogais

    texto = input("Digite uma frase: ")
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    print(f"O número de vogais é {contador}.")

#ex5()

# Questão 6

def ex6():
    numeros = [1,2,3,4,5,6,7,8,9]
    pares = []
    for numero in numeros: #condicao
        if numero % 2 == 0:
            pares.append(numero)
    print(f"Números pares da lista {pares}")

#resultado = ex6() #chamar a funcao e depois imprimir
#print(f"Números pares da lista: {resultado}")

# Questão 7

def ex7():
    while True:
        print("Menu")
        print("1 - Converter Celsius em Fahrenheit")
        print("2 - Converter Fahrenheit em Celsius")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            c = float(input("Digite os graus em Celsius: "))
            f = (c * 9) / 5 + 32
            print(f"{c}ºC = {f}ºF")

        elif opcao == "2":
            f = float(input("Digite os graus em Fahrenheit: "))
            c = (f - 32) *5/9
            print(f"{f}ºF = {c}ºC")

        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

#ex7()

"""
Parte III
 Questão 8. Escreve uma função que devolva uma lista com os primeiros n números da sequência de
 Fibonacci.
 
 
 
 Fn =
 Testa a função para n = 15.
 
 
 0,
 1,
 se n = 0,
 se n = 1,
 Fn−1 +Fn−2, se n > 1.
 Questão 9. Escreve um conjunto de funções para simular uma lista de compras:
 • Outilizador pode adicionar produtos (nome + preço)
 • Listar produtos adicionados
 • Calcular o total da compra
 Implementa a solução usando listas e/ou dicionários e organiza o código em múltiplas
 funções.
"""

# Questao 8
def ex8():
    print("Não sei nem por onde começar.")
#ex8()

# Questao 9

def ex9():
    def adicionar_produto(lista):
        nome = input("Digite o nome do produto: ")
        try:
            preco = float(input("Digite o preço do produto em euros (€): "))
            produto = {"nome": nome, "preco": preco}  # Cria um dicionário com nome e preço
            lista.append(produto)  # Adiciona o produto à lista
            print(f"Produto '{nome}' adicionado com sucesso!\n")
        except ValueError:
            print("Preço inválido. Tente novamente.\n")

    # Função para listar todos os produtos na lista
    def listar_produtos(lista):
        if not lista:  # Verifica se a lista está vazia
            print("Lista de compras vazia.\n")
            return
        print("\n📋 Lista de produtos:")
        for i, item in enumerate(lista, start=1):  # Mostra cada produto com número
            print(f"{i}. {item['nome']} - € {item['preco']:.2f}")
        print()  # Linha em branco

    # Função para calcular o total da compra
    def calcular_total(lista):
        total = sum(item["preco"] for item in lista)  # Soma todos os produtos
        print(f"💰 Total da compra: € {total:.2f}\n")

    # Função principal com o menu
    def menu_lista_compras():
        lista_compras = []  # Lista produtos

        while True:  # Loop para manter o menu a correr até o utilizador pedir p sair
            print("==== MENU LISTA DE COMPRAS ====")
            print("1 - Adicionar produto")
            print("2 - Listar produtos")
            print("3 - Calcular total")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                adicionar_produto(lista_compras)
            elif opcao == "2":
                listar_produtos(lista_compras)
            elif opcao == "3":
                calcular_total(lista_compras)
            elif opcao == "0":
                print("Saindo do programa. Até logo!")
                break  # para o if
            else:
                print("Opção inválida. Tente novamente.\n")

    menu_lista_compras()  # chama a funcao
#ex9() #chama a funcao novamente

#criando um menu para organizar, já que deu certo da ultima vez

def menu():
    while True:
        print("\nEscolha a questão que deseja rodar:")
        print("1. Questão 1")
        print("2. Questão 2")
        print("3. Questão 3")
        print("4. Questão 4")
        print("5. Questão 5")
        print("6. Questão 6")
        print("7. Questão 7")
        print("8. Questão 8")
        print("9. Questão 9")
        print("0. Sair")

        opcao = input("Digite a opçao desejada: ")

        if opcao == '1':
            ex1() #se tudo der certo executa a 1 apenas
        elif opcao == '2':
            ex2()
        elif opcao == '3':
            ex3()
        elif opcao == '4':
            ex4()
        elif opcao == '5':
            ex5()
        elif opcao == '6':
            ex6()
        elif opcao == '7':
            ex7()
        elif opcao == '8':
            ex8()
        elif opcao == '9':
            ex9()
        elif opcao == '0':
            print("Saindo... Até logo!")
        else:
            print("Opção inválida! Tente novamente.")

        continuar = input("Quer escolher outra questão? (s/n): ").strip().lower()
        if continuar != 's':
            print("Encerrando o programa. Até logo!")
            break
menu()