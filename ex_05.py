import math

# Exemplo 1

prixilato_possui = 44
zitaropan_possui = 52
madozol_possui = 36
tilazinan_possui = 14

prixilado_dia = 3
zitaropan_dia = 4
madozol_dia = 1
tilazinan_dia = 1

prixilato_caixa = 30
zitaropan_caixa = 60
madozol_caixa = 15
tilazinan_caixa = 30

prixilato_mes = prixilado_dia * 30
zitaropan_mes = zitaropan_dia * 30
madozol_mes = madozol_dia * 30
tilazinan_mes = tilazinan_dia * 30

prixilado_precisa = prixilato_mes - prixilato_possui
zitaropan_precisa = zitaropan_mes - zitaropan_possui
madozol_precisa = madozol_mes - madozol_possui
tilazinan_precisa = tilazinan_mes - tilazinan_possui

prixilato_caixas = math.ceil(prixilado_precisa / prixilato_caixa)
zitaropan_caixas = math.ceil(zitaropan_precisa / zitaropan_caixa)
madozol_caixas = math.ceil(madozol_precisa / madozol_caixa)
tilazinan_caixas = math.ceil(tilazinan_precisa / tilazinan_caixa)

print("Exemplo 1")
print("Precisamos de", prixilato_caixas, "caixas de Prixilato de Citamina")
print("Precisamos de", zitaropan_caixas, "caixas de Zitaropan")
print("Precisamos de", madozol_caixas, "caixas de Madozol")
print("Precisamos de", tilazinan_caixas, "caixas de Tilazinan")
print("")

# Exemplo 2

prixilato_possui1 = 40
zitaropan_possui1 = 60
madozol_possui1 = 40
tilazinan_possui1 = 10

prixilado_dia1 = 2
zitaropan_dia1 = 2
madozol_dia1 = 3
tilazinan_dia1 = 4

prixilato_caixa1 = 20
zitaropan_caixa1 = 75
madozol_caixa1 = 20
tilazinan_caixa1 = 25

prixilato_mes1 = prixilado_dia1 * 30
zitaropan_mes1 = zitaropan_dia1 * 30
madozol_mes1 = madozol_dia1 * 30
tilazinan_mes1 = tilazinan_dia1 * 30

prixilado_precisa1 = prixilato_mes1 - prixilato_possui1
zitaropan_precisa1 = zitaropan_mes1 - zitaropan_possui1
madozol_precisa1 = madozol_mes1 - madozol_possui1
tilazinan_precisa1 = tilazinan_mes1 - tilazinan_possui1

prixilato_caixas1 = math.ceil(prixilado_precisa1 / prixilato_caixa1)
zitaropan_caixas1 = math.ceil(zitaropan_precisa1 / zitaropan_caixa1)
madozol_caixas1 = math.ceil(madozol_precisa1 / madozol_caixa1)
tilazinan_caixas1 = math.ceil(tilazinan_precisa1 / tilazinan_caixa1)

print("Exemplo 2")
print("Precisamos de", prixilato_caixas1, "caixas de Prixilato de Citamina")
print("Precisamos de", zitaropan_caixas1, "caixas de Zitaropan")
print("Precisamos de", madozol_caixas1, "caixas de Madozol")
print("Precisamos de", tilazinan_caixas1, "caixas de Tilazinan")
print("")

# Exemplo 3

prixilato_possui2 = 17
zitaropan_possui2 = 31
madozol_possui2 = 53
tilazinan_possui2 = 9

prixilado_dia2 = 4
zitaropan_dia2 = 3
madozol_dia2 = 6
tilazinan_dia2 = 1

prixilato_caixa2 = 30
zitaropan_caixa2 = 10
madozol_caixa2 = 25
tilazinan_caixa2 = 40

prixilato_mes2 = prixilado_dia2 * 30
zitaropan_mes2 = zitaropan_dia2 * 30
madozol_mes2 = madozol_dia2 * 30
tilazinan_mes2 = tilazinan_dia2 * 30

prixilado_precisa2 = prixilato_mes2 - prixilato_possui2
zitaropan_precisa2 = zitaropan_mes2 - zitaropan_possui2
madozol_precisa2 = madozol_mes2 - madozol_possui2
tilazinan_precisa2 = tilazinan_mes2 - tilazinan_possui2

prixilato_caixas2 = math.ceil(prixilado_precisa2 / prixilato_caixa2)
zitaropan_caixas2 = math.ceil(zitaropan_precisa2 / zitaropan_caixa2)
madozol_caixas2 = math.ceil(madozol_precisa2 / madozol_caixa2)
tilazinan_caixas2 = math.ceil(tilazinan_precisa2 / tilazinan_caixa2)

print("Exemplo 3")
print("Precisamos de", prixilato_caixas2, "caixas de Prixilato de Citamina")
print("Precisamos de", zitaropan_caixas2, "caixas de Zitaropan")
print("Precisamos de", madozol_caixas2, "caixas de Madozol")
print("Precisamos de", tilazinan_caixas2, "caixas de Tilazinan")
print("")