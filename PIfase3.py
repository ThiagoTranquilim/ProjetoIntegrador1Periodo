import cx_Oracle  # Importa a biblioteca do Oracle
import msvcrt  # É um módulo para Windows que importa a funcionalidade de pressionar uma tecla do teclado sem a necessidade de apertar Enter
import os  # É um módulo para Windows que importa varias funcionalidades, no caso desse sistema foi utilizado para limpar a tela do console

conn = cx_Oracle.connect('bd240223111/Kyaoo7@172.16.12.14:1521/xe')  # Conn é a variável definida para conectar ao banco de dados
cursor = conn.cursor()  # Cursor é uma variavel definida para executar consultas no Oracle


def insertAmostra():  # Essa função tem como objetivo inserir uma amostra no banco de dados
    print("\n--------------------------------")
    print("Inserir Amostras")
    print("--------------------------------\n")
    while True:
        try:
            idNovaAmostra = int(input("Digite o ID da nova amostra a ser cadastrada: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    while True:
        try:
            novaMP10 = int(input("Digite o valor do MP10: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    while True:
        try:
            novaMP25 = int(input("Digite o valor do MP25: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    while True:
        try:
            novaO3 = int(input("Digite o valor do O3: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    while True:
        try:
            novaCO = int(input("Digite o valor do CO: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    while True:
        try:
            novaNO2 = int(input("Digite o valor do NO2: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    while True:
        try:
            novaSO2 = int(input("Digite o valor do SO2: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    consultaSQL = "INSERT INTO PI VALUES (:idNovaAmostra, :novaMP10, :novaMP25, :novaO3, :novaCO, :novaNO2, :novaSO2)"  # Essa variável tem como string uma consulta no banco de dados
    values = {'idNovaAmostra': idNovaAmostra, 'novaMP10': novaMP10, 'novaMP25': novaMP25, 'novaO3': novaO3, 'novaCO': novaCO, 'novaNO2': novaNO2, 'novaSO2': novaSO2}  # Esse dicionário tem os valores para a consultaSQL
    cursor.execute(consultaSQL, values)  # A função .execute() tem como objetivo executar a consulta no Oracle, com os parâmetros consultaSQL e values
    conn.commit()  # A função .commit() confirma as alterações feitas no banco de dados


def listaAmostra():  # Essa função tem como objetivo listar todas as amostras no banco de dados
    print("\n--------------------------------")
    print("Lista das Amostras")
    print("--------------------------------\n")
    cursor.execute("SELECT * FROM PI ORDER BY ID")  # A função executa a consulta no Oracle
    for i in cursor:
        print(i)  # Para todo i presente na consulta, aparece na tela os registros do banco de dados


def altAmostra():  # Essa função tem como objetivo alterar alguma Amostra já cadastrada
    print("\n--------------------------------")
    print("Alteração das Amostras")
    print("--------------------------------\n")
    while True:
        try:
            idAmostraAlterar = int(input("Digite o ID da amostra a ser alterada: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    while True:
        try:
            alteraMP10 = int(input("Digite o valor de MP10 a ser alterado: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    while True:
        try:
            alteraMP25 = int(input("Digite o valor de MP25 a ser alterado: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    while True:
        try:
            alteraO3 = int(input("Digite o valor de 03 a ser alterado: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    while True:
        try:
            alteraCO = int(input("Digite o valor de CO a ser alterado: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    while True:
        try:
            alteraNO2 = int(input("Digite o valor de NO2 a ser alterado: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    while True:
        try:
            alteraSO2 = int(input("Digite o valor de SO2 a ser alterado: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    consultaSQL = "UPDATE PI SET MP10=:alteraMP10, MP25=:alteraMP25, O3=:alteraO3, CO=:alteraCO, NO2=:alteraNO2, SO2=:alteraSO2 WHERE ID=:idAmostraAlterar"  # Essa variável tem como string uma consulta no banco de dados
    values = {'idAmostraAlterar': idAmostraAlterar, 'alteraMP10': alteraMP10, 'alteraMP25': alteraMP25, 'alteraO3': alteraO3, 'alteraCO': alteraCO, 'alteraNO2': alteraNO2, 'alteraSO2': alteraSO2}  # Esse dicionário tem os valores para a consultaSQL
    cursor.execute(consultaSQL, values)  # A função executa a consulta no Oracle
    conn.commit()  # Confirma as alterações feitas no banco de dados


def excAmostra():  # Essa função tem como objetivo excluir uma Amostra no banco de dados
    print("\n--------------------------------")
    print("Excluir Amostras")
    print("--------------------------------\n")
    while True:
        try:
            idAmostraExcluir = int(input("Digite o ID da amostra a ser excluida: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    cursor.execute("DELETE FROM PI WHERE ID=:idAmostra", idAmostra=idAmostraExcluir)  # A função executa a consulta no Oracle
    conn.commit()  # Confirma as alterações feitas no banco de dados


def classAmostra():  # Essa função tem como objetivo classificar a Amostra selecionada no banco de dados
    print("\n--------------------------------")
    print("Classificação Amostra Específica")
    print("--------------------------------\n")
    while True:
        try:
            idAmostraClassificar = int(input("Digite o ID da amostra a ser classificada: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    cursor.execute("SELECT * FROM PI WHERE ID=:idAmostra", idAmostra=idAmostraClassificar)  # A função executa a consulta no Oracle
    for i in cursor:
        print(i)
    MP10 = i[1]  # Cada variavel recebe um valor correspondente a sua coluna respectivamente
    MP25 = i[2]
    O3 = i[3]
    CO = i[4]
    NO2 = i[5]
    SO2 = i[6]
    if (0 <= MP10 <= 50 and 0 <= MP25 <= 25 and 0 <= O3 <= 100 and 0 <= CO <= 9 and 0 <= NO2 <= 200 and 0 <= SO2 <= 20):  # Cada comparação se refere a uma qualidade do ar e seus efeitos a saúde
        print("Qualidade do ar: N1 - Boa")
        print("Efeitos a Saúde: ")
        print("A qualidade do ar está boa, o efeito à saúde não é prejudicial.")
    elif (MP10 <= 100 and MP25 <= 50 and O3 <= 130 and CO <= 11 and NO2 <= 240 and SO2 <= 40):
        print('Qualidade do ar: N2 - Moderada')
        print("Efeitos a Saúde: ")
        print("Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
    elif (MP10 <= 150 and MP25 <= 75 and O3 <= 160 and CO <= 13 and NO2 <= 320 and SO2 <= 365):
        print("Qualidade do ar: N3 - Ruim")
        print("Efeitos a Saúde: ")
        print("Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
    elif (MP10 <= 250 and MP25 <= 125 and O3 <= 200 and CO <= 15 and NO2 <= 1130 and SO2 <= 800):
        print("Qualidade do ar: N4 - Muito ruim")
        print("Efeitos a Saúde: ")
        print("Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
    elif (250 < MP10 or 125 < MP25 or 200 < O3 or 15 < CO or 1130 < NO2 or 800 < SO2):
        print("Qualidade do ar: N5 - Péssima")
        print("Efeitos a Saúde: ")
        print("Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.")
    else:
        print("Dados incorretos")


def menu():  # Essa função tem como objetivo mostrar na tela um menu, que retorna um valor "opcao", que será utilizado para chamar outra função
    print("\n--------------------------------")
    print("1- Listar as amostras")
    print("2 - Inserir amostras")
    print("3 - Alterar amostras")
    print("4 - Excluir amostras")
    print("5 - Classificação de amostra específica")
    print("0 - Sair")
    print("--------------------------------\n")
    while True:
        try:
            opcao = int(input("Digite a opção escolhida: "))
            break
        except ValueError:
            print("Digite um valor inteiro")
    return opcao


def main():  # Definição da função principal, a primeira a ser executada
    opcao = None
    while opcao != 0:  # Loop
        opcao = menu()
        if opcao == 1:
            listaAmostra()
        elif opcao == 2:
            insertAmostra()
        elif opcao == 3:
            altAmostra()
        elif opcao == 4:
            excAmostra()
        elif opcao == 5:
            classAmostra()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Dados inseridos incorretos")

        msvcrt.getch()  # Essa função ela permite a leitura de uma tecla sem objetivo de aparecer no prompt, dessa forma o algoritmo só continuará apartir da inserção de qualquer tecla
        os.system("cls")  # Essa função é utilizada para limpar a tela do console, com objetivo de facilitar a leitura do sistema


main()  # Após a definição de cursor, main() é executada

cursor.close()  # A função .close() é utilizada para fechar qualquer operação pendente durante o sistema, no cursor encerra qualquer consulta
conn.close()  # A função .close() é utilizada para fechar qualquer operação pendente durante o sistema, no conn encerra a conexão do banco de dados
