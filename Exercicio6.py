from dataclasses import replace


print ("##### Super verificador de palíndromo #####".upper())
frase1 = input("Insira a Primeira Frase: ")
frase1 = frase1.replace (" ","")
invertida = ' '.join(palavra[::-1] for palavra in frase1.split())
print("A frase que você digitou invertida fica: ",invertida)
if frase1 == invertida:
    print ("Essa Frase é um Palidromo")
else:
    print ("Essa Frase não é um Palidromo")

#socorram me subi no onibus em marrocos