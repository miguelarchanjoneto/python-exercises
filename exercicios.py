#1 - CALCULADORA SIMPLES: crie um programa que receba dois números e uma operação matemática (+, -, *, /). Realize a operação e exiba o resultado. Se o usuário inserir uma operação inválida, informe o erro e permita tentar novamente.

#REQUIREMENTS 
#1 - input 1 - primeiro número do usário 
#2 - input 2 - segundo número do usuário
#3 - input 3 - operação matemática (+, -, *, /)
#4 - se invalido print('operação inválida')
#4 - realizar a operação matemática
#5 - permitir tentar novamente
'''''
#Início
while True:
    primeiro_numero = float(input('digite o primeiro número: '))
    segundo_numero = float(input('digite o segundo número: '))
    op_mat = input('Escolha a operação: + -  * /')
    if op_mat == '+':
        soma = (primeiro_numero + segundo_numero)
        print(f'{soma}')
        jogar_novamente = input('gostaria de realizar outra operação?')
        if jogar_novamente != 'sim':
            break
    elif op_mat == '-':
        subtracao = (primeiro_numero - segundo_numero)
        print(f'{subtracao}')
        jogar_novamente = input('gostaria de realizar outra operação?')
        if jogar_novamente != 'sim':
            break
    elif op_mat == '*':
        multi = (primeiro_numero * segundo_numero)
        print(f'{multi}')
        jogar_novamente = input('gostaria de realizar outra operação?')
        if jogar_novamente != 'sim':
            break
    elif op_mat == '/':
        div = (primeiro_numero / segundo_numero)
        print(f'{div}')
        jogar_novamente = input('gostaria de realizar outra operação?')
        if jogar_novamente != 'sim':
            break
    else:
        print('operação inválida')
        jogar_novamente = input('gostaria de realizar outra operação?')
        if jogar_novamente != 'sim':
            break
    #Fim
    '''''

#2 - Jogo de Adivinhação Simples: crie um programa que sorteie um número aleatório entre 1 e 100. O usuário deve tentar adivinhar o número. O programa deve informar se o número digitado é maior ou menor que o número sorteado até o usuário acertar. Quando acertar, exiba a quantidade de tentativas realizadas.

#REQUIREMENTS 
#1 - input 1 - chute um número de 1 a 100
#2 - print se chutou acima ou print se chutou abaixo ou se acertou
#3 - quando acertar, mostrar o número de tentativas
#4 - quando acertar, print 'gostaria de jogar novamente?
#5 - if jogar novamente != sim: print ('até a próxima')
#6 - break

import random 
tentativas = 0
numero_aleatorio = random.randint (1, 100)

while True:
 try:
    chute = int(input('Chute um número de 1 a 100: ').strip())
    tentativas += 1
    if chute > numero_aleatorio:
       print('chutou acima!')
    elif chute < numero_aleatorio:
       print('chutou abaixo!')
    else:
         print(f'parabéns, você acertou o número {numero_aleatorio} após {tentativas} tentativas')
         jogar_novamente = input('gostaria de jogar novamente? sim/não:  ').strip().lower()
         if jogar_novamente == 'sim':
          tentativas = 0
          numero_aleatorio = random.randint(1, 100)
         else:
          print('obrigado por jogar, até a próxima')
          break
 except ValueError:
       print('Erro: por favor, digite um número válido')




        
























'''''
resultado = sum(primeiro_numero + segundo_numero)

#5 - perguntar se quer novamente (sim/não):
#6 - se perguntar se quer jogar novamente != sim 
#7 - 
'''''