class ContaBanco:

  def __init__(self, nomeCliente, conta, agencia, saldo):
    self.nome = nomeCliente
    self.conta = conta
    self.agencia = agencia
    self.saldo = saldo
          
  

  ##DEPOSITAAAAAAAAAAAAAR   
  def Depositar(self, valor):
    saldaozao = self.saldo
    self.saldo = (saldaozao + valor)
    
    print("\nVoce depositou: " +str(valor) + " Reais")

  ##SACAAAAAAAAAAAAAAAAAR
  def Sacar(self, valor):
    
    if self.saldo < valor:
      print(self.nome + " voce nao pode sacar mais do que o limite")
      conta.Sacar(int(input("Quanto voce deseja sacar?  ")))
    else:
      print(self.nome + " voce sacou: R$" + str(valor))
      self.saldo -= valor


  def verificarsaldo(self):
    print("Seu saldo é: " + str(self.saldo) + ' Reais')


  lista = []
  def salvar(self):
      dados = {"nome": conta.nome, "conta": conta.conta,"agencia": conta.agencia, "saldo": conta.saldo}
      
      
      
      save = open("dados/" + dados["nome"] + dados["conta"] + ".txt", "w")
      save.write(dados["nome"])
      save.write("\n")
      save.write(str(dados["conta"]))
      save.write("\n")
      save.write(str(dados["agencia"]))
      save.write("\n")
      save.write(str(dados["saldo"]))


      save.close() 
###########################################################################################       

class Doacao:
  def __init__(self, nome, conta, agencia, saldo):
    self.agencia = agencia
    self.nome = nome
    self.conta = conta
    self.saldo = saldo

  def doar(self, valor):
    
    self.saldo -= valor
    print("\n\n" + str(self.nome) +  " doou R$" + str(valor) + " para: " ) 
    if resposta == 1:
      print("Crianças felizes.")
    elif resposta == 2:
      print("Idosos carentes")
    elif resposta == 3:
      print("Orfanato Raio de Luz")
    elif resposta == 4:
      print("Cancer Infantil")
  
  


      
    print("\nObrigado por doar!!! Voce fez a felicidade de muitas pessoas com sua doação!!!")
    


  def salvar(self):
    dados = {"nome": conta.nome, "conta": conta.conta,"agencia": conta.agencia, "saldo": conta.saldo}
    
    
    
    save = open("dados/" + dados["nome"] + dados["conta"] + ".txt", "w")
    save.write(dados["nome"])
    save.write("\n")
    save.write(str(dados["conta"]))
    save.write("\n")
    save.write(str(dados["agencia"]))
    save.write("\n")
    save.write(str(dados["saldo"]))


    save.close() 

###########################################################################################

####LISTA:
lista = []
resp = 0

print("(1) - Abrir conta")
print("(2) - deposito")
print("(3) - Saque")
print("(4) - Verificar saldo da conta")
print("(5) - finalizar")
print("\n")
print("(6) - Doar dinheiro para a caridade")

while resp != 5:

    
  resp = int(input("\n\nQual operação deseja realizar?  "))

  if resp == 1:
      conta = ContaBanco(input("Digite seu nome: "), input("\nConta: "), input("\nAgencia: "), 0)
      
      ###LISTA:
      lista.append(conta.nome)
      lista.append(conta.conta)
      lista.append(conta.agencia)
      lista.append(conta.saldo)
      
      conta.salvar()
        
        
        

  if resp == 2:
    print("\n\nInforme seus dados:")
    
    nome = input("Nome: ")
    conta = input("Conta: ")

    nome1 = open("dados/" + nome + conta + ".txt",'r').readlines()[0]
    nome1 = nome1.rstrip('\n') 

    conta1 = open("dados/" + nome + conta + ".txt",'r').readlines()[1]
    conta1 = conta1.rstrip('\n')

    agencia = open("dados/" + nome + conta + ".txt",'r').readlines()[2]
    agencia = agencia.rstrip('\n')

    saldo = open("dados/" + nome + conta + ".txt",'r').readlines()[3]
    saldo = saldo.strip('\n')
    
    saldo1 = int(saldo)
    
   
      
    conta = ContaBanco(nome1, conta1 , agencia, saldo1)
    
    
    
    conta.Depositar(int(input("Valor a ser depositado: ")))
    lista.append(conta.nome)
    lista.append(conta.conta)
    lista.append(conta.agencia)
    lista.append(conta.saldo)
    conta.salvar()
   



  if resp == 3:
    print("\n\nInforme seus dados:")
    nome = input("Nome: ")
    conta = input("Conta: ")

    
    nome1 = open("dados/" + nome + conta + ".txt",'r').readlines()[0]
    nome1 = nome1.rstrip('\n') 

    conta1 = open("dados/" + nome + conta + ".txt",'r').readlines()[1]
    conta1 = conta1.rstrip('\n')

    agencia = open("dados/" + nome + conta + ".txt",'r').readlines()[2]
    agencia = agencia.rstrip('\n')

    saldo = open("dados/" + nome + conta + ".txt",'r').readlines()[3]
    saldo = saldo.rstrip('\n')
    saldo1 = int(saldo)
      
    conta = ContaBanco(nome1, conta1 , agencia, saldo1)
    
    
    
    conta.Sacar(int(input("Quanto voce deseja sacar?  ")))
    lista.append(conta.nome)
    lista.append(conta.conta)
    lista.append(conta.agencia)
    lista.append(conta.saldo)
    conta.salvar()
      

  if resp == 4:
    print("\n\nInforme seus dados:")
    nome = input("Nome: ")
    conta = input("Conta: ")

    
    nome1 = open("dados/" + nome + conta + ".txt",'r').readlines()[0]
    nome1 = nome1.rstrip('\n') 

    conta1 = open("dados/" + nome + conta + ".txt",'r').readlines()[1]
    conta1 = conta1.rstrip('\n')

    agencia = open("dados/" + nome + conta + ".txt",'r').readlines()[2]
    agencia = agencia.rstrip('\n')

    saldo = open("dados/" + nome + conta + ".txt",'r').readlines()[3]
    saldo = saldo.rstrip('\n')
    

    conta = ContaBanco(nome1, conta1 , agencia, saldo)
    lista.append(conta.nome)
    lista.append(conta.conta)
    lista.append(conta.agencia)
    lista.append(conta.saldo)
    conta.salvar()

    print("\n\n\n")
    conta.verificarsaldo()
         

  if resp == 5:
    break


  if resp == 6:
    print("\n\nInforme seus dados:")
    nome = input("Nome: ")
    conta = input("Conta: ")

    
    nome1 = open("dados/" + nome + conta + ".txt",'r').readlines()[0]
    nome1 = nome1.rstrip('\n') 

    conta1 = open("dados/" + nome + conta + ".txt",'r').readlines()[1]
    conta1 = conta1.rstrip('\n')

    agencia = open("dados/" + nome + conta + ".txt",'r').readlines()[2]
    agencia = agencia.rstrip('\n')

    saldo = open("dados/" + nome + conta + ".txt",'r').readlines()[3]
    saldo = saldo.rstrip('\n')
    saldo1 = int(saldo)

    conta = Doacao(nome1, conta1, agencia, saldo1)
    
    
    print("\n\n(1) - Crianças Felizes")
    print("(2) - Idosos Carentes")
    print("(3) - Orfanato Raio de Luz")
    print("(4) - Cancer Infantil")

    resposta = int(input("\nPara qual estabelecimento deseja doar?  "))

    

    conta.doar(int(input("Valor a ser doado: ")))
    lista.append(conta.nome)
    lista.append(conta.conta)
    lista.append(conta.agencia)
    lista.append(conta.saldo)
    conta.salvar()