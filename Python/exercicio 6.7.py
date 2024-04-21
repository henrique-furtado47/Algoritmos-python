#Exercicio 6.7
#Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
# Criando a pilha
pilha=[]
# Criando a expressão
expressao=input("Digite a expressão: ")
# Criando um loop para verificar a expressão
while True:
    for i in expressao:
        if i=="(":
            pilha.append(i)
        elif i==")":
            if len(pilha)>0:
                pilha.pop()
            else:
                pilha.append(i)
    break
# Verificando se a pilha está vazia
if len(pilha)==0:
    print("Os parênteses foram abertos e fechados corretamente.")
else:
    print("Os parênteses não foram abertos e fechados corretamente.")
