
print('Bem Vindo a loja do Jhonatan Herman Eichemberger\n')

desconto = 0
ValorProduto = float(input('\nDigite o valor do produto: ')) #entrada de dados do valor do produto    
QtdProduto = int(input('Digite a quantidade do produto: ')) #entrada de dados da quantidade do produto


if QtdProduto >= 1000: #Se a quantidade do produto for maior ou igual a 1000, será aplicado desconto de 15% por unidade
    
    #Calculo valor sem desconto:
    valorfinalSdesc = QtdProduto * ValorProduto

    #Calculo do valor com desconto:
    desconto = ValorProduto * 0.85
    valorfinaldesc = desconto * QtdProduto

    print('\nValor sem desconto: {:.2f}'.format(valorfinalSdesc))
    print('Valor com desconto: {:.2f} R$    (desconto de 15% por unidade)\n'.format(valorfinaldesc))

elif QtdProduto > 100 and QtdProduto < 999: #Se a quantidade do produto for maior que 100 e menor que 999, será aplicado desconto de 10% por unidade
    
    #Calculo valor sem desconto:
    valorfinalSdesc = QtdProduto * ValorProduto

    #Calculo do valor com desconto:
    desconto = ValorProduto * 0.90
    valorfinaldesc = desconto * QtdProduto

    print('Valor sem desconto: {:.2f}'.format(valorfinalSdesc))
    print('Valor com desconto: {:.2f} R$    (desconto de 10% por unidade)\n'.format(valorfinaldesc))

elif QtdProduto > 10 and QtdProduto < 99: #se a quantidade do produto for maior que 10 e menor que 99, será aplicado desconto de 5% por unidade

    #Calculo valor sem desconto:
    valorfinalSdesc = QtdProduto * ValorProduto

    #Calculo do valor com desconto:
    desconto = ValorProduto * 0.95
    valorfinaldesc = desconto * QtdProduto

    print('\nValor sem desconto: {:.2f} R$'.format(valorfinalSdesc))
    print('Valor com desconto: {:.2f} R$    (desconto de 5% por unidade)\n'.format(valorfinaldesc))

else: #se a quantidade do produto for até 9, entregará apenas o valor final da compra

    valorfinal = QtdProduto * ValorProduto
    print('valor sem desconto: {:.2f} R$'.format(valorfinal))
