import mysql.connector #Importamos o concector MySQL que implementa o Banco

import datetime


#Aqui vai as credenciais do nosso banco. Isso varia entre as máquinas, então por enquanto não foquemos aqui
#e sim nos códigos SQL
mydb = mysql.connector.connect(
   host = "localhost",
   user = "root",
   password = "",
   database = ""
)

#O cursor precisa ser criado para que possamos executar os códigos SQL no Python
#Lembra bastante os Objetos em Java.
cursor = mydb.cursor(prepared=True)

#O código de DDL está COMENTADO para não haver duplicidade ou erro nos testes
"""
#Aqui é onde a mágica acontece. Através dessa linha executando esse método, o que
#estiver entre as aspas duplas será executado no Banco propriamente dito.
cursor.execute("CREATE DATABASE INFORMA_MAIS")

cursor.execute("USE INFORMA_MAIS")

cursor.execute("CREATE TABLE Relato (\
              Descricao VARCHAR(100) NOT NULL,\
              ID_Relato INTEGER NOT NULL,\
              Data DATETIME NOT NULL,\
              Status BIT NOT NULL,\
              PRIMARY KEY(ID_Relato)) ENGINE=InnoDB")\

cursor.execute("CREATE TABLE Midia (\
              ID_Relato INTEGER,\
              Foto BLOB,\
              Video BLOB) ENGINE=InnoDB")\

cursor.execute("CREATE TABLE Problema (\
              ID_Relato INTEGER NOT NULL,\
              Categoria VARCHAR(20) NOT NULL,\
              Subcategoria VARCHAR(20) NOT NULL,\
              PRIMARY KEY(Categoria)) ENGINE=InnoDB")\

cursor.execute("CREATE TABLE Localizacao (\
              ID_Relato INTEGER NOT NULL,\
              Rua VARCHAR(15) NOT NULL,\
              Bairro VARCHAR(20) NOT NULL,\
              Cidade VARCHAR(15) NOT NULL,\
              CEP VARCHAR(10) NOT NULL) ENGINE=InnoDB")\

cursor.execute("CREATE TABLE Funcionario_Publico (\
              nome VARCHAR(30) NOT NULL,\
              Orgao_empresa VARCHAR(15) NOT NULL,\
              ID_Funcionario INTEGER NOT NULL,\
              PRIMARY KEY(ID_Funcionario)) ENGINE=InnoDB")\

cursor.execute("CREATE TABLE Endereco (\
              email_cidadao VARCHAR(35) NOT NULL,\
              Rua VARCHAR(25) NOT NULL,\
              Bairro VARCHAR(20) NOT NULL,\
              Cidade VARCHAR(15) NOT NULL,\
              CEP VARCHAR(10) NOT NULL,\
              Numero VARCHAR(4) NOT NULL) ENGINE=InnoDB")\

cursor.execute("CREATE TABLE Cidadao (\
              id_cidadao INTEGER NOT NULL,\
              nome VARCHAR(30) NOT NULL,\
              email VARCHAR(35) NOT NULL,\
              senha VARCHAR(16) NOT NULL,\
              data_nascimento DATE NOT NULL,\
              telefone VARCHAR(12) NOT NULL,\
              ID_Relato INTEGER NOT NULL,\
              PRIMARY KEY(id_cidadao)) ENGINE=InnoDB")

#Aqui está a CIRAÇÃO DAS FOREIGN KEYS
cursor.execute("ALTER TABLE Cidadao ADD CONSTRAINT FK_Cidadao_Relato FOREIGN KEY (ID_Relato) REFERENCES Relato (ID_Relato)")

cursor.execute("ALTER TABLE Problema ADD CONSTRAINT FK_Problema_Relato FOREIGN KEY (ID_Relato) REFERENCES Relato (ID_Relato)")

cursor.execute("ALTER TABLE Endereco ADD CONSTRAINT FK_Endereco_Cidadao FOREIGN KEY (email_cidadao) REFERENCES Cidadao (email)")

cursor.execute("ALTER TABLE Midia ADD CONSTRAINT FK_Midia_Relato FOREIGN KEY (ID_Relato) REFERENCES Relato (ID_Relato)")

cursor.execute("ALTER TABLE Localizacao ADD CONSTRAINT FK_Localizacao_Relato FOREIGN KEY (ID_Relato) REFERENCES Relato (ID_Relato)")

cursor.execute("INSERT INTO Cidadao VALUES(0, 'Jose', 'jose@email.com', 'jose1234', '15/05/1985', '83986571374')")
"""
#Esse método fetchall() recupera as linhas de uma consulta
#e retorna uma lista de tuplas onde cada tupla é uma linha
#mas o código funciona sem ele
#myresult = cursor.fetchall()

#TELA DE INTRODUÇÃO e decoração pro código
print("########## CONSOLE MYSQL ##########\nPara sair, digite -1\n")
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
   # INICIALIZAÇÃO DE VARIÁVEIS
   tabela = "0"

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
            print("")

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
                     sql = "SELECT * FROM LOCALIZACAOELATO WHERE %s LIKE '%s'"
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

         elif (numero == '5'):
            break
         print("------------------------------------")
         MenuPrincipal()


#Como o DATETIME funciona
"""a = datetime.datetime.now().isoformat()
print(a)
sql = "INSERT INTO RELATO(data) VALUES(%a)"

val = (a)
cursor.execute(sql % val)
mydb.commit()
cursor.execute("select * from relato")
for x in cursor:
   print(x)"""

#Esta é a forma como se deve formatar a função de PESQUISA em Python
"""
a = input("")
b = input("")
sql = "SELECT * FROM RELATO WHERE %s LIKE '%s'"
val = (a, "%" + b + "%",)
print(sql % val)
cursor.execute(sql % val)
for x in cursor:
   print(x)
"""
#ORDEM DE MENUS
#MenuLogin()
MenuPrincipal()

"""
#Aqui está a INTERAÇÃO COM O USUÁRIO
while True:
   try: #O try é utilizado para "tentar" executar o código
      command = input("SQL>") #Aqui o input será atribuído à variável "command"
      if(command == '-1'): #caso o usuário digite -1 o console será fechado
         print("########## CONSOLE MYSQL FECHADO ##########")
         break
      cursor.execute(command) #O cursor mandará executar o input dado em "command"
      for x in cursor: #O for faz uma varredura no comando do input e printa o que resgatou
         print(x)
   except: #E caso o código haja erros de sintaxe, ele avisa e volta para o começo do loop
      print("***ERRO DE SINTAXE SQL***")
      pass"""
