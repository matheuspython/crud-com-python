import mysql.connector


conexao= mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Acesso@123",
  database = "dbboessoal"
)
cursor = conexao.cursor()

comando = 'INSERT into vendas (nome_produto, valor)'#comando

cursor.execute(comando)#executa comando

conexao.commit()#edita o banco de dados
#resultado = cursor.fetchall()#ler o banco de dados


cursor.close()
conexao.close()