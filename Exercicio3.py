data = input ("Insira a Data no Formato DD/MM/AAAA: ")
datac = data.split ("/")
mes = int(datac[1])
meslist = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
print (f'O Dia é {datac[0]} de {meslist[mes-1]} de {datac[2]}')