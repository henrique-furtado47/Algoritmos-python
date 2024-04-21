#Pesquisa sequencial
L=[15, 7 ,23, 2]
p=int(input("Digite o valor a procurar: "))
x=0
achou=False
while x<len(L):
    if L[x]==p:
        achou=True
        break
    x+=1
if achou:
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")