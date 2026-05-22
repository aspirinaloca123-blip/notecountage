#desafio contagem de notas
def notas():

    notas = int(input("Digite o valor das notas: "))


    while notas == 0:
        notas = int(input("Digite novamente: "))
 

 # O codigo pega o valor {notas} e faz as contas

    valor = 0
    resto = notas

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

       


notas()