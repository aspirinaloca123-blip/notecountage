
# Saldo inicial do programa
saldo=0   

# A função que vai cuidar da parte de depósito do programa
def Dep_Dinheiro(saldo):

    # Esse while vai ser tipo o porteiro, o programa só funciona se ele deixar
    
    while True:
        try:
             Dep = int(input("Digite o valor que vc quer Depositar: ")) 
             break
        except ValueError:
             print("Entrada invalida, tente novamente!")

    # Aqui o Dep2 (que cuida da parte de repetição) está em verdadeiro até o usuário decidir parar
    
    Dep2 = "y" 


    while Dep2 == "y":
        
         # Essa parte faz a conta
        
         saldo = saldo + Dep
        
        # A partir daqui o programa vai perguntar ao usuário se ele quer depositar mais, se não vai só continuar  
        
         print(f" O saldo na conta atualizado é: {saldo} R$\n")
         Dep2 = str(input("deseja Depositar mais algum valor? Y/N ").strip().lower())
        
         if Dep2 == "y":
             Dep = int(input("Digite o valor que vc quer Depositar: "))   
             continue  
    
         elif Dep2 == "n":
             print("valor(es) Depositado(s) com sucesso! Encerrando atendimento. \n" )
             break
         else:
             print("Tente novamente")
             continue

    # Essa parte vai atualizar o saldo para mandar pra o programa
    return saldo






# Essa função vai cuidar da parte do saque

def SaqueNotas(saldo):

    Dep2 = "y"

    while Dep2 == "y":
        while True:
            try:
                notas = int(input("Digite o valor que vc quer sacar: "))
                break
            except ValueError:
                print("entrada inválida, tente novamente")
                continue
        

    
        valor = 0
        resto = notas
        
    # O codigo pega o valor {notas} e faz as contas
        
        if notas > saldo:
            print('saldo insuficiente! Tente novamente.')
            continue

        if notas >= 100:    
            valor = notas // 100
            resto = notas % 100
            if valor > 0:
                print(f"{valor} notas de 100")                   
     
        if resto >= 50:
            valor = resto // 50
            resto = resto % 50   
            print(f" {valor} notas de 50")
        


        if resto >= 20:
            valor = resto // 20
            resto = resto % 20
            print(f" {valor} notas de 20")
          
        
        if resto >= 10:
            valor = resto // 10
            resto = resto % 10
            print(f" {valor} notas de 10")
        
        
        if resto >= 5:
            valor = resto // 5
            resto = resto % 5
            print(f" {valor} notas de 5")
        
        
        if resto >= 2:
            valor = resto // 2
            resto = resto % 2
            print(f" {valor} notas de 2")
       
        

        if resto >= 1:
            valor = resto // 1
            resto = resto % 1
            print(f" {valor} moeda de 1")

 # Aqui a mesma coisa do deposito
        saldo = saldo - notas
        print(f" O saldo na conta atualizado é: {saldo} R$\n")
        Dep2 = str(input("deseja Sacar mais algum valor? Y/N ").strip().lower())
        
        if Dep2 == "y": 
            continue  
    
        elif Dep2 == "n":
            print("valor(es) Sacado(s) com sucesso! Encerrando atendimento \n" )
            break
        else:
            print("Tente novamente")
            continue
        


    return saldo





# Menu do caixa (aqui enquanto o usuário não digitar 4 - Sair, vai repetir)

while True:
    
    print("-" * 30)
    print("Qual o serviço que vc deseja?\n")
    print("1 - Saque")
    print("2 - Deposito")
    print("3 - Ver saldo\n")
    print("4 - Sair")
    print("-" * 30)
    
# Essa parte controla o input pra que o programa só continue se o valor for valido
    
    try:
        opcao = int(input("Digite 1, 2, 3 ou 4: "))
    except ValueError:
        print("Digite um valor válido") 
        continue


# Essa parte é o caminho a ser seguido dependendo da escolha do usuário no input "opcao"

    if opcao == 1:
         saldo = SaqueNotas(saldo)
        

    elif opcao == 2:
        saldo = Dep_Dinheiro(saldo)

    elif opcao == 3:
        print(f"Seu saldo é de: {saldo}R$")
        
    elif opcao == 4:
        print("Encerrando Programa...")
        break
    else:
        print("Digite um valor entre 1 e 4\n")
