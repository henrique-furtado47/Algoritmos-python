# Pia de louça
prato=5
pilha=list(range(1,prato+1))
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar um prato,")
    print("ou D para desempilhar. S para sair.")
    operacao = input("Operação (E, D ou S): ")
    if operacao=="E":
        prato+=1
        pilha.append(prato)
    elif operacao=="D":
        if len(pilha)>0:
            lavado=pilha.pop(-1)
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha vazia! Nenhum prato para lavar.")
    elif operacao=="S":
        break
    else:
        print("Operação inválida! Digite apenas E, D ou S!")
    

