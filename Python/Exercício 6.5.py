 # Fila de banco
#Exercício 6.5- Altere o programa de forma a poder trabalhar com vários comandos digitados de uma vez só. 
ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (Pode ser AAAFFFS [3 atendimentos, 3 filas novas e uma saída]): ")
    
    for comando in operacao:
        if comando == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif comando == "F":
            ultimo += 1
            fila.append(ultimo)
        elif comando == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
