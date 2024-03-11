import mysql.connector


conexao= mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Acesso@123",
  database = "dbboessoal"
)
cursor = conexao.cursor()

def create(name, value):
  comando = f'INSERT into vendas (nome_produto, valor) VALUES ("{nome}", "{value}")'#
  cursor.execute(comando)#executa comando
  readDatabase()

def readDatabase():
  comando = f'SELECT * FROM vendas'
  cursor.execute(comando)
  resultado = cursor.fetchall()
  print(resultado)

def updateDatabase(name, value):
  comando = f'UPDATE vendas SET valor = {value} WHERE nome_produto = {name}'
  cursor.execute(comando)
  conexao.commit()
  readDatabase()
 
def delete(name, value):
  comando - f'DELETE FROM vendas where nome_produto = {name}'
  cursor.execute(comando)
  conexao.commit()
  readDatabase()
  
  
cursor.close()
conexao.close()