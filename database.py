import mysql.connector

conexao = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password = "020305",
    database = "estoque"
)

cursor = conexao.cursor()

conexao.commit()
