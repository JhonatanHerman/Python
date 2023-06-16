menu = 100
valor = 0

#menu do pedido
print('\nBem vindo à lanchonete do Jhonatan Herman Eichemberger')
print('***********************Cárdapio***********************')
print('| Código |             Descricao             | Valor |')
print('|   1    |             X-Burguer             | 10,00 |')
print('|   2    |              X-Bacon              | 16,00 |')
print('|   3    |               X-Egg               | 14,00 |')
print('|   4    |             X-Salada              | 13,00 |')
print('|   5    |              X-Tudo               | 20,00 |')


while menu != 0:  #enquanto o valor da variavel menu for diferente de 0. O codigo permanecerá em execução
    
    menu = int(input('\nEntre com o código desejado ou digite 0 para sair: '))
    
    if menu == 1:  #Se o codigo for igual a 1, adicionará 10.00 ao valor
        valor += 10.00
        print('Você pediu um X-burguer no valor de 10,00')
        print('\nDeseja pedir mais alguma coisa?')
        resp = int(input('1 - Sim\n0 - Não\nR:'))
        if resp == 0:  #Se resp for 0. entregará o balor final do pedido e encerrará o código
            print('Valor total do pedido: R${:.2f} '.format(valor))
            break

        
    elif menu == 2:  #Se o codigo for igual a 2, adicionará 16.00 ao valor
        valor += 16.00
        print('Você pediu um X-Bacon no valor de 13,0')
        print('\nDeseja pedir mais alguma coisa?')
        resp = int(input('1 - Sim\n0 - Não\nR:'))
        if resp == 0:  #Se resp for 0. entregará o balor final do pedido e encerrará o código
            print('Valor total do pedido: R${:.2f} '.format(valor))
            break


    elif menu == 3:  #Se o codigo for igual a 3, adicionará 14.00 ao valor
        valor += 14.00
        print('Você pediu um X-Bacon no valor de 13,0')
        print('\nDeseja pedir mais alguma coisa?')
        resp = int(input('1 - Sim\n0 - Não\nR:'))
        if resp == 0:  #Se resp for 0. entregará o balor final do pedido e encerrará o código
            print('Valor total do pedido: R${:.2f} '.format(valor))
            break
    

    elif menu == 4:  #Se o codigo for igual a 13, adicionará 13.00 ao valor
        valor += 13.00
        print('Você pediu um X-Bacon no valor de 13,0')
        print('\nDeseja pedir mais alguma coisa?')
        resp = int(input('1 - Sim\n0 - Não\nR:'))
        if resp == 0:  #Se resp for 0. entregará o balor final do pedido e encerrará o código
            print('Valor total do pedido: R${:.2f} '.format(valor))
            break


    elif menu == 5:  #Se o codigo for igual a 13, adicionará 20.00 ao valor
        valor += 20.00
        print('Você pediu um X-Bacon no valor de 13,0')
        print('\nDeseja pedir mais alguma coisa?')
        resp = int(input('1 - Sim\n0 - Não\nR:'))
        if resp == 0:  #Se resp for 0. entregará o balor final do pedido e encerrará o código
            print('Valor total do pedido: R${:.2f} '.format(valor))
            break

    else:
        #Se o código for invalido, retornará um erro e voltará ao menu
        print('Opção inválida!!')
       
