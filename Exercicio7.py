#Buscador de Trechos
frase = input ("Digite a Frase aqui: ").lower()
busca = input ("Digite a Parte que deseja buscar: ").lower()
posicao = frase.find (busca)
if busca in frase:
    print ("O trecho que voce busca esta na posição",posicao)
else:
    print ("Não foi possivel encontrar o trecho.")