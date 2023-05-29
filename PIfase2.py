import cx_Oracle
import msvcrt
import os

conn = cx_Oracle.connect('bd240223111/Kyaoo7@172.16.12.14:1521/xe')
cursor = conn.cursor()
mMP10 = mMP25 = mO3 = mCO = mNO2 = mSO2 = cont = 0


def listaAmostra():
    print("\n--------------------------------")
    print("Lista das Amostras")
    print("--------------------------------\n")
    cursor.execute("SELECT * FROM PI")
    for i in cursor:
        print(i)


def funcSoma(cont, mMP10, mMP25, mO3, mCO, mNO2, mSO2):
    cursor.execute("SELECT MP10 FROM PI")
    for i in cursor:
        mMP10 += i[0]
        cont += 1

    cursor.execute("SELECT MP25 FROM PI")
    for i in cursor:
        mMP25 += i[0]

    cursor.execute("SELECT O3 FROM PI")
    for i in cursor:
        mO3 += i[0]

    cursor.execute("SELECT CO FROM PI")
    for i in cursor:
        mCO += i[0]

    cursor.execute("SELECT NO2 FROM PI")
    for i in cursor:
        mNO2 += i[0]

    cursor.execute("SELECT SO2 FROM PI")
    for i in cursor:
        mSO2 += i[0]
    mMP10 = mMP10 / cont
    mMP25 = mMP25 / cont
    mO3 = mO3 / cont
    mCO = mCO / cont
    mNO2 = mNO2 / cont
    mSO2 = mSO2 / cont
    listaMedia = [mMP10, mMP25, mO3, mCO, mNO2, mSO2]
    print(f'A média de todas classificações são: {listaMedia}')
    return listaMedia


def classAmostra(cont, mMP10, mMP25, mO3, mCO, mNO2, mSO2):
    listaMedia = funcSoma(cont, mMP10, mMP25, mO3, mCO, mNO2, mSO2)
    mMP10 = listaMedia[0]
    mMP25 = listaMedia[1]
    mO3 = listaMedia[2]
    mCO = listaMedia[3]
    mNO2 = listaMedia[4]
    mSO2 = listaMedia[5]
    if (0 <= mMP10 <= 50 and 0 <= mMP25 <= 25 and 0 <= mO3 <= 100 and 0 <= mCO <= 9 and 0 <= mNO2 <= 200 and 0 <= mSO2 <= 20):
        print("Qualidade do ar: N1 - Boa")
        print("Efeitos a Saúde: ")
        print("A qualidade do ar está boa, o efeito à saúde não é prejudicial.")
    elif (mMP10 <= 100 and mMP25 <= 50 and mO3 <= 130 and mCO <= 11 and mNO2 <= 240 and mSO2 <= 40):
        print('Qualidade do ar: N2 - Moderada')
        print("Efeitos a Saúde: ")
        print("Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
    elif (mMP10 <= 150 and mMP25 <= 75 and mO3 <= 160 and mCO <= 13 and mNO2 <= 320 and mSO2 <= 365):
        print("Qualidade do ar: N3 - Ruim")
        print("Efeitos a Saúde: ")
        print("Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
    elif (mMP10 <= 250 and mMP25 <= 125 and mO3 <= 200 and mCO <= 15 and mNO2 <= 1130 and mSO2 <= 800):
        print("Qualidade do ar: N4 - Muito ruim")
        print("Efeitos a Saúde: ")
        print("Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
    elif (250 < mMP10 or 125 < mMP25 or 200 < mO3 or 15 < mCO or 1130 < mNO2 or 800 < mSO2):
        print("Qualidade do ar: N5 - Péssima")
        print("Efeitos a Saúde: ")
        print("Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.")
    else:
        print("Dados incorretos")


def menu():
    print("\n--------------------------------")
    print("1- Listar as amostras")
    print("2 - Classificação das amostras gerais")
    print("0 - Sair")
    print("--------------------------------\n")
    opcao = int(input(""))
    return opcao


def main():
    opcao = None
    while opcao != 0:
        opcao = menu()
        if opcao == 1:
            listaAmostra()
        elif opcao == 2:
            classAmostra(cont, mMP10, mMP25, mO3, mCO, mNO2, mSO2)
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Dados inseridos incorretos")

        msvcrt.getch()
        os.system("cls")


if __name__ == '__main__':
    main()

cursor.close()
conn.close()
