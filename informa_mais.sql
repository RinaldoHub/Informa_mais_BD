DROP DATABASE IF EXISTS informa_mais
CREATE DATABASE informa_mais
CREATE TABLE Endereco (ID_endereco INTEGER NOT NULL AUTO_INCREMENT, cep VARCHAR(10), cidade VARCHAR(10), bairro VARCHAR(20), rua VARCHAR(25), numero VARCHAR(4), PRIMARY KEY(ID_endereco)) Engine=InnoDB
CREATE TABLE Cidadao (ID_cidadao INTEGER NOT NULL AUTO_INCREMENT,ID_endereco INTEGER, nome VARCHAR(30),data_nascimento DATE, telefone VARCHAR(12), email VARCHAR(35), senha VARCHAR(16), PRIMARY KEY(ID_cidadao)) Engine=InnoDB
CREATE TABLE Relato (ID_relato INTEGER NOT NULL AUTO_INCREMENT, ID_cidadao INTEGER, ID_problema INTEGER, ID_funcionario INTEGER, ID_localizacao INTEGER, descricao VARCHAR(100), data DATETIME, status VARCHAR(15), PRIMARY KEY(ID_relato)) Engine=InnoDB
CREATE TABLE Problema (ID_problema INTEGER NOT NULL AUTO_INCREMENT, categoria VARCHAR(20), subcategoria VARCHAR(20) , PRIMARY KEY(ID_problema)) Engine=InnoDB
CREATE TABLE Localizacao (ID_localizacao INTEGER NOT NULL AUTO_INCREMENT, cep VARCHAR(10), rua VARCHAR(15), cidade VARCHAR(15), bairro VARCHAR(20), PRIMARY KEY (ID_localizacao)) Engine=InnoDB
CREATE TABLE Funcionario_publico (ID_funcionario INTEGER NOT NULL AUTO_INCREMENT, nome VARCHAR(30) , orgao_empresa VARCHAR(15),  email_institucional VARCHAR(35), senha VARCHAR(16) , PRIMARY KEY(ID_funcionario)) Engine=InnoDB
ALTER TABLE Cidadao ADD CONSTRAINT FK_Cidadao_Endereco FOREIGN KEY (ID_endereco) REFERENCES Endereco (ID_endereco)
ALTER TABLE Relato ADD CONSTRAINT FK_Relato_Cidadao FOREIGN KEY (ID_cidadao) REFERENCES Cidadao (ID_cidadao)
ALTER TABLE Relato ADD CONSTRAINT FK_Problema_Relato FOREIGN KEY (ID_problema) REFERENCES Problema (ID_problema)
ALTER TABLE Relato ADD CONSTRAINT FK_Funcionario_Relato FOREIGN KEY (ID_funcionario) REFERENCES Funcionario_publico (ID_funcionario)
ALTER TABLE Relato ADD CONSTRAINT FK_Localizacao_Relato FOREIGN KEY (ID_localizacao) REFERENCES Localizacao (ID_localizacao)