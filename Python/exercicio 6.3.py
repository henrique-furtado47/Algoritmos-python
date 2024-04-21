#Exercício 6.3 - Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
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
# Criando uma lista vazia para adicionar os objetos sem repetição
L4=[]
# Criando um loop para adicionar os objetos sem repetição
for i in L3:
    if i not in L4:
        L4.append(i)
# Imprimindo as listas
print(f"Lista 1: {L} \nLista 2: {L2} \nLista 3: {L4}")
