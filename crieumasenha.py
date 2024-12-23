#Validação de Senha Crie um programa que peça ao usuário para criar uma senha. Em seguida, solicite a senha novamente para login. Caso a senha esteja correta, exiba “Acesso Permitido”. Caso contrário, informe “Senha Incorreta” e permita mais duas tentativas antes de encerrar o programa.

#REQUIREMENTS
#1 solicitar uma senha ao usuário 
#2 solicitar confirmação de senha pra login
#3 se a senha estiver correta, print 'senha incorreta''
#4 permita mais duas tentativas antes de encerrar
#cd ~/programacao/repositories/python-exercises   
#5 encerrar 

#Início 

tentativa = 0  # Contador de tentativas

while tentativa < 2:  # Limite de 2 tentativas
    try:
        senha_usuario = input('Digite uma senha de 4 dígitos: ')
        confirma_senha = input('Digite a mesma senha para acessar: ')
        
        if confirma_senha != senha_usuario:
            tentativa += 1  # Incrementa o contador em caso de erro
            print(f'Senha incorreta. Você ainda tem {2 - tentativa} tentativa(s).')
        else:
            print('Acesso permitido.')
            break  # Sai do loop se a senha estiver correta
    except ValueError:
        print('Erro: Entrada inválida. Por favor, tente novamente.')
    
else:
    # Executa quando o limite de tentativas é atingido
    print('Seu limite diário de tentativas foi atingido.')

