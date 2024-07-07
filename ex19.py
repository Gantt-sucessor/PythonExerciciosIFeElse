# . Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma
# de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se
# o número lido não for maior do que zero, o programa termina com a mensagem “Número
# inválido”.

numero = int(input("Informe um número:"))

if (numero > 0):
    soma_digitos = sum(int(numero) for numero in str(numero)) 
    print("A soma dos dígitos de", numero, "é:", soma_digitos)
else:
    if (numero < 0):
        print("Número inválido")