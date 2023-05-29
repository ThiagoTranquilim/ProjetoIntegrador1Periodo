# Partículas inaláveis (MP10)
# Partículas inaláveis finas (MP2,5)
# Ozônio (O3)
# Monóxido de carbono (CO)
# Dióxido de nitrogênio (NO2)
# Dióxido de enxofre (SO2)

MP10 = int(input("Qual o índice de partículas inaláveis (MP10): "))
MP2 = int(input("Qual o índice de partículas inaláveis finas (MP2,5): "))
O3 = int(input("Qual o índice de ozônio (O3): "))
CO = int(input("Qual o índice de monóxido de carbono (CO): "))
NO2 = int(input("Qual o índice de dióxido de nitrogênio (NO2): "))
SO2 = int(input("Qual o índice de dióxido de enxofre (SO2): "))

if (0 <= MP10 <= 50 and 0 <= MP2 <= 25 and 0 <= O3 <= 100 and 0 <= CO <= 9 and 0 <= NO2 <= 200 and 0 <= SO2 <= 20):
    print("Qualidade do ar: N1 - Boa")
    print("Efeitos a Saúde: ")
    print("A qualidade do ar está boa, o efeito à saúde não é prejudicial.")
elif (MP10 <= 100 and MP2 <= 50 and O3 <= 130 and CO <= 11 and NO2 <= 240 and SO2 <= 40):
    print('Qualidade do ar: N2 - Moderada')
    print("Efeitos a Saúde: ")
    print("Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
elif ( MP10 <= 150 and MP2 <= 75 and O3 <= 160 and CO <= 13 and NO2 <= 320 and SO2 <= 365):
    print("Qualidade do ar: N3 - Ruim")
    print("Efeitos a Saúde: ")
    print("Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
elif (MP10 <= 250 and MP2 <= 125 and O3 <= 200 and CO <= 15 and NO2 <= 1130 and SO2 <= 800):
    print("Qualidade do ar: N4 - Muito ruim")
    print("Efeitos a Saúde: ")
    print("Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
elif (250 < MP10 or 125 < MP2 or 200 < O3 or 15 < CO or 1130 < NO2 or 800 < SO2):
    print("Qualidade do ar: N5 - Péssima")
    print("Efeitos a Saúde: ")
    print("Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.")
else:
    print("Dados incorretos")
