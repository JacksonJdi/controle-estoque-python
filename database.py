import mysql.connector

conexao = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password = "SUA_SENHA",
    database = "estoque"
)

cursor = conexao.cursor()

conexao.commit()

print("Produto cadastrado!")