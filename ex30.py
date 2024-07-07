# Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma
# taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Crie um programa
# em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço
# final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado
# não for válido, mostrar uma mensagem de erro

produto = float(input("Informe o preço do produto:"))
estado = str(input("Informe o estado de destino do produto:"))



if (estado == "MG"):
    print("Você escolheu o estado de Minas Gerais")
    preco_final = produto + (produto * 0.07)
    print("O preço final com imposto para esse estado fica:",preco_final)
else:
    if (estado == "SP"):
        print("Você escolher o estado de São Paulo")
        preco_final = produto + (produto * 0.12)
        print("O preço final com imposto para esse estado fica:",preco_final)
    else:
        if (estado == "RJ"):
             print("Você escolher o estado de Rio de Janeiro")
             preco_final = produto + (produto * 0.15)
             print("O preço final com imposto para esse estado fica:",preco_final)
        else:
            if (estado == "MS"):
             print("Você escolher o estado de Mato Grosso do Sul")
             preco_final = produto + (produto * 0.08)
             print("O preço final com imposto para esse estado fica:",preco_final)
            else:
                print("Estado não está listado, por favor informe um válido!")