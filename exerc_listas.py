def exercicio_1():
    numeros = [12, 45, 3, 7, 89, 21, 34, 2, 66, 10]
    print("Maior:", max(numeros))
    print("Menor:", min(numeros))
    print("Soma:", sum(numeros))

def exercicio_2():
    nomes = [input("Nome: ") for _ in range(5)]
    nomes.sort()
    print("Nomes em ordem alfabética:", nomes)

def exercicio_3():
    pares = [n for n in range(1, 21) if n % 2 == 0]
    print("Números pares de 1 a 20:", pares)

def exercicio_4():
    notas = [float(n) for n in input("Insere as notas separadas por espaço: ").split()]
    media = sum(notas) / len(notas)
    print("Média:", media)

def exercicio_5():
    lista = [1, 2, 3, 2, 4, 1, 5, 3]
    sem_duplicados = []
    for item in lista:
        if item not in sem_duplicados:
            sem_duplicados.append(item)
    print("Lista sem duplicados:", sem_duplicados)

def exercicio_6():
    dias = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
    print("Primeiro dia:", dias[0])
    print("Último dia:", dias[-1])
    print("Dias do meio:", dias[1:-1])

def exercicio_7():
    numeros = (5, 2, 8, 5, 10, 3, 5, 7, 8, 1)
    print("O número 5 aparece:", numeros.count(5), "vezes")
    print("Índice do primeiro 8:", numeros.index(8))

def exercicio_8():
    tuplo = tuple(int(input("Número: ")) for _ in range(5))
    print("Em ordem inversa:", tuplo[::-1])

def exercicio_9():
    tuplo = (10, 20, 30, 40, 50)
    lista = list(tuplo)
    lista[2] = 300
    novo_tuplo = tuple(lista)
    print("Novo tuplo:", novo_tuplo)

def exercicio_10():
    alunos = {
        "Ana": 16,
        "Bruno": 14,
        "Carla": 18
    }
    media = sum(alunos.values()) / len(alunos)
    print("Média da turma:", media)

def exercicio_11():
    traducao = {}
    for _ in range(3):
        palavra = input("Palavra: ")
        traducao[palavra] = input("Tradução: ")
    pesquisa = input("Pesquisar tradução de: ")
    print("Tradução:", traducao.get(pesquisa, "Palavra não encontrada"))

def exercicio_12():
    carro = {
        "marca": "Toyota",
        "modelo": "Corolla",
        "ano": 2021
    }
    for chave, valor in carro.items():
        print(f"{chave.capitalize()}: {valor}")

def exercicio_13():
    palavra = input("Insere uma palavra: ")
    contador = {}
    for letra in palavra:
        contador[letra] = contador.get(letra, 0) + 1
    print("Frequência das letras:")
    for letra, freq in contador.items():
        print(f"{letra}: {freq}")

def exercicio_14():
    produtos = {
        "maçã": 0.5,
        "banana": 0.3,
        "pão": 1.2
    }
    total = 0
    print("Insere os produtos e quantidades (escreve 'fim' para terminar)")
    while True:
        nome = input("Produto: ")
        if nome == "fim":
            break
        if nome in produtos:
            quantidade = int(input("Quantidade: "))
            total += produtos[nome] * quantidade
        else:
            print("Produto não encontrado.")
    print("Total da compra:", round(total, 2))


def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Maior, menor e soma de 10 números")
        print("2. Pedir 5 nomes e mostrar por ordem alfabética")
        print("3. Mostrar apenas os pares de 1 a 20")
        print("4. Calcular média de uma lista de notas")
        print("5. Remover duplicados mantendo a ordem")
        print("6. Dias da semana (1º, último e meio)")
        print("7. Tuplo de 10 números (contar 5s, índice do 8)")
        print("8. Ler 5 números e mostrar ao contrário")
        print("9. Alterar valor em tuplo convertido")
        print("10. Média de notas de 3 alunos")
        print("11. Dicionário de traduções e pesquisa")
        print("12. Mostrar dados de um carro")
        print("13. Contar letras numa palavra")
        print("14. Calcular total de compras com dicionário")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            exercicio_1()
        elif escolha == "2":
            exercicio_2()
        elif escolha == "3":
            exercicio_3()
        elif escolha == "4":
            exercicio_4()
        elif escolha == "5":
            exercicio_5()
        elif escolha == "6":
            exercicio_6()
        elif escolha == "7":
            exercicio_7()
        elif escolha == "8":
            exercicio_8()
        elif escolha == "9":
            exercicio_9()
        elif escolha == "10":
            exercicio_10()
        elif escolha == "11":
            exercicio_11()
        elif escolha == "12":
            exercicio_12()
        elif escolha == "13":
            exercicio_13()
        elif escolha == "14":
            exercicio_14()
        elif escolha == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
