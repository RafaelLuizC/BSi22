string = input ("Insira uma String: ")
string = string.replace (" ","")
stringinv = string[::-1]
if string == stringinv:
    print ("Essa Frase é um Palidromo")
else:
    print ("Essa Frase não é um Palidromo")