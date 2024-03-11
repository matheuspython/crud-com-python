# CRUD Python com MySQL

Este é um simples aplicativo de CRUD (Create, Read, Update, Delete) em Python usando MySQL como banco de dados.

## Pré-requisitos

- Python 3.x instalado
- MySQL Server instalado e em execução
- Pacote `mysql-connector-python` instalado (pode ser instalado via `pip install mysql-connector-python`)

## Configuração do Banco de Dados

Antes de executar o aplicativo, certifique-se de ter um banco de dados MySQL criado. Você pode criar um banco de dados executando o seguinte comando no terminal MySQL:

CREATE DATABASE dbboessoal;


Além disso, você deve criar uma tabela `vendas` com as colunas `nome_produto` e `valor`.


CREATE TABLE vendas (
id INT AUTO_INCREMENT PRIMARY KEY,
nome_produto VARCHAR(255) NOT NULL,
valor DECIMAL(10, 2) NOT NULL
);


## Utilização

Execute o script `app.py` e siga as instruções apresentadas no console para interagir com o aplicativo. Você pode criar novos produtos, atualizar valores de produtos existentes, deletar produtos e visualizar todos os produtos no banco de dados.

## Estrutura do Código

O código do aplicativo consiste em funções para realizar operações CRUD no banco de dados e uma função principal (`main()`) que gerencia a interação com o usuário através do console.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
