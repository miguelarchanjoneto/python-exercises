#4 Soma de Números Pares: Peça ao usuário para digitar um número inteiro positivo. Em seguida, exiba a soma de todos os números pares de 1 até esse número

#REQUIREMENTS
#1 pedir ao usuário para digitar um número inteiro positvo
#2 somar todos os números pares de 1 até o número que o usuário escolheu
#3 exibir o resultado da soma 

#Início
# Soma de Números Pares de 1 até um número digitado pelo usuário

import sys

# Solicitar ao usuário para digitar um número inteiro positivo
while True:
    soma_pares = 0  # Variável para armazenar a soma dos números pares
    try:
        us_n = int(input('Digite um número inteiro positivo: '))
        if us_n <= 0:  # Verifica se o número é positivo
            print('Erro: Por favor, digite um número inteiro positivo.')
            continue
    except ValueError:
        print('Erro: Por favor, digite um número inteiro válido.')
        continue

    # Somar todos os números pares de 1 até o número digitado
    for numero in range(2, us_n + 1, 2):  # Itera apenas sobre números pares
        soma_pares += numero

    # Exibir o resultado final
    print(f"A soma dos números pares entre 2 e {us_n} é: {soma_pares}")
    sys.exit(0)  # Encerra o programa
        

