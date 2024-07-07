# Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e
# a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a
# cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão
# abaixo:

codigo = int(input("Informe o código do produto:"))
quantidade = int(input("Informe a quantidade do pedido:"))

if (codigo == 100):
    preco = 12
    preco_final = preco * quantidade
    print("O valor total a ser pago é:",preco_final)
else:
    if (codigo == 102):
        preco = 18.50
        preco_final = preco * quantidade
        print("O valor total a ser pago é:",preco_final)
    else:
        if (codigo == 103):
            preco = 25.50
            preco_final = preco * quantidade
            print("O valor total a ser pago é:",preco_final)
        else:
            if (codigo == 104):
                 preco = 17
                 preco_final = preco * quantidade
                 print("O valor total a ser pago é:",preco_final)
            else:
                if (codigo == 105):
                    preco = 9.50
                    preco_final = preco * quantidade
                    print("O valor total a ser pago é:",preco_final)
                else:
                    if (codigo == 106):
                        preco = 6
                        preco_final = preco * quantidade
                        print("O valor total a ser pago é:",preco_final)
                        
