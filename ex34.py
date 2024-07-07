#  Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e
# escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a
# segunda tabela).

preco_antigo = float(input("Informe o preço antigo:"))

if (preco_antigo <= 50):
    preco_novo = preco_antigo + (preco_antigo * 0.05)
    print("Produto teve aumento de 5%, valor novo ficou:",preco_novo)
else:
    if (preco_antigo > 50 and preco_antigo <= 100):
        preco_novo =  preco_antigo + (preco_antigo * 0.10)
        print("Produto teve aumento de 10%, valor novo ficou:",preco_novo)
    else:
        if (preco_antigo > 100):
           preco_novo =  preco_antigo + (preco_antigo * 0.15) 
           print("Produto teve aumento de 10%, valor novo ficou:",preco_novo)
           
