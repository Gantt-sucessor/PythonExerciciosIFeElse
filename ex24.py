# Crie um programa que calcule e mostre a área de um trapézio. Sabe-se que:

base_maior = int(input("Informe a base maior do trapézio:"))
base_menor = int(input("Informe a base menor do trapézio:"))
altura = int(input("Informe a altura do trapézio:"))

area = (base_maior + base_menor)*altura/2

if (base_maior and base_menor != 0):
    print("A área do trapézio é:",area)
else:
    print("Valores não correspondem!")