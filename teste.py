import mysql.connector #Importamos o concector MySQL que implementa o Banco

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
cursor = mydb.cursor()

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
              PRIMARY KEY(id)) ENGINE=InnoDB")

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
print("BANCO DE DADOS ATIVO: {0}\nUSUÁRIO: {1}\n".format(mydb.database, mydb.user))

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
      pass
