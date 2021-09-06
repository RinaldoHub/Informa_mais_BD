import mysql.connector #Importamos o concector MySQL que implementa o Banco

import datetime


#Aqui vai as credenciais do nosso banco. Serve para realizar a conexão do plugin do python com o BD
mydb = mysql.connector.connect(
   host = "localhost",
   user = "root",
   password = "",
   database = ""
)
#O cursor precisa ser criado para que possamos executar os códigos SQL no Python
#Lembra bastante os Objetos em Java.
cursor = mydb.cursor(prepared=True)

#Aqui o Python irá abrir o arquivo .sql com os comandos DDL para criação do nosso banco
if mydb.database == 'None':
   f = open("informa_mais.sql", "r")
   for x in f:
      cursor.execute(f)
   f.close()

#TELA DE INTRODUÇÃO e decoração pro código
print("########## BEM-VINDO(A) AO INFORMA+ ##########\nPara sair, digite -1\n")
print("BANCO DE DADOS ATIVO: %s\nUSUÁRIO: %s\n" % (mydb.database, mydb.user))
"""
#TELA PRINCIPAL
def MenuLogin():
   print("------------------------------------\n")
   print("########## TELA PRINCIPAL ##########")
   print("1 - LOGIN\n2 - CADASTRAR\n")
   numero = input("O que deseja?\n")

   if(numero == '1'):
      Login()

   elif(numero == '2'):
      Cadastrar()

   #elif(numero == '3'): break

   elif(numero != 1 or 2 or 3):
      print("ESCOLHA UMA OPÇÃO VÁLIDA")

def Login():
   print("------------------------------------\n")
   print("########## TELA DE LOGIN ##########")
   user = input("Digite seu Username:")
   senha = input("Digite sua Senha: ")
   print("ACESSO AUTORIZADO")
   MenuPrincipal()

def Cadastrar():
   print("------------------------------------\n")
   print("########## TELA DE CADASTRO ##########")
   user = input("Digite seu Username:")
   senha = input("Digite sua Senha: ")
   print("ACESSO AUTORIZADO")
   MenuPrincipal()
"""



#FUNÇÃO DA TABELA
def MenuPrincipal():
   while True:
         print("------------------------------------\n")
         print("########## MENU PRINCIPAL ##########")
         print("1 - MOSTRAR TABELAS\n2 - INSERIR DADOS NA TABELA\n3 - ATUALIZAR DADOS\n4 - PESQUISAR DADOS\n5 - SAIR\n")
         numero = input("O que deseja?\n>")

         #MOSTRAR TABELAS
         if (numero == '1'):
            cursor.execute("SHOW TABLES")
            for x in cursor:  # O for faz uma varredura no comando do input e printa o que resgatou
               print(x)

            print("\n1 - RELATO\n2 - CIDADÃO\n3 - FUNCIONÁRIO PÚBLICO\n4 - ENDEREÇO\n5 - PROBLEMA\n6 - LOCALIZAÇÃO\n7 - MIDIA\n")
            tabela = input("Deseja visualizar todos os dados de alguma tabela?\nSe sim, digite o número dela\nSe não, digite '-1'\n>")

            while tabela != '-1':
               if tabela == '1':
                  print("") #Quebra de linha
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
               print("1 - RELATO 2 - CIDADÃO 3 - FUNCIONÁRIO PÚBLICO 4 - ENDEREÇO 5 - PROBLEMA 6 - LOCALIZAÇÃO 7 - MIDIA")
               tabela = input("Deseja visualizar alguma outra tabela?\nSe sim, digite o número dela\nSe não, digite '-1'\n>")

         #INSERIR DE DADOS
         elif (numero == '2'):
            print("------------------------------------\n")
            print("########## INSERÇÃO DE DADOS ##########")
            print("1 - RELATO\n2 - CIDADÃO\n3 - FUNCIONÁRIO PÚBLICO\n4 - ENDEREÇO\n5 - PROBLEMA\n6 - LOCALIZAÇÃO\n7 - MIDIA\n")
            tabela = input('Qual TABELA deseja INSERIR DADOS?\n>')
            while tabela != '-1':
               if tabela == '1':
                  a = input("Descrição: ")
                  b = datetime.datetime.now().isoformat()
                  c = input("Status: (PENDENTE, PUBLICADO, EM ANDAMENTO, DESATIVADO OU RESOLVIDO)\n>")
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
                  val = (a,b,c,d,e)
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
                  val = (a,b,c,d)
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
                  sql = "INSERT INTO ENDERECO(cep, cidade, bairro, rua, numero) VALUES(%s, %a, %a, %a, %a, %a)"
                  val = (a,b,c,d,e,)
                  cursor.execute(sql % val)
                  mydb.commit()
                  cursor.execute("select * from endereco")
                  for x in cursor:
                     print(x)
               elif tabela == '5':
                  a = input("Categoria: ")
                  b = input("Subcategoria: ")
                  sql = "INSERT INTO PROBLEMA(categoria, subcategoria) VALUES(%a, %a)"
                  val = (a,b)
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
                  sql = "INSERT INTO LOCALIZACAO(rua, bairro, cidade, cep)"
                  val = (a,b,c,d)
                  cursor.execute(sql % val)
                  mydb.commit()
                  cursor.execute("select * from localizacao")
                  for x in cursor:
                     print(x)

               print("")  # Quebra de linha
               print(cursor.rowcount,"Dado(s) INSERIDO(s)!\n")
               print(
                  "1 - RELATO 2 - CIDADÃO 3 - FUNCIONÁRIO PÚBLICO 4 - ENDEREÇO 5 - PROBLEMA 6 - LOCALIZAÇÃO 7 - MIDIA")
               tabela = input("Deseja inserir mais dados?\nSe sim, digite o número da tabela\nSe não, digite '-1'\n>")

         #ATUALIZAR DADOS
         elif (numero == '3'):

            print("------------------------------------------\n")
            print("########## ATUALIZAÇÃO DE DADOS ##########")
            print("1 - RELATO\n2 - CIDADÃO\n3 - FUNCIONÁRIO PÚBLICO\n4 - ENDEREÇO\n5 - PROBLEMA\n6 - LOCALIZAÇÃO\n")
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
                  print("") #Quebra de Linha
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
               print(cursor.rowcount,"Dado(s) INSERIDO(s)!\n")
               print(
                  "1 - RELATO 2 - CIDADÃO 3 - FUNCIONÁRIO PÚBLICO 4 - ENDEREÇO 5 - PROBLEMA 6 - LOCALIZAÇÃO")
               tabela = input("Deseja inserir mais dados?\nSe sim, digite o número da tabela\nSe não, digite '-1'\n>")

         #PESQUISAR DADOS
         elif (numero == '4'):
            print("------------------------------------\n")
            print("########## PESQUISA DE DADOS ##########")
            print("1 - RELATO\n2 - CIDADÃO\n3 - FUNCIONÁRIO PÚBLICO\n4 - ENDEREÇO\n5 - PROBLEMA\n6 - LOCALIZAÇÃO\n7 - MIDIA\n")
            tabela = input('Em qual TABELA deseja PESQUISAR?\n>')
            while tabela != '-1':
               if tabela == '1':
                  print("Colunas na TABELA RELATO")
                  cursor.execute("describe relato")
                  for x in cursor:
                     print(x)

                  coluna = input("Coluna que deseja pesquisar: ")
                  pesq = input("O que deseja pesquisar: ")
                  posicao = input("Deseja que sua pesquisa esteja no começo (1), meio (2), ou fim (3) do registo?\n>")

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
                  posicao = input("Deseja que sua pesquisa esteja no começo (1), meio (2), ou fim (3) do registo?\n>")

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
                  posicao = input("Deseja que sua pesquisa esteja no começo (1), meio (2), ou fim (3) do registo?\n>")

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
                  posicao = input("Deseja que sua pesquisa esteja no começo (1), meio (2), ou fim (3) do registo?\n>")

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
                  posicao = input("Deseja que sua pesquisa esteja no começo (1), meio (2), ou fim (3) do registo?\n>")

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
                  posicao = input("Deseja que sua pesquisa esteja no começo (1), meio (2), ou fim (3) do registo?\n>")

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
               print("") #Quebra de linha
               print("1 - RELATO 2 - CIDADÃO 3 - FUNCIONÁRIO PÚBLICO 4 - ENDEREÇO5 - PROBLEMA 6 - LOCALIZAÇÃO")
               tabela = input("Deseja realizar outra pesquisa?\nSe sim, digite o número da tabela\nSe não, digite '-1'\n>")

         #Fechar CONSOLE
         elif (numero == '5'):
            print("########## APLICATIVO ENCERRADO ##########")
            break
         print("------------------------------------")
         MenuPrincipal()

#ORDEM DE MENUS
#MenuLogin()
MenuPrincipal()
