import math

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

print("Precisamos de", prixilato_caixas, "caixas de Prixilato de Citamina")
print("Precisamos de", zitaropan_caixas, "caixas de Zitaropan")
print("Precisamos de", madozol_caixas, "caixas de Madozol")
print("Precisamos de", tilazinan_caixas, "caixas de Tilazinan")