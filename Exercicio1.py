#Esse codigo inverte o nome
nome = input ("Insira o seu nome aqui: ")
nome = (nome.upper())
nomeinv = ' '.join(palavra[::-1] for palavra in nome.split())
print ("O seu nome é: ",nome)
print ("O Seu nome invertido fica: ",nomeinv)