animais = ("gato", "cachorro", "coelho", "pássaro")

primeiro_animal = animais[0]
print(f"O primeiro animal é: {primeiro_animal}")

ultimo_animal = animais[-1]
print(f"O último animal é: {ultimo_animal}")

alguns_animais = animais[1:3]
print(f"Alguns animais são: {alguns_animais}")

print("-----"*10)

livro = ("Harry Potter", "J.K. Rowling", 1997)

titulo, autor, ano = livro

print(f"Título: {titulo}")
print(f"Autor: {autor}")
print(f"Ano de lançamento: {ano}")

notas = (8.5, 9.0, 7.5, 10.0, 6.0)

primeira_nota, *outras_notas, ultima_nota = notas

print(f"\nPrimeira nota: {primeira_nota}")
print(f"As outras notas são: {outras_notas}")
print(f"Última nota: {ultima_nota}")

print("-----"*10)

cores = ["vermelho", "azul", "verde"]

segunda_cor = cores[1]
print(f"A segunda cor é: {segunda_cor}")

cores.append("amarelo")
print(f"Lista de cores após adicionar: {cores}")

cores[0] = "rosa"
print(f"Lista de cores após modificar: {cores}")