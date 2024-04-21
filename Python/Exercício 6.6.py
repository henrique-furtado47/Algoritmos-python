# Fila de banco
# Altere o programa de forma a trabalhar com duas filas.
ultimo = 10
fila = list(range(1, ultimo + 1))
fila2= list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila 1 e {len(fila2)} clientes na fila 2")
    print(f"Fila 1 atual: {fila}, Fila 2 atual: {fila2}")
    print("Digite F para adicionar um cliente ao fim da fila 1 , G para adicionar um cliente ao fim da fila 2,")
    print("ou A para realizar o atendimento da fila 1 e B para realizar o atendimento da fila 2 . S para sair.")
    operacao = input("Operação (F, A ou S): ")
    if operacao =="A":
        if(len(fila))>0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")    
    elif operacao == "F":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == "S":
        break
    if operacao == "B":
        if(len(fila2))>0:
            atendido = fila2.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operacao == "G":
        ultimo += 1
        fila2.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, G, A, B, ou S!")
