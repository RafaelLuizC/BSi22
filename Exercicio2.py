#Esse Codigo imprime o nome na vertical em escadinha
nome = input("Digite o Nome do usuario: ").upper()
nomes = len(nome)

for x in range (0,nomes+1):
    print (nome[0:x:1])
