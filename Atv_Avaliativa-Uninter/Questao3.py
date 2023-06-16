

def dimensoesObjeto(): #Quadro 1: dimensões vs valor
    
    while True: #input da altura
        altura = input('Digite a altura (cm): ')
        try: #analisa se o valor digitado é um valor numerico de tipo float
            altura = float(altura)
            break
        except ValueError as err:
            print("Digite um valor decimal válido")
            
    while True: #input do comprimento
        comprimento = input('Digite o comprimento (cm): ')
        try: #analisa se o valor digitado é um valor numerico de tipo float
            comprimento = float(comprimento)
            break
        except ValueError as err:
            print("Digite um valor decimal válido")

    while True: #input da largura
        largura = input('Digite a largura (cm): ')
        try: #analisa se o valor digitado é um valor numerico de tipo float
            largura = float(largura)
            break
        except ValueError as err:
            print("Digite um valor decimal válido")



    #calculo do volume
    volume = (altura * largura) * comprimento
    if volume >= 100000: #Se volume for maior que 100000: relatar erro
        print('Limite excedido. Favor entrar com novos valores')
        return dimensoesObjeto()


    elif 30000 <= volume < 100000: #Se volume maior ou igual a 30000 ou menor que 100000: retornar valor 50
        print('O valor é R$50,00')
        valor = 50.00
        return valor 
    
    elif 10000 <= volume < 30000: #Se volume maior ou igual a 10000 ou menor que 30000: retornar valor 30
        print('O valor é R$30,00')
        valor = 30.00
        return valor
    
    elif 1000 <= volume < 10000: #Se volume maior ou igual a 1000 ou menor que 10000: retornar valor 20
        print('O valor é R$20,00')
        valor = 20.00
        return valor
    
    else: #Se volume for menor ou igual a 0.1: retornar valor 10
        print('O valor é R$10,00')
        valor = 10.00
        return valor

        
def pesoObjeto(): #Quadro 2: peso vs multiplicador

    
    while True: #input do peso
        peso = input('Digite o peso do objeto (KG): ')
        try: #analisa se o valor digitado é um valor numerico de tipo float
            peso = float(peso) #tranforma valor em float e segue com o codigo
            break
        except ValueError as err:
            print("Digite um valor decimal válido")

    if peso >= 30: #Se peso maior ou igual a 30: retornar erro e voltar codigo do inicio
        print('Limite excedido. Favor entrar com novos valores')
        return pesoObjeto()

    elif 10 <= peso < 30: #se peso maior ou igual a 10 ou menor que 30: retornar multiplicador 3
        multiplicador = 3
        return multiplicador
    
    elif 1 <= peso < 10: #se peso maior ou igual a 1 ou menor que 10: retornar multiplicador 2
        multiplicador = 2
        return multiplicador
    
    elif 0.1 <= peso < 1: #se peso for maior ou igual a 0.1 ou menor que 1: retornar multiplicador 1.5
        multiplicador = 1.5
        return multiplicador
    
    else: #Se peso for menor ou igual a 0.1: retornar multiplicador 1
        multiplicador = 1
        return multiplicador
    

def rotacidades(): #Quadro 3: rota vs multiplicador
    rota = input('Selecione a rota:\n' +
                 'BR - De Brasília para o Rio de Janeiro\n' +
                 'SB - De São Paulo para Brasília\n' +
                 'SR - De São Paulo para Rio de Janeiro\n' +
                 'RB - De Rio de Janeiro até Brasília\n' +
                 'Selecione a rota: ')
    rota = rota.upper() #transforma string em maiuscula
    if rota == 'BR': #Se BR retornar 1
        mult = 1
        return mult
    
    elif rota == 'SB': #Se SB retornar 2
        mult = 2
        return mult
    
    elif rota == 'SR': #Se SR retornar 3
        mult = 3
        return mult
    
    elif rota == 'RB': #Se RB retornar 4
        mult = 4
        return mult


dimensoes = dimensoesObjeto() #Chama a função e atribui o retorno da função à variavel dimensoes
#print(dimensoes)

pesoFinal = pesoObjeto() #Chama a função e atribui o retorno da função à variavel pesoFinal
#print((pesoFinal))

rotaF = rotacidades() #Chama a função e atribui o retorno da função à variavel RotaF
#print(rotaF)

total = dimensoes * pesoFinal * rotaF #Calcula o valor total do pedido

print('\nTotal a pagar(R$): R${:.2f} (dimensões: {} * peso: {} * rota: {})'.format(total, dimensoes, pesoFinal, rotaF)) #imprime na ela o valor total
 





