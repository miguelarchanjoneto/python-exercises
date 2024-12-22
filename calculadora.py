#1 - CALCULADORA SIMPLES: crie um programa que receba dois números e uma operação matemática (+, -, *, /). Realize a operação e exiba o resultado. Se o usuário inserir uma operação inválida, informe o erro e permita tentar novamente.

#REQUIREMENTS 
#1 - input 1 - primeiro número do usário 
#2 - input 2 - segundo número do usuário
#3 - input 3 - operação matemática (+, -, *, /)
#4 - se invalido print('operação inválida')
#4 - realizar a operação matemática
#5 - permitir tentar novamente

#Início

import sys  

while True:  #Loop principal
    try:
        primeiro_numero = float(input('Digite o primeiro número: '))
    except ValueError:
        print('Erro: Entrada inválida. Por favor, digite um número válido.')
        continue
    while True:  
        try:
            segundo_numero = float(input('Digite o segundo número: '))
            break  # Sai do subloop assim que o segundo número for válido
        except ValueError:
            print('Erro: Entrada inválida. Por favor, digite um número válido.')
                   #não precisa de continue aqui porque no subloop ele já volta sozinho
    while True:  # Loop para obter uma operação válida
        operacao = input('Escolha a operação (+, -, *, /): ').strip()

        if operacao == '+':
            print(f'Resultado: {primeiro_numero + segundo_numero}')
        elif operacao == '-':
            print(f'Resultado: {primeiro_numero - segundo_numero}')
        elif operacao == '*':
            print(f'Resultado: {primeiro_numero * segundo_numero}')
        elif operacao == '/':
            if segundo_numero == 0:
                print('Erro: Divisão por zero não permitida')
                try:
                    segundo_numero = float(input('Digite um novo número para o divisor: '))
                except ValueError:
                    print('Erro: Entrada inválida. Por favor, digite um número válido.')
                    continue  # Volta ao início para corrigir o número.
            print(f'Resultado: {primeiro_numero / segundo_numero}')
        else:
            while True:
             print('Operação inválida. Por favor, escolha uma operação válida.')
             operacao = input('Escolha a operação (+, -, *, /): ').strip()
             if operacao == '+':
              print(f'Resultado: {primeiro_numero + segundo_numero}')
             elif operacao == '-':
              print(f'Resultado: {primeiro_numero - segundo_numero}')
             elif operacao == '*':
              print(f'Resultado: {primeiro_numero * segundo_numero}')
             elif operacao == '/':
              if segundo_numero == 0:
                print('Erro: Divisão por zero não permitida')
                try:
                    segundo_numero = float(input('Digite um novo número para o divisor: '))
                except ValueError:
                    print('Erro: Entrada inválida. Por favor, digite um número válido.')
                    continue  # Volta ao início para corrigir o número.
             break # Sai do loop de operações se uma operação válida foi executada

        break # Sai do loop de operações se uma operação válida foi executada
     

    # Pergunta se o usuário deseja continuar ou encerrar o programa
    continuar = input('Deseja realizar outra operação? (sim/não): ').strip().lower()
    if continuar != 'sim':
        print('Encerrando o programa. Até a próxima!')
        sys.exit(0)



        
























'''''
resultado = sum(primeiro_numero + segundo_numero)

#5 - perguntar se quer novamente (sim/não):
#6 - se perguntar se quer jogar novamente != sim 
#7 - 
'''''