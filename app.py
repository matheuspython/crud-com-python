import mysql.connector


conexao= mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Acesso@123",
  database = "dbboessoal"
)
cursor = conexao.cursor()
#create data 
nome_produto = "toddynho"
valor = 3

comando = f'INSERT into vendas (nome_produto, valor) VALUES ("{nome_produto}", "{valor}")'#comando

cursor.execute(comando)#executa comando

# conexao.commit()#edita o banco de dados
#resultado = cursor.fetchall()#ler o banco de dados

#read data
comando = f"SELECT * FROM vendas"
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)



#update
# nome_produto = "toddynho"
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()#edita o banco de dados

#delete
# nome_produto = "toddynho"
# valor = 6
# comando = f'DELETE FROM vendas where nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()







cursor.close()
conexao.close()