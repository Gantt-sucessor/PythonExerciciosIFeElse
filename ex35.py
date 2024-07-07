# Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao
# vendedor. Para calcular a comissão, considere a tabela abaixo:
# Venda mensal Comissão
# Maior ou igual a R$100.000,00 R$700,00 + 16% das vendas
# Menor que R$100.000,00 e maior ou igual a R$80.000,00 R$650,00 +14% das vendas
# Menor que R$80.000,00 e maior ou igual a R$60.000,00 R$600,00 +14% das vendas
# Menor que R$60.000,00 e maior ou igual a R$40.000,00 R$550,00 +14% das vendas
# Menor que R$40.000,00 e maior ou igual a R$20.000,00 R$500,00 +14% das vendas
# Menor que R$20.000,00 R$400,00 +14% das vendas

venda_mensal = float(input("Informe sua venda mensal:"))

if (venda_mensal >= 100000):
    comissao = 700 + (0.16 * venda_mensal)
    print("Comissão que deverá ser paga ao vendedor é:",comissao)
else:
    if (venda_mensal >= 80000 and venda_mensal < 100000):
        comissao = 650 + (0.14 * venda_mensal)
        print("Comissão que deverá ser paga ao vendedor é:",comissao)
    else:
        if (venda_mensal >= 60000 and venda_mensal < 80000):
            comissao = 600 + (0.14 * venda_mensal)
            print("Comissão que deverá ser paga ao vendedor é:",comissao)
        else:
            if (venda_mensal >= 40000 and venda_mensal < 60000):
                comissao = 550 + (0.14 * venda_mensal)
                print("Comissão que deverá ser paga ao vendedor é:",comissao)
            else: 
                if (venda_mensal >= 20000 and venda_mensal < 40000):
                    comissao = 500 + (0.14 * venda_mensal)
                    print("Comissão que deverá ser paga ao vendedor é:",comissao)
                else:
                    if (venda_mensal < 20000):
                        comissao = 400 + (0.14 * venda_mensal)
                        print("Comissão que deverá ser paga ao vendedor é:",comissao)
