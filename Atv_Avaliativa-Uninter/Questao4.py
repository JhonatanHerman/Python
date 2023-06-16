

codigo = 0 #codigo contador de pecas
pecasL = [] #lista de pecas 
cadastroD = {} #Dicionario das pecas


####################################### CADASTRO ###########################################
def cadastrarPeca(codigo): #passagem do codigo por parametro
    print('\nCADASTRO')
    print('O codigo da peça é: {}'.format(codigo))
    nome = input('Digite o nome da peça: ')
    fabricante = input('Digite o fabricante da peça: ')
    valor = input('Digite o valor da peça: ')

    cadastroD = {'codigo': codigo, #insere os valores recebidos nas variaveis para os respectivos lugares no dicionario
                 'nome': nome,
                 'fabricante': fabricante,
                 'valor': valor}
    
    pecasL.append(cadastroD.copy()) #Cria uma copia do dicionario inserindo dentro da lista
    print('---------------------------------------------')

    

################################ CONSULTAR PECA #########################################
def consultarPeca(): 
    print('\nCONSULTAR')   
    print('1 - Consultar todas as peças')
    print('2 - Consultar peças por código')
    print('3 - Consultar peças por frabricante')
    print('4 - Voltar')
    resposta2 = int(input('>> '))

    if resposta2 == 1: #se a resposta for a opção 1, vai exibir todas as peças
        print('\nTODAS AS PEÇAS CADASTRADAS')
        print('----------------------------')
        for i in pecasL:
            for key, value in i.items():
              print('{} : {}'.format(key,value))
            print('----------------------------')
    elif resposta2 == 2: #resposta = 2, pede o codigo a ser consultado e pesquisa dentro da lista
        print('\nCONSULTA POR CODIGO')
        consulCod = int(input('Digite o codigo que deseja consultar: '))
        for i in pecasL:
            if i['codigo'] == consulCod:
                for chave, valor in i.items():
                    print('{} = {}'.format(chave, valor))
    elif resposta2 == 3: #resposta = 3, pede o nome do fabricante e pesquisa dentro da lista
        print('\nCONSULTA POR FABRICANTE')
        consulFab = input('Digite o fabricante que deseja consultar: ')
        for i in pecasL:
            if i['fabricante'] == consulFab:
                for chave, valor in i.items():
                    print('{} = {}'.format(chave, valor))
    elif resposta2 == 4:
        print('voltando...')
                


################################ REMOVER PECA ############################################
def removerPeca():
    print('\nREMOVER')
    remove = int(input('Digite o codigo da peça que deseja remover: '))
    for i in pecasL:
        if i['codigo'] == remove:
            pecasL.remove(i)
        




########################################## MENU ############################################
print('BEM VINDO À BICICLETARIA DO JHONATAN HERMAN EICHEMBERGER')

while True:
    print('\n########## MENU ##########')
    print('1 - Cadastrar produtos      ')
    print('2 - Consultar peças         ')
    print('3 - Remover pecas           ')
    print('4 - Sair                    ')
    resposta = int(input('>> '))

    if resposta == 1:
        codigo += 1
        cadastrarPeca(codigo)    
    elif resposta == 2:
        consultarPeca()
    elif resposta == 3:
        removerPeca()
    else:
        print('Voce escolheu sair...')
        break