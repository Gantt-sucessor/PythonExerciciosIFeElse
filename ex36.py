# Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela´ que
# considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor
# salário terão um aumento proporcionalmente maior do que os funcionários com um salário
# maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus
# adicional de salário. Crie um programa que leia:
# • o valor do salário atual do funcionário;
# • o tempo de serviço desse funcionário na empresa (número de anos de trabalho na
# empresa).
# Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do
# salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum
# aumento.
# Salário Atual Reajuste (%) Tempo de Serviço Bônus
# Até 500,00    25% Abaixo de 1 ano Sem bônus
# Até 1000,00   20% De 1 a 3 anos 100,00
# Até 1500,00   15% De 4 a 6 anos 200,00
# Até 2000,00   10% De 7 a 10 anos 300,00
# Acima de 2000,00 Sem reajuste Mais de 10 anos 500,00

salario_atual = float(input("Informe seu salário atual:"))
tempo_servico = float(input("Informe seu tempo se serviço em anos na empresa:"))

if (salario_atual <= 500 and tempo_servico <= 1):
    salario_novo = salario_atual + (salario_atual * 0.25)
    print("Seu salario após os reajustes ficou:",salario_novo)
    print("Você não tem bônus por tempo de serviço")
else:
    if (salario_atual <= 1000 and tempo_servico > 1 or tempo_servico <= 3):
        salario_novo = salario_atual + (salario_atual * 0.20)
        bonus = salario_novo + 100
        print("Seu salario após os reajustes ficou:",salario_novo,"e seu bônus por tempo de serviço ficou:",bonus)
    else:
        if (salario_atual <= 1500 and tempo_servico >= 4 or tempo_servico <= 6):
            salario_novo = salario_atual + (salario_atual * 0.15)
            bonus = salario_novo + 200
            print("Seu salario após os reajustes ficou:",salario_novo,"e seu bônus por tempo de serviço ficou:",bonus)
        else:
            if (salario_atual <= 2000 and tempo_servico >= 7 or tempo_servico <= 10 ):
                salario_novo = salario_atual + (salario_atual * 0.10)
                bonus = salario_novo + 300
                print("Seu salario após os reajustes ficou:",salario_novo,"e seu bônus por tempo de serviço ficou:",bonus)
            else:
                if (salario_atual > 2000 and tempo_servico > 10):
                    bonus = salario_atual + 50
                    print("Você não tem reajuste de salário, mas seu bônus por tempo de serviço ficou:",bonus)
                 
