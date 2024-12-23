# Número Primo Peça ao usuário para digitar um número inteiro positivo. Verifique se o número é primo (um número primo só é divisível por 1 e por ele mesmo). Exiba uma mensagem informando se o número é primo ou não.

#Início


while True:
    try:
        usu_n = int(input('Digite um número inteiro positivo: '))
        if usu_n < 2:
            print(f'{usu_n} não é um número primo. Números menores que 2 não são primos.')
        else:
            # Verificar se o número é primo
            eh_primo = True  # Assume que o número é primo
            for divisor in range(2, int(usu_n ** 0.5) + 1):  # Testa divisores de 2 até a raiz quadrada do número
                if usu_n % divisor == 0:
                    eh_primo = False
                    break  # Não é primo, sai do loop

            if eh_primo:
                print(f'{usu_n} é um número primo.')
            else:
                print(f'{usu_n} não é um número primo.')

    except ValueError:
        print('Erro: Por favor, digite um número inteiro positivo.')
        continue

    tentar_novamente = input('Gostaria de digitar outro número? (sim/não): ').strip().lower()
    if tentar_novamente != 'sim':
        print('Até a próxima!')
        break

          

