# Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um
# percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:

distancia = float(input("Informe a distância em km:"))
litros_consumidos = float(input("Informe a quantidade de litros consumidos:"))
consumo_kml = distancia/litros_consumidos

print(consumo_kml)

if (consumo_kml < 8):
    print("Venda o carro!")
else:
    if (consumo_kml >= 8 and consumo_kml <= 12):
        print("Econômico")
    else:
        if (consumo_kml > 14):
            print("Super Econônomico")
