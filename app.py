import mysql.connector


conexao= mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Acesso@123",
  database = "dbboessoal"
)

cursor = conexao.cursor()

cursor.close()
conexao.close()