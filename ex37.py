# O custo ao consumidor de um carro novo e a soma do custo de fábrica, da comissão do
# distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica,
# de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.

custo_fabrica = float(input("Informe o custo de fabrica:"))

if (custo_fabrica <= 12000):
    comissao = custo_fabrica * 0.05
    print("A comissão do distribuidor fica:",comissao)
    print("Você não precisa pagar impostos")
else:
    if (custo_fabrica > 12000 and custo_fabrica <= 25000):
        comissao = custo_fabrica * 0.10
        impostos = custo_fabrica * 0.15
        print("A comissão do distribuidor fica:",comissao)
        print("Os impostos que você deve pegar é:",impostos)
    else:
        if (custo_fabrica > 25000):
            comissao = custo_fabrica * 0.15
            impostos = custo_fabrica * 0.20
            print("A comissão do distribuidor fica:",comissao)
            print("Os impostos você deve pegar é:",impostos)
