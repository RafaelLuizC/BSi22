frase = input("Insira a Frase Aqui: ").upper()
lista = list (frase)

for x in lista:
    if (frase.count(x) != 0):
        print (f'A Letra "{x}" apareceu {frase.count(x)} x')
        frase = frase.replace (x,"")