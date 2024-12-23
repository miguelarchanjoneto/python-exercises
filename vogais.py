#crie um programa que conte a quantidade de vogais de uma palavra fornecida pelo usuário


#Início
while True:
    palavra = input("Digite uma palavra: ").strip()
    vogais = "aeiou"
    contador = 0
    for letra in palavra:
     if letra in vogais:
      contador += 1
    print(f"a palavra {palavra} possui {contador} vogais")
    continuar = input("Deseja continuar?: ")
    if continuar != "sim":
     print("Operacao encerrada")
     break
    else:
     continue
#Fim
