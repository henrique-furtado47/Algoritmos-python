# Exercicio 6.2 - Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
# Criando variáveis das listas
L=[]
L2=[]
# Criando um loop para adicionar objetos nas listas
while True:
    n=input("Digite um objeto para a primeira lista (0 para sair): ")
    if n=="0":
        break
    L.append(n)
while True:
    n2=input("Digite um objeto para a segunda lista (0 para sair): ")
    if n2=="0":
        break
    L2.append(n2)
# Criando a terceira lista com a junção das duas primeiras
L3=L+L2
# Imprimindo as listas
print(f"Lista 1: {L} \nLista 2: {L2} \nLista 3: {L3}")