# Primeira versão do sistema bancário - trabalha apenas com um usuário:

#String de múltiplas linhas para apresentar um menu interativo ao usuário.
menu = """ 

[d] Depositar
[s] Sacar    
[e] Extrato
[q] Sair

=> """

#Inicialização dos objetos do programa.
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#Laço infinito para a execução contínua do programa:
while True:

    opcao = input(menu)

    if opcao == "d":
        #Verificações para realizar o depósito:
        deposito = int(input("Digite o valor a ser depositado:"))

        if deposito <= 0:
            print("Valor inválido, tente novamente.")

        else:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n" # Atribuição de soma de string interpolada para o objeto.
    
    elif opcao == "s":
        
        saque = int(input("Digite o valor a ser sacado:"))

        #Verificações para realizar o saque:
        if (saque > saldo): 
            print("Valor em saldo insuficiente, tente novamente.")

        elif (numero_saques >= LIMITE_SAQUES):
            print("Quantidade de saques excede o limite, tente outra operação.")
        
        elif (saque > 500):
            print("Valor de saque acima do limite autorizado, tente novamente")
        
        elif (saque > 0):
            numero_saques += 1
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n" # Atribuição de soma de string interpolada para o objeto.
        
        else:
            print("Valor informado inválido, tente novamente.")
            
    elif opcao == "e":
       print("\n==========EXTRATO==========")
       print("Não foram realizadas movimentações." if not extrato else extrato) #If ternário.
       print(f"\nSaldo atual: R$ {saldo:.2f}") #Saldo atual.
       print("=============================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    
    