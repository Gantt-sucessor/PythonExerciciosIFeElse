# Crie um programa de uma calculadora simples com as 4 operações básicas, apresente o menu
# de opções abaixo, leia dois números reais. Em seguida mostre o resultado da operação entre os
# dois números recebidos. Escreva uma mensagem de erro se a opção for inválida.
# Escolha a opção:
# 1- Soma de 2 números.
# 2- Diferença entre 2 números (maior pelo menor).
# 3- Produto entre 2 números.
# 4- Divisão entre 2 números (o denominador não pode ser zero).

print("1 - Soma de 2 números")
print("2 - Diferença entre 2 números")
print("3- Produto entre 2 números")
print("4- Divisão entre 2 números")
opcoes = int(input("Digite uma das opções:"))

if (opcoes == 1):
    print("Informe dois números para somar:")
    n1 = float((input("Primeiro número:")))
    n2 = float(input("Segundo número:"))
    soma = n1 + n2
    print("A soma dos dois números fica:",soma)
else:
    if (opcoes == 2):
        print("Informe dois números para subtrair:")
        n3 = float(input("Primeiro número:"))
        n4 = float(input("Segundo número:"))
        subtracao = n3 - n4
        print("A substração dos dois números fica:",subtracao)
    else:
        if (opcoes == 3):
            print("Informe dois números para multiplicar:")
            n5 = float(input("Primeiro número:"))
            n6 = float(input("Segundo número:"))
            multiplicacao = n5 * n6
            print("A multiplicação dois dois números fica:",multiplicacao)
        else:
            if (opcoes == 4):
                print("Informe dois números para dividir:")
                n7 = float(input("Primeiro número:"))
                n8 = float(input("Segundo número:"))
                divisao = n7/n8
                print("A divisão dos dois números é:",divisao)
            else:
                if (opcoes != 1,2,3,4):
                    print("O valor é inválido")
