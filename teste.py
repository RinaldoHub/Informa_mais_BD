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

#Aqui é onde a mágica acontece. Através dessa linha executando esse método, o que
#estiver entre as aspas duplas será executado no Banco propriamente dito.
#Resumindo, é a ÚNICA parte do código que iramos mexer, por enquanto
cursor.execute("CREATE DATABASE INFORMA_MAIS")

cursor.execute("CREATE TABLE Relato (
               Descricao VARCHAR(100) NOT NULL,
               ID_Relato INTEGER NOT NULL, 
               Data DATETIME NOT NULL, 
               Status BIT NOT NULL, 
               PRIMARY KEY(ID_Relato))")

cursor.execute("CREATE TABLE Midia (
               ID_Relato INTEGER, 
               Foto BLOB, 
               Video BLOB)")

cursor.execute("CREATE TABLE Problema (
               ID_Relato INTEGER NOT NULL, 
               Categoria VARCHAR(20) NOT NULL, 
               Subcategoria VARCHAR(20) NOT NULL, 
               PRIMARY KEY(Categoria))")

cursor.execute("CREATE TABLE Localizacao (
               ID_Relato INTEGER NOT NULL, 
               Rua VARCHAR(15) NOT NULL, 
               Bairro VARCHAR(20) NOT NULL, 
               Cidade VARCHAR(15) NOT NULL, 
               CEP VARCHAR(10) NOT NULL)")

cursor.execute("CREATE TABLE Prestador de Serviços Publicos (
               nome VARCHAR(30) NOT NULL, 
               Orgao_empresa VARCHAR(15) NOT NULL, 
               ID_Funcionario INTEGER NOT NULL, 
               PRIMARY KEY(ID_Funcionario))")

cursor.execute("CREATE TABLE Endereco (
               email_cidadao VARCHAR(35) NOT NULL, 
               Rua VARCHAR(25) NOT NULL, 
               Bairro VARCHAR(20) NOT NULL, 
               Cidade VARCHAR(15) NOT NULL, 
               CEP VARCHAR(10) NOT NULL, 
               Numero VARCHAR(4) NOT NULL)")

cursor.execute("CREATE TABLE Cidadao (
               nome VARCHAR(30) NOT NULL, 
               email VARCHAR(35) NOT NULL, 
               senha VARCHAR(16) NOT NULL, 
               data_nascimento DATE NOT NULL, 
               telefone VARCHAR(12) NOT NULL, 
               ID_Relato INTEGER NOT NULL, 
               PRIMARY KEY(email))")



#Sinceramente não me lembro pra quê serve isso, mas sei que é necessário
#Quem souber, deixa aqui nos comentários
myresult = mycursor.fetchall()

#Isso daqui não vamos usar, porque digamos que isso "substitui" o SELECT no MySQL
#então o professor não permitiu usar. E pra falar a verdade, achei o SELECT muito
#mais fácil de usar. Não precisamos mexer nessa parte do código
for x in myresult:
    print(x)
