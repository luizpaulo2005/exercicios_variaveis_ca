import math

tArea = int(input("Digite o tamanho da área em m²: ")) # tamanho da área em m²
cobTinta = int(input("Digite a cobertura de tinta em litros: ")) #cobertura da tinta em litros por m²
tamLata = int(input("Digite o tamanho da lata de tinta em litros: ")) # tamanho da lata em litros
valLata = float(input("Digite o valor da lata em reais: ")) # valor da lata em reais

# qtdLatas = (tArea * cobTinta / tArea) / tamLata # quantidade de latas
qtdLatas = math.ceil(tArea / (cobTinta * tamLata)) 
valorTotal = qtdLatas * valLata # valor total em reais

print("A quantidade de latas necessárias será de: " + str(qtdLatas) + " latas")
print("O valor total será de: R$" + str(valorTotal) + " reais")