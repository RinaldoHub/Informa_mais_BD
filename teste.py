import sys

import mysql.connector  # Importamos o concector MySQL que implementa o Banco
import datetime

# Aqui vai as credenciais do nosso banco. Serve para realizar a conexão do plugin do python com o BD
# PRIMEIRAMENTE, FAZEMOS A CONEXÃO SEM NENHUM BANCO DE DADOS
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=""
)

# O cursor precisa ser criado para que possamos executar os códigos SQL no Python
# Lembra bastante os Objetos em Java.
cursor = mydb.cursor(prepared=True)

# Aqui o Python irá abrir o arquivo .sql com os comandos DDL para criação do nosso banco
# E DEPOIS, LEMOS AS DUAS PRIMEIRAS LINHAS DO ARQUIVO.SQL QUE DROPA O BANCO CASO EXISTA E CRIA UM NOVO
f = open("informa_mais.sql", "r")
cursor.execute(f.readline())
cursor.execute(f.readline())

# POR ÚLTIMO FAZEMOS UMA NOVA CONEXÃO COM O BANCO JÁ CRIADO E USANDO-O
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="informa_mais"
)

# TELA DE INTRODUÇÃO e decoração pro código
print("########## BEM-VINDO(A) AO INFORMA+ ##########\nPara sair, digite -1\n")
print("BANCO DE DADOS ATIVO: %s\nUSUÁRIO: %s\n" % (mydb.database, mydb.user))
print("\nCarregando aplicativo...\n")

# É necessário criar outro cursor, já que a conexão mudou
cursor = mydb.cursor(prepared=True)

# E FINALIZAMOS A EXECUÇÃO DOS COMANDOS DDL DE TABELAS E FKs DO ARQUIVO
for x in f:
    cursor.execute(x)
f.close()


# TELA INICIAL
def MenuLogin():

    # Declaração de variáveis de acesso global
    global emailCid, senhaCid, emailFunc, senhaFunc, acessoCid, acessoFunc

    print("------------------------------------\n")
    print("########## TELA PRINCIPAL ##########")
    print("[1] - Cidadão\n[2] - Funcionário\n[3] - TESTADOR DE FUNCOES\n[4] - Sair")
    numero = input("Quem você é?\n>")

    # CIDADÃO
    if (numero == '1'):
        numero = input("\nO que deseja?\n[1] - LOGIN\n[2] - CADASTRAR\n>")
        print("")  # Quebra de linha

        if numero == '1':
            LoginCid()
        elif numero == '2':
            CadastrarCid()

    # FUNCIONÁRIO PÚBLICO
    elif (numero == '2'):
        numero = input("\nO que deseja?\n[1] - LOGIN\n[2] - CADASTRAR\n>")
        print("")  # Quebra de linha

        if numero == '1':
            LoginFunc()
        elif numero == '2':
            CadastrarFunc()

    # TESTADOR
    elif (numero == '3'):
        MenuPrincipal()

    # SAIR DO APLICATIVO
    elif (numero == '4'):
        print("########## APLICATIVO ENCERRADO ##########")
        quit()

# TELA DE LOGIN DO CIDADÃO
def LoginCid():
    global emailCid, senhaCid, acessoCid
    try:
        print("------------------------------------\n")
        print("########## TELA DE LOGIN ##########")
        autorizacao = None
        email = input("Digite seu E-Mail: ")
        senha = input("Digite sua Senha: ")
        sql = "select id_cidadao from cidadao where email = '%s' and senha = '%s'"
        val = (email, senha)
        x = None
        cursor.execute(sql % val)
        for x in cursor:
            x = cursor
        autorizacao = x
        if autorizacao != None:
            print("------------------------------------\nACESSO AUTORIZADO")
            emailCid = email
            senhaCid = senha
            acessoCid = (emailCid, senhaCid)
            MenuCid()
        else:
            print("E-MAIL OU SENHA INCORRETOS\n")
            LoginCid()
    except:
        print("E-MAIL OU SENHA INCORRETOS\n")
        LoginCid()


# Cadastro do cidadão
def CadastrarCid():
    global emailCid, senhaCid, acessoCid
    try:
        print("------------------------------------\n")
        print("########## TELA DE CADASTRO ##########")
        print("---------- DADOS PESSOAIS ----------")

        # Primeiro os dados pessoais
        a = input("Nome: ")
        b1 = int(input("Data de Nascimento (DIA): "))
        b2 = int(input("Data de Nascimento (MÊS): "))
        b3 = int(input("Data de Nascimento (ANO): "))
        b = datetime.date(b3, b2, b1).isoformat()
        c = input("Telefone: (xx)9xxxx-xxxx\n>")
        email = input("E-Mail: ")
        senha = input("Senha: ")
        sql = "INSERT INTO CIDADAO(nome, data_nascimento, telefone, email, senha) VALUES(%a, %a, %a, %a, %a)"
        val = (a, b, c, email, senha)
        cursor.execute(sql % val)
        mydb.commit()

        # Depois o Endereço
        print("---------- ENDEREÇO ----------")
        a = input("CEP: (xxxxx-xxx)\n>")
        b = input("Cidade: ")
        c = input("Bairro: ")
        d = input("Rua: ")
        e = input("Número: ")
        sql = "INSERT INTO ENDERECO(cep, cidade, bairro, rua, numero) VALUES(%a, %a, %a, %a, %a)"
        val = (a, b, c, d, e)
        cursor.execute(sql % val)
        mydb.commit()
        print("------------------------------------\nACESSO AUTORIZADO")

        emailCid = email
        senhaCid = senha
        acessoCid = (emailCid, senhaCid)

        # Agora unimos as FKs nas tabelas
        sql = "update cidadao set ID_endereco = (select max(id_endereco) from endereco order by id_endereco desc limit 1) where email = '%s' and senha = '%s'"
        cursor.execute(sql % acessoCid)
        cursor.fetchall()
        mydb.commit()

        MenuCid()
    except:
        print("##### ALGO DEU ERRADO #####\n##### Chame Roque #####")
        pass
        CadastrarCid()


# TELA DE LOGIN DO FUNCIONÁRIO
def LoginFunc():
    global emailFunc, senhaFunc, acessoFunc
    try:
        print("------------------------------------\n")
        print("########## TELA DE LOGIN ##########")
        autorizacao = None
        email = input("E-Mail Institucional: ")
        senha = input("Senha: ")

        sql = "select id_funcionario from funcionario_publico where email_institucional = '%s' and senha = '%s'"
        val = (email, senha)

        x = None
        cursor.execute(sql % val)
        for x in cursor:
            x = cursor
        autorizacao = x

        if autorizacao != None:
            print("------------------------------------\nACESSO AUTORIZADO")
            emailFunc = email
            senhaFunc = senha
            acessoFunc = (emailFunc, senhaFunc)
            MenuFunc()
        else:
            print("E-MAIL OU SENHA INCORRETOS\n")
            LoginFunc()
    except:
        print("E-MAIL OU SENHA INCORRETOS\n")
        LoginFunc()


# TELA DE CADASTRO DO FUNCIONÁRIO
def CadastrarFunc():
    global emailFunc, senhaFunc, acessoFunc
    try:
        print("------------------------------------\n")
        print("########## TELA DE CADASTRO ##########")
        a = input("Nome: ")
        b = input("Órgão/Empresa: ")
        email = input("E-Mail Institucional: ")
        senha = input("Senha: ")
        sql = "INSERT INTO FUNCIONARIO_PUBLICO(nome, orgao_empresa, email_institucional, senha) VALUES(%a, %a, %a, %a)"
        val = (a, b, email, senha)
        cursor.execute(sql % val)
        mydb.commit()
        print("------------------------------------\nACESSO AUTORIZADO")
        emailFunc = email
        senhaFunc = senha
        acessoFunc = (emailFunc, senhaFunc)
        MenuFunc()
    except:
        print("##### ALGO DEU ERRADO #####\n##### Chame Roque #####")
        pass
        CadastrarFunc()


# FUNÇÃO DO TESTADOR contendo todas as funções do banco
def MenuPrincipal():
    try:
        while True:
            print("------------ BEM-VINDO, TESTADOR ------------\n")
            print("########## MENU PRINCIPAL ##########")
            print(
                "[1] - MOSTRAR TABELAS\n[2] - INSERIR DADOS NA TABELA\n[3] - ATUALIZAR DADOS\n[4] - PESQUISAR DADOS\n[5] - DELETAR TUPLA\n[6] - SAIR\n")
            numero = input("O que deseja?\n>")

            # MOSTRAR TABELAS
            if (numero == '1'):
                print(
                    "[1] - RELATO\n[2] - CIDADÃO\n[3] - FUNCIONÁRIO PÚBLICO\n[4] - ENDEREÇO\n[5] - PROBLEMA\n[6] - LOCALIZAÇÃO\n")
                tabela = input(
                    "Deseja visualizar todos os dados de alguma tabela?\nSe sim, digite o número dela\nSe não, digite '-1'\n>")

                while tabela != '-1':
                    if tabela == '1':
                        print("")  # Quebra de linha
                        cursor.execute("select * from relato")
                        for x in cursor:
                            print(x)
                    if tabela == '2':
                        print("")  # Quebra de linha
                        cursor.execute("select * from cidadao")
                        for x in cursor:
                            print(x)
                    if tabela == '3':
                        print("")  # Quebra de linha
                        cursor.execute("select * from funcionario_publico")
                        for x in cursor:
                            print(x)
                    if tabela == '4':
                        print("")  # Quebra de linha
                        cursor.execute("select * from endereco")
                        for x in cursor:
                            print(x)
                    if tabela == '5':
                        print("")  # Quebra de linha
                        cursor.execute("select * from problema")
                        for x in cursor:
                            print(x)
                    if tabela == '6':
                        print("")  # Quebra de linha
                        cursor.execute("select * from localizacao")
                        for x in cursor:
                            print(x)

                    print("")  # Quebra de linha
                    print(
                        "[1] - RELATO\n[2] - CIDADÃO\n[3] - FUNCIONÁRIO PÚBLICO\n[4] - ENDEREÇO\n[5] - PROBLEMA\n[6] - LOCALIZAÇÃO\n")
                    tabela = input(
                        "Deseja visualizar alguma outra tabela?\nSe sim, digite o número dela\nSe não, digite '-1'\n>")

            # INSERIR DE DADOS
            elif (numero == '2'):
                print("------------------------------------\n")
                print("########## INSERÇÃO DE DADOS ##########")
                print(
                    "[1] - RELATO\n[2] - CIDADÃO\n[3] - FUNCIONÁRIO PÚBLICO\n[4] - ENDEREÇO\n[5] - PROBLEMA\n[6] - LOCALIZAÇÃO\n")
                tabela = input('Qual TABELA deseja INSERIR DADOS?\n>')
                while tabela != '-1':
                    if tabela == '1':
                        a = input("Descrição: ")
                        b = datetime.datetime.now().isoformat()
                        c = input("Status: (PUBLICADO, EM ANDAMENTO, DESATIVADO OU RESOLVIDO)\n>")
                        sql = "INSERT INTO RELATO(descricao, data, status) VALUES(%a, %a, %a)"
                        val = (a, b, c)
                        cursor.execute(sql % val)
                        mydb.commit()
                        cursor.execute("select * from relato")
                        for x in cursor:
                            print(x)
                    elif tabela == '2':
                        a = input("Nome: ")
                        b1 = int(input("Data de Nascimento (DIA): "))
                        b2 = int(input("Data de Nascimento (MÊS): "))
                        b3 = int(input("Data de Nascimento (ANO): "))
                        b = datetime.date(b3, b2, b1).isoformat()
                        c = input("Telefone: (xx)9xxxx-xxxx\n>")
                        d = input("E-Mail: ")
                        e = input("Senha: ")
                        sql = "INSERT INTO CIDADAO(nome, data_nascimento, telefone, email, senha) VALUES(%a, %a, %a, %a, %a)"
                        val = (a, b, c, d, e)
                        cursor.execute(sql % val)
                        mydb.commit()
                        cursor.execute("select * from cidadao")
                        for x in cursor:
                            print(x)
                    elif tabela == '3':
                        a = input("Nome: ")
                        b = input("Órgão/Empresa: ")
                        c = input("E-Mail Institucional: ")
                        d = input("Senha: ")
                        sql = "INSERT INTO FUNCIONARIO_PUBLICO(nome, orgao_empresa, email_institucional, senha) VALUES(%a, %a, %a, %a)"
                        val = (a, b, c, d)
                        cursor.execute(sql % val)
                        mydb.commit()
                        cursor.execute("select * from funcionario_publico")
                        for x in cursor:
                            print(x)
                    elif tabela == '4':
                        a = input("CEP: (xxxxx-xxx)\n>")
                        b = input("Cidade: ")
                        c = input("Bairro: ")
                        d = input("Rua: ")
                        e = input("Número: ")
                        sql = "INSERT INTO ENDERECO(cep, cidade, bairro, rua, numero) VALUES(%s, %s, %s, %s, %s)"
                        val = (a, b, c, d, e)
                        cursor.execute(sql, val)
                        mydb.commit()
                        cursor.execute("select * from endereco")
                        for x in cursor:
                            print(x)
                    elif tabela == '5':
                        a = input("Categoria: ")
                        b = input("Subcategoria: ")
                        sql = "INSERT INTO PROBLEMA(categoria, subcategoria) VALUES(%a, %a)"
                        val = (a, b)
                        cursor.execute(sql % val)
                        mydb.commit()
                        cursor.execute("select * from problema")
                        for x in cursor:
                            print(x)
                    elif tabela == '6':
                        a = input("Rua: ")
                        b = input("Bairro: ")
                        c = input("Cidade: ")
                        d = input("CEP: (xxxxx-xxx)\n>")
                        sql = "INSERT INTO LOCALIZACAO(rua, bairro, cidade, cep) VALUES (%s, %s, %s, %s)"
                        val = (a, b, c, d)
                        cursor.execute(sql % val)
                        mydb.commit()
                        cursor.execute("select * from localizacao")
                        for x in cursor:
                            print(x)

                    print("")  # Quebra de linha
                    print(cursor.rowcount, "Linhas(s) INSERIDA(s)!\n")
                    print(
                        "[1] - RELATO\n[2] - CIDADÃO\n[3] - FUNCIONÁRIO PÚBLICO\n[4] - ENDEREÇO\n[5] - PROBLEMA\n[6] - LOCALIZAÇÃO\n")
                    tabela = input(
                        "Deseja inserir mais dados?\nSe sim, digite o número da tabela\nSe não, digite '-1'\n>")

            # ATUALIZAR DADOS
            elif (numero == '3'):

                print("------------------------------------------\n")
                print("########## ATUALIZAÇÃO DE DADOS ##########")
                print(
                    "[1] - RELATO\n[2] - CIDADÃO\n[3] - FUNCIONÁRIO PÚBLICO\n[4] - ENDEREÇO\n[5] - PROBLEMA\n[6] - LOCALIZAÇÃO\n")
                tabela = input('Qual TABELA deseja ATUALIZAR DADOS?\n>')
                while tabela != '-1':
                    if tabela == '1':
                        print("-------------------- COLUNAS NA TABELA RELATO --------------------")
                        cursor.execute("describe relato")
                        for x in cursor:
                            print(x)
                        print("-------------------- DADOS NA TABELA RELATO --------------------")
                        cursor.execute("select * from relato")
                        for x in cursor:
                            print(x)
                        print("")  # Quebra de Linha
                        c = input("Digite a ID do RELATO que sofrerá a atualização: ")
                        a = input("Digite a coluna que deseja atualizar: ")
                        b = input("Digite o dado que deseja inserir: ")
                        sql = "UPDATE RELATO SET %s = '%s' WHERE ID_RELATO = '%s'"
                        val = (a, b, c)
                        cursor.execute(sql % val)
                        mydb.commit()
                        val = (a, c)
                        cursor.execute("SELECT * FROM RELATO WHERE ID_RELATO = '%s'" % c)
                        for x in cursor:
                            print(x)
                    elif tabela == '2':
                        print("-------------------- COLUNAS NA TABELA CIDADÃO --------------------")
                        cursor.execute("describe cidadao")
                        for x in cursor:
                            print(x)
                        print("-------------------- DADOS NA TABELA CIDADÃO --------------------")
                        cursor.execute("select * from cidadao")
                        for x in cursor:
                            print(x)
                        print("")  # Quebra de Linha
                        c = input("Digite a ID do CIDADÃO que sofrerá a atualização: ")
                        a = input("Digite a coluna que deseja atualizar: ")
                        b = input("Digite o dado que deseja inserir: ")
                        sql = "UPDATE CIDADAO SET %s = '%s' WHERE ID_CIDADAO = '%s'"
                        val = (a, b, c)
                        cursor.execute(sql % val)
                        mydb.commit()
                        val = (a, c)
                        cursor.execute("SELECT * FROM CIDADAO WHERE ID_CIDADAO = '%s'" % c)
                        for x in cursor:
                            print(x)
                    elif tabela == '3':
                        print("-------------------- COLUNAS NA TABELA FUNCIONÁRIO PÚBLICO --------------------")
                        cursor.execute("describe FUNCIONARIO_PUBLICO")
                        for x in cursor:
                            print(x)
                        print("-------------------- DADOS NA TABELA FUNCIONÁRIO PÚBLICO --------------------")
                        cursor.execute("select * from FUNCIONARIO_PUBLICO")
                        for x in cursor:
                            print(x)
                        print("")  # Quebra de Linha
                        c = input("Digite a ID do FUNCIONÁRIO PÚBLICO que sofrerá a atualização: ")
                        a = input("Digite a coluna que deseja atualizar: ")
                        b = input("Digite o dado que deseja inserir: ")
                        sql = "UPDATE FUNCIONARIO_PUBLICO SET %s = '%s' WHERE ID_FUNCIONARIO = '%s'"
                        val = (a, b, c)
                        cursor.execute(sql % val)
                        mydb.commit()
                        val = (a, c)
                        cursor.execute("SELECT * FROM FUNCIONARIO_PUBLICO WHERE ID_FUNCIONARIO = '%s'" % c)
                        for x in cursor:
                            print(x)
                    elif tabela == '4':
                        print("-------------------- COLUNAS NA TABELA ENDEREÇO --------------------")
                        cursor.execute("describe endereco")
                        for x in cursor:
                            print(x)
                        print("-------------------- DADOS NA TABELA ENDEREÇO --------------------")
                        cursor.execute("select * from endereco")
                        for x in cursor:
                            print(x)
                        print("")  # Quebra de Linha
                        c = input("Digite a ID do ENDEREÇO que sofrerá a atualização: ")
                        a = input("Digite a coluna que deseja atualizar: ")
                        b = input("Digite o dado que deseja inserir: ")
                        sql = "UPDATE endereco SET %s = '%s' WHERE ID_endereco = '%s'"
                        val = (a, b, c)
                        cursor.execute(sql % val)
                        mydb.commit()
                        val = (a, c)
                        cursor.execute("SELECT * FROM endereco WHERE ID_endereco = '%s'" % c)
                        for x in cursor:
                            print(x)
                    elif tabela == '5':
                        print("-------------------- COLUNAS NA TABELA PROBLEMA --------------------")
                        cursor.execute("describe problema")
                        for x in cursor:
                            print(x)
                        print("-------------------- DADOS NA TABELA PROBLEMA --------------------")
                        cursor.execute("select * from problema")
                        for x in cursor:
                            print(x)
                        print("")  # Quebra de Linha
                        c = input("Digite a ID do PROBLEMA que sofrerá a atualização: ")
                        a = input("Digite a coluna que deseja atualizar: ")
                        b = input("Digite o dado que deseja inserir: ")
                        sql = "UPDATE problema SET %s = '%s' WHERE ID_problema = '%s'"
                        val = (a, b, c)
                        cursor.execute(sql % val)
                        mydb.commit()
                        val = (a, c)
                        cursor.execute("SELECT * FROM problema WHERE id_problema = '%s'" % c)
                        for x in cursor:
                            print(x)
                    elif tabela == '6':
                        print("-------------------- COLUNAS NA TABELA LOCALIZAÇÃO --------------------")
                        cursor.execute("describe localizacao")
                        for x in cursor:
                            print(x)
                        print("-------------------- DADOS NA TABELA LOCALIZAÇÃO --------------------")
                        cursor.execute("select * from localizacao")
                        for x in cursor:
                            print(x)
                        print("")  # Quebra de Linha
                        c = input("Digite a ID da LOCALIZAÇÃO que sofrerá a atualização: ")
                        a = input("Digite a coluna que deseja atualizar: ")
                        b = input("Digite o dado que deseja inserir: ")
                        sql = "UPDATE localizacao SET %s = '%s' WHERE ID_localizacao = '%s'"
                        val = (a, b, c)
                        cursor.execute(sql % val)
                        mydb.commit()
                        val = (a, c)
                        cursor.execute("SELECT * FROM localizacao WHERE ID_localizacao = '%s'" % c)
                        for x in cursor:
                            print(x)

                    print("")  # Quebra de linha
                    print(cursor.rowcount, "Linha(s) ATUALIZADA(s)!\n")
                    print(
                        "[1] - RELATO\n[2] - CIDADÃO\n[3] - FUNCIONÁRIO PÚBLICO\n[4] - ENDEREÇO\n[5] - PROBLEMA\n[6] - LOCALIZAÇÃO\n")
                    tabela = input(
                        "Deseja inserir mais dados?\nSe sim, digite o número da tabela\nSe não, digite '-1'\n>")

            # PESQUISAR DADOS
            elif (numero == '4'):
                print("------------------------------------\n")
                print("########## PESQUISA DE DADOS ##########")
                print(
                    "[1] - RELATO\n[2] - CIDADÃO\n[3] - FUNCIONÁRIO PÚBLICO\n[4] - ENDEREÇO\n[5] - PROBLEMA\n[6] - LOCALIZAÇÃO\n")
                tabela = input('Em qual TABELA deseja PESQUISAR?\n>')
                while tabela != '-1':
                    if tabela == '1':
                        print("Colunas na TABELA RELATO")
                        cursor.execute("describe relato")
                        for x in cursor:
                            print(x)

                        coluna = input("Coluna que deseja pesquisar: ")
                        pesq = input("O que deseja pesquisar: ")
                        posicao = input(
                            "Deseja que sua pesquisa esteja no começo (1), meio (2), ou fim (3) do registo?\n>")

                        if posicao == '1':
                            sql = "SELECT * FROM RELATO WHERE %s LIKE '%s'"
                            val = (coluna, pesq + "%",)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        elif posicao == '2':
                            sql = "SELECT * FROM RELATO WHERE %s LIKE '%s'"
                            val = (coluna, "%" + pesq + "%",)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        elif posicao == '3':
                            sql = "SELECT * FROM RELATO WHERE %s LIKE '%s'"
                            val = (coluna, "%" + pesq,)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        print("")

                    elif tabela == '2':
                        print("Colunas na TABELA CIDADAO")
                        cursor.execute("describe cidadao")
                        for x in cursor:
                            print(x)

                        coluna = input("Coluna que deseja pesquisar: ")
                        pesq = input("O que deseja pesquisar: ")
                        posicao = input(
                            "Deseja que sua pesquisa esteja no começo (1), meio (2), ou fim (3) do registo?\n>")

                        if posicao == '1':
                            sql = "SELECT * FROM CIDADAO WHERE %s LIKE '%s'"
                            val = (coluna, pesq + "%",)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        elif posicao == '2':
                            sql = "SELECT * FROM CIDADAO WHERE %s LIKE '%s'"
                            val = (coluna, "%" + pesq + "%",)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        elif posicao == '3':
                            sql = "SELECT * FROM CIDADAO WHERE %s LIKE '%s'"
                            val = (coluna, "%" + pesq,)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        print("")

                    elif tabela == '3':
                        print("Colunas na TABELA FUNCIONÁRIO PÚBLICO")
                        cursor.execute("describe funcionario_publico")
                        for x in cursor:
                            print(x)

                        coluna = input("Coluna que deseja pesquisar: ")
                        pesq = input("O que deseja pesquisar: ")
                        posicao = input(
                            "Deseja que sua pesquisa esteja no começo (1), meio (2), ou fim (3) do registo?\n>")

                        if posicao == '1':
                            sql = "SELECT * FROM FUNCIONARIO_PUBLICO WHERE %s LIKE '%s'"
                            val = (coluna, pesq + "%",)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        elif posicao == '2':
                            sql = "SELECT * FROM FUNCIONARIO_PUBLICO WHERE %s LIKE '%s'"
                            val = (coluna, "%" + pesq + "%",)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        elif posicao == '3':
                            sql = "SELECT * FROM FUNCIONARIO_PUBLICO WHERE %s LIKE '%s'"
                            val = (coluna, "%" + pesq,)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        print("")
                    elif tabela == '4':
                        print("Colunas na TABELA ENDEREÇO")
                        cursor.execute("describe endereco")
                        for x in cursor:
                            print(x)

                        coluna = input("Coluna que deseja pesquisar: ")
                        pesq = input("O que deseja pesquisar: ")
                        posicao = input(
                            "Deseja que sua pesquisa esteja no começo (1), meio (2), ou fim (3) do registo?\n>")

                        if posicao == '1':
                            sql = "SELECT * FROM ENDERECO WHERE %s LIKE '%s'"
                            val = (coluna, pesq + "%",)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        elif posicao == '2':
                            sql = "SELECT * FROM ENDERECO WHERE %s LIKE '%s'"
                            val = (coluna, "%" + pesq + "%",)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        elif posicao == '3':
                            sql = "SELECT * FROM ENDERECO WHERE %s LIKE '%s'"
                            val = (coluna, "%" + pesq,)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        print("")
                    elif tabela == '5':
                        print("Colunas na TABELA PROBLEMA")
                        cursor.execute("describe problema")
                        for x in cursor:
                            print(x)

                        coluna = input("Coluna que deseja pesquisar: ")
                        pesq = input("O que deseja pesquisar: ")
                        posicao = input(
                            "Deseja que sua pesquisa esteja no começo (1), meio (2), ou fim (3) do registo?\n>")

                        if posicao == '1':
                            sql = "SELECT * FROM PROBLEMA WHERE %s LIKE '%s'"
                            val = (coluna, pesq + "%",)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        elif posicao == '2':
                            sql = "SELECT * FROM PROBLEMA WHERE %s LIKE '%s'"
                            val = (coluna, "%" + pesq + "%",)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        elif posicao == '3':
                            sql = "SELECT * FROM PROBLEMA WHERE %s LIKE '%s'"
                            val = (coluna, "%" + pesq,)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        print("")
                    elif tabela == '6':
                        print("Colunas na TABELA LOCALIZAÇÃO")
                        cursor.execute("describe localizacao")
                        for x in cursor:
                            print(x)

                        coluna = input("Coluna que deseja pesquisar: ")
                        pesq = input("O que deseja pesquisar: ")
                        posicao = input(
                            "Deseja que sua pesquisa esteja no começo (1), meio (2), ou fim (3) do registo?\n>")

                        if posicao == '1':
                            sql = "SELECT * FROM LOCALIZACAO WHERE %s LIKE '%s'"
                            val = (coluna, pesq + "%",)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        elif posicao == '2':
                            sql = "SELECT * FROM LOCALIZACAO WHERE %s LIKE '%s'"
                            val = (coluna, "%" + pesq + "%",)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        elif posicao == '3':
                            sql = "SELECT * FROM LOCALIZACAO WHERE %s LIKE '%s'"
                            val = (coluna, "%" + pesq,)
                            cursor.execute(sql % val)
                            for x in cursor:
                                print(x)
                        print("")
                    print("")  # Quebra de linha
                    print(
                        "[1] - RELATO\n[2] - CIDADÃO\n[3] - FUNCIONÁRIO PÚBLICO\n[4] - ENDEREÇO\n[5] - PROBLEMA\n[6] - LOCALIZAÇÃO\n")
                    tabela = input(
                        "Deseja realizar outra pesquisa?\nSe sim, digite o número da tabela\nSe não, digite '-1'\n>")

            # DELETAR TUPLA
            elif (numero == '5'):
                print("------------------------------------\n")
                print(
                    "[1] - RELATO\n[2] - CIDADÃO\n[3] - FUNCIONÁRIO PÚBLICO\n[4] - ENDEREÇO\n[5] - PROBLEMA\n[6] - LOCALIZAÇÃO\n")
                print("########## DELETAR TUPLA ##########")
                tabela = input('Em qual TABELA deseja DELETAR uma TUPLA?\n>')
                while tabela != '-1':
                    if tabela == '1':
                        # Primeiro mostra todas TUPLAS da TABELA
                        print("")  # Quebra de linha
                        cursor.execute("select * from relato")
                        for x in cursor:
                            print(x)
                        print("")  # Quebra de linha

                        # Depois pede que TUPLA deseja DELETAR
                        a = input("ID da TUPLA que deseja DELETAR: ")
                        sql = "DELETE FROM relato WHERE ID_relato LIKE '%s'"
                        val = (a)
                        cursor.execute(sql % val)
                        mydb.commit()  # Sempre commitar depois de codigos DML
                        cursor.execute("select * from relato")
                        for x in cursor:
                            print(x)

                    elif tabela == '2':
                        print("")  # Quebra de linha
                        # Primeiro mostra todas TUPLAS da TABELA
                        cursor.execute("select * from cidadao")
                        for x in cursor:
                            print(x)
                        print("")  # Quebra de linha

                        # Depois pede que TUPLA deseja DELETAR
                        a = input("ID da TUPLA que deseja DELETAR: ")
                        sql = "DELETE FROM cidadao WHERE ID_cidadao LIKE '%s'"
                        val = (a)
                        cursor.execute(sql % val)
                        mydb.commit()  # Sempre commitar depois de codigos DML
                        cursor.execute("select * from cidadao")
                        for x in cursor:
                            print(x)

                    elif tabela == '3':
                        print("")  # Quebra de linha
                        # Primeiro mostra todas TUPLAS da TABELA
                        cursor.execute("select * from funcionario_publico")
                        for x in cursor:
                            print(x)
                        print("")  # Quebra de linha

                        # Depois pede que TUPLA deseja DELETAR
                        a = input("ID da TUPLA que deseja DELETAR: ")
                        sql = "DELETE FROM funcionario WHERE ID_funcionario LIKE '%s'"
                        val = (a)
                        cursor.execute(sql % val)
                        mydb.commit()  # Sempre commitar depois de codigos DML
                        cursor.execute("select * from funcionario_publico")
                        for x in cursor:
                            print(x)

                    elif tabela == '4':
                        print("")  # Quebra de linha
                        # Primeiro mostra todas TUPLAS da TABELA
                        cursor.execute("select * from endereco")
                        for x in cursor:
                            print(x)
                        print("")  # Quebra de linha

                        # Depois pede que TUPLA deseja DELETAR
                        a = input("ID da TUPLA que deseja DELETAR: ")
                        sql = "DELETE FROM endereco WHERE ID_endereco LIKE '%s'"
                        val = (a)
                        cursor.execute(sql % val)
                        mydb.commit()  # Sempre commitar depois de codigos DML
                        cursor.execute("select * from endereco")
                        for x in cursor:
                            print(x)

                    elif tabela == '5':
                        print("")  # Quebra de linha
                        # Primeiro mostra todas TUPLAS da TABELA
                        cursor.execute("select * from problema")
                        for x in cursor:
                            print(x)
                        print("")  # Quebra de linha

                        # Depois pede que TUPLA deseja DELETAR
                        a = input("ID da TUPLA que deseja DELETAR: ")
                        sql = "DELETE FROM problema WHERE ID_problema LIKE '%s'"
                        val = (a)
                        cursor.execute(sql % val)
                        mydb.commit()  # Sempre commitar depois de codigos DML
                        cursor.execute("select * from problema")
                        for x in cursor:
                            print(x)

                    elif tabela == '6':
                        print("")  # Quebra de linha
                        # Primeiro mostra todas TUPLAS da TABELA
                        cursor.execute("select * from localizacao")
                        for x in cursor:
                            print(x)

                        # Depois pede que TUPLA deseja DELETAR
                        a = input("ID da TUPLA que deseja DELETAR: ")
                        sql = "DELETE FROM localizacao WHERE ID_localizacao LIKE '%s'"
                        val = (a)
                        cursor.execute(sql % val)
                        mydb.commit()  # Sempre commitar depois de codigos DML
                        cursor.execute("select * from localizacao")
                        for x in cursor:
                            print(x)

                    print(cursor.rowcount, "Linha(s) DELETADA(s)!\n")
                    print(
                        "[1] - RELATO\n[2] - CIDADÃO\n[3] - FUNCIONÁRIO PÚBLICO\n[4] - ENDEREÇO\n[5] - PROBLEMA\n[6] - LOCALIZAÇÃO\n")
                    tabela = input(
                        "Deseja realizar outro DELETE?\nSe sim, digite o número da tabela\nSe não, digite '-1'\n>")

            # Fechar CONSOLE
            elif (numero == '6'):
                print("########## FAZENDO LOG OFF ##########")
                print("------------------------------------")
                MenuLogin()
    except:
        print("##### ALGO DEU ERRADO #####\n##### Chame Roque #####")
        pass
        MenuPrincipal()


# FUNÇÃO DO CIDADÃO contendo funções específicas para tal usuário
def MenuCid():
    global acessoCid
    try:
        print("------------------------------------\n")
        print("########## MENU PRINCIPAL ##########")
        print("[1] - RELATAR PROBLEMA\n[2] - LISTAR RELATOS\n[3] - EXCLUIR RELATO\n[4] - SAIR\n")
        numero = input("O que deseja?\n>")

        # RELATAR PROBLEMA
        if numero == '1':
            # INSERIR PROBLEMA
            a = input("Categoria: ")
            b = input("Subcategoria: ")
            sql = "INSERT INTO PROBLEMA(categoria, subcategoria) VALUES(%a, %a)"
            val = (a, b)
            cursor.execute(sql % val)
            mydb.commit()

            # INSERIR RELATO do problema
            a = input("Descrição: ")
            b = datetime.datetime.now().isoformat()
            c = "PUBLICADO"
            sql = "INSERT INTO RELATO(descricao, data, status) VALUES(%a, %a, %a)"
            val = (a, b, c)
            cursor.execute(sql % val)
            mydb.commit()

            # INSERIR LOCALIZAÇÃO do problema
            a = input("Rua: ")
            b = input("Bairro: ")
            c = input("Cidade: ")
            d = input("CEP: (xxxxx-xxx)\n>")
            sql = "INSERT INTO LOCALIZACAO(rua, bairro, cidade, cep) VALUES ('%s', '%s', '%s', '%s')"
            val = (a, b, c, d)
            cursor.execute(sql % val)
            mydb.commit()

            # Agora atribuímos todas as FKs
            cursor.execute("update relato r join (select max(r2.id_relato) as idMax from relato r2) as sub on r.id_relato = sub.idMax set r.id_cidadao = (select id_cidadao from cidadao where email = '%s' and senha = '%s')" % acessoCid)
            cursor.execute("update relato r join (select max(r2.id_relato) as idMax from relato r2) as sub on r.id_relato = sub.idMax set r.id_problema = (select id_problema from problema order by id_problema desc limit 1)")
            cursor.execute("update relato r join (select max(r2.id_relato) as idMax from relato r2) as sub on r.id_relato = sub.idMax set r.id_localizacao = (select id_localizacao from localizacao order by id_localizacao desc limit 1)")
            cursor.fetchall()
            mydb.commit()

            print("\nRELATO PUBLICADO COM SUCESSO\n")

            MenuCid()

        # LISTAR RELATOS
        if numero == '2':
            # MOSTRAR OS RELATOS
            print("")  # Quebra de linha
            cursor.execute(
                "select r.ID_relato, p.categoria, r.descricao, r.data, r.status, l.rua from relato as r inner "
                "join problema p on r.id_relato = p.ID_problema join localizacao as l on r.ID_relato = "
                "l.ID_localizacao order by p.categoria")
            for x in cursor:
                print(x)

            MenuCid()

        # EXCLUIR RELATOS
        if numero == '3':
            acesso = None
            # Primeiro mostra todas TUPLAS da TABELA
            print("")  # Quebra de linha
            cursor.execute(
                "select r.id_relato, r.status, p.categoria, r.descricao, r.data, l.rua from relato as r inner join "
                "problema as p on r.id_relato = p.ID_problema join localizacao as l on r.id_relato = l.id_localizacao "
                "where r.id_cidadao = (select id_cidadao from cidadao where email = '%s' and senha = '%s' limit 1)"
                "order by p.categoria" % acessoCid)
            for x in cursor:
                print(x)
            for x in cursor:
                x = cursor
            acesso = x
            print("")  # Quebra de linha

            if acesso != None:
                # Depois pede que TUPLA deseja DELETAR
                a = input("ID da TUPLA que deseja DELETAR: ")
                sql = "DELETE FROM relato WHERE ID_relato LIKE '%s'"
                val = (a)
                cursor.execute(sql % val)
                mydb.commit()  # Sempre commitar depois de codigos DML
                cursor.execute("select * from relato")
                for x in cursor:
                    print(x)
            else:
                print("VOCÊ NÃO POSSUI RELATOS. PUBLIQUE UM AGORA MESMO!")

            MenuCid()

        # FAZER LOG-OFF
        if numero == '4':
            print("\nFAZENDO LOGOFF...\n")
            MenuLogin()

    except:
        print("##### ALGO DEU ERRADO #####\n##### Chame Roque #####")
        pass
        MenuCid()


# FUNÇÃO DO FUNCIONÁRIO PÚBLICO contendo funções específicas para tal usuário
def MenuFunc():
    global acessoFunc
    try:
        print("------------------------------------\n")
        print("########## MENU PRINCIPAL ##########")
        print("[1] - LISTAR RELATOS\n[2] - MARCAR RESOLUÇÃO\n[3] - SAIR\n")
        numero = input("O que deseja?\n>")

        # MOSTRAR RELATOS
        if numero == '1':
            # MOSTRAR OS RELATOS e seus detalhes de outras TABELAS
            print("")  # Quebra de linha
            cursor.execute(
                "select r.ID_relato, p.categoria, r.descricao, r.data, r.status, l.rua from relato as r inner "
                "join problema p on r.id_relato = p.ID_problema join localizacao as l on r.ID_relato = "
                "l.ID_localizacao order by p.categoria")
            for x in cursor:
                print(x)
            MenuFunc()

        # MARCAR RESOLUÇÃO
        if numero == '2':
            print("-------------------- RELATOS EM ANDAMENTO --------------------")

            # Mostrará apenas o RELATOS com o STATUS EM ANDAMENTO ou PUBLICADO
            cursor.execute("select r.id_relato, r.status, p.categoria, r.descricao, r.data, l.rua from relato as r "
                           "inner join problema as p on r.id_relato = p.id_problema join localizacao as l on "
                           "r.ID_relato = l.ID_localizacao where (r.status like 'PUBLICADO') or (r.status like 'EM "
                           "ANDAMENTO') order by p.categoria")
            for x in cursor:
                print(x)

            print("")  # Quebra de Linha
            b = input("Digite a ID do RELATO que sofrerá a atualização: ")
            a = input("O RELATO está EM ANDAMENTO ou RESOLVIDO?\n>")
            sql = "UPDATE RELATO SET status = '%s' WHERE ID_RELATO = '%s'"
            val = (a, b)
            cursor.execute(sql % val)
            mydb.commit()

            # Agora atribuimos à FK_Relato_Funcionario a id do funcionario que atualizou o relato
            sql = "update relato set id_funcionario = (select ID_funcionario from funcionario_publico where email_institucional = '%s' and senha = '%s') where id_relato = '%s'"
            val = (emailFunc, senhaFunc, b)
            cursor.execute(sql % val)
            mydb.commit()

            val = (b, a)
            print("RELATO COM ID = '%s' MARCADO COMO '%s'", val)
            cursor.execute(
                "select r.id_relato, r.status, p.categoria, r.descricao, r.data, l.rua from relato as r "
                           "inner join problema as p on r.id_relato = p.id_problema join localizacao as l on "
                           "r.ID_relato = l.ID_localizacao where r.id_relato = '%s' order by "
                           "p.categoria" % b)
            for x in cursor:
                print(x)

            MenuFunc()

        # SAIR DO APLICATIVO
        if numero == '3':
            print("########## FAZENDO LOG OFF ##########")
            print("------------------------------------")
            quit()

    except:
        print("##### ALGO DEU ERRADO #####\n##### Chame Roque #####")
        pass
        MenuFunc()


# INICIALIZAÇÃO DO APLICATIVO
MenuLogin()
