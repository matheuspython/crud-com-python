import mysql.connector


conexao= mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Acesso@123",
  database = "dbboessoal"
)
cursor = conexao.cursor()

def create(name, value):
  comando = f'INSERT into vendas (nome_produto, valor) VALUES ("{name}", "{value}")'#
  cursor.execute(comando)#executa comando
  readDatabase()

def readDatabase():
  comando = f'SELECT * FROM vendas'
  cursor.execute(comando)
  resultado = cursor.fetchall()
  print(resultado)

def updateDatabase(name, value):
  comando = f'UPDATE vendas SET valor = {value} WHERE nome_produto = "{name}"'
  cursor = conexao.cursor()
  cursor.execute(comando)
  
  readDatabase()
 
def delete(name):
  comando = f'DELETE FROM vendas where nome_produto = "{name}"'
  cursor = conexao.cursor()
  cursor.execute(comando)
  conexao.commit()
  readDatabase()
  
   




def main():
    while True:
        print("1. Criar um novo produto")
        print("2. Atualizar o valor de um produto")
        print("3. Deletar um produto")
        print("4. Visualizar todos os produtos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            name = input("Digite o nome do produto: ")
            value = input("Digite o valor do produto: ")
            create(name, value)
        elif opcao == "2":
            name = input("Digite o nome do produto que deseja atualizar: ")
            value = input("Digite o novo valor do produto: ")
            updateDatabase(name, value)
        elif opcao == "3":
            name = input("Digite o nome do produto que deseja deletar: ")
            delete(name)
        elif opcao == "4":
            readDatabase()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()




cursor.close()
conexao.close()