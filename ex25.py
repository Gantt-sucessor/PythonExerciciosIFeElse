# Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas
# (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois
# valores numéricos e realiza a operação, mostrando o resultado e finalizando o programa.

print("Soma: 1")
print("Subtração: 2")
print("Multiplicação: 3")
print("Divisão: 4")
opcões = int(input("Digite uma das opções:"))

if (opcões == 1):
    print("Informe dois números para somar:")
    n1 = int((input("Primeiro número:")))
    n2 = int(input("Segundo número:"))
    soma = n1 + n2
    print("A soma dos dois números fica:",soma)
else:
    if (opcões == 2):
        print("Informe dois números para subtrair:")
        n3 = int(input("Primeiro número:"))
        n4 = int(input("Segundo número:"))
        subtracao = n3 - n4
        print("A substração dos dois números fica:",subtracao)
    else:
        if (opcões == 3):
            print("Informe dois números para multiplicar:")
            n5 = int(input("Primeiro número:"))
            n6 = int(input("Segundo número:"))
            multiplicacao = n5 * n6
            print("A multiplicação dois dois números fica:",multiplicacao)
        else:
            if (opcões == 4):
                print("Informe dois números para dividir:")
                n7 = int(input("Primeiro número:"))
                n8 = int(input("Segundo número:"))
                divisao = n7/n8
                print("A divisão dos dois números é:",divisao)
        
