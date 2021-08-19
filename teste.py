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
mycursor = mydb.cursor()

#Aqui é onde a mágica acontece. Através dessa linha executando esse método, o que
#estiver entre as aspas duplas será executado no Banco propriamente dito.
#Resumindo, é a ÚNICA parte do código que iramos mexer, por enquanto
mycursor.execute("Código MySQL aqui")

#Sinceramente não me lembro pra quê serve isso, mas sei que é necessário
#Quem souber, deixa aqui nos comentários
myresult = mycursor.fetchall()

#Isso daqui não vamos usar, porque digamos que isso "substitui" o SELECT no MySQL
#então o professor não permitiu usar. E pra falar a verdade, achei o SELECT muito
#mais fácil de usar. Não precisamos mexer nessa parte do código
for x in myresult:
    print(x)
