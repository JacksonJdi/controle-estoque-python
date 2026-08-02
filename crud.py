import json
from database import cursor, conexao

def cadastrar():
        nome    = input("Digite o nome do produto: ")
        while True:
            try:
                qtd = input("Digite a quantiade de produtos: ")
                valor = input("Digite o preço do produto: ")
                qtd = int(qtd)
                valor = float(valor)
                break
            except ValueError: 
                print("DIGITE APENAS NUMEROS!!")
        if valor < 0 or qtd < 0:
            print("VALOR OU QUANTIDADE ERRADA")   
            return     
             
        try:
            cursor.execute (
            "INSERT INTO produtos(nome, quantidade, preco) VALUES(%s,%s,%s)",
            (nome, qtd, valor)
        )
            conexao.commit()
            print("PRODUTO CADASTRADO COM SUCESSO")
        except Exception as erro:
            print(f"ERRO AO CADASTRAR O PRODUTO: {erro}")

         
def listar():
    cursor.execute(
        "SELECT * FROM produtos;"
    )
    produtos = cursor.fetchall()
    for produto in produtos:
        print(f"""
            ID: {produto[0]}
            PRODUTOS: {produto[1]}
            QUANTIDADE: {produto[2]}
            PREÇO: R$ {produto[3]:.2f}
              """)
    if not produtos:
        print("NENHUM PRODUTO CADASTRADO")
        
def remover_produto():
    user_remove = input("DIGITE O ID DO PRODUTO QUE DESEJA REMOVER: ")
    try:
        cursor.execute(
                       "SELECT * FROM produtos WHERE id = %s",
                       (user_remove,))
        produto = cursor.fetchone()  
        
        if produto:
            user_confirma = input("TEM CERTEZA QUE DESEJA REMOVER? S/N: ").lower()
            
            if user_confirma == "s":
                cursor.execute("DELETE FROM produtos WHERE id = %s",
                               (user_remove,)
                               )
                conexao.commit()
                print("Produto removido com sucesso!")
                
            elif user_confirma == "n":
                print("VOLTANDO AO MENU!")
                
            else:
                print("OPCAO INVALIDA!")
                
        else:
            print("PRODUTO NÃO ENCONTRADO!")
            
    except Exception as erro:
        print(f"Erro ao remover produto: {erro}")            
    
        
def atualizar_qtd_produto():
    user_atualiza_id = input("Digite o ID do que produto deseja atualizar? ")
    user_quantidade = input("DIGITE A QUANTIDADE: ")
    try:
        user_atualiza_id = int(user_atualiza_id)
        user_quantidade = int(user_quantidade)
    except ValueError:
        print("ID OU QUANTIDADE INVALIDADE")
        return
                 
    try:
        cursor.execute("UPDATE produtos SET quantidade = %s WHERE id = %s",
        (user_quantidade, user_atualiza_id))
        conexao.commit()
        if cursor.rowcount == 0:
            print("PRODUTO NAO ATUALIZADO")
            return
        print("PRODUTO ATUALIZADO COM SUCESSO")
            
    except Exception as e:
        print(e)
        print("PRODUTO NAO ATUALIZADO")
        return
        
def atualizar_preco_produto():
    user_atualiza_preco_id = input("Digite o ID do que produto deseja atualizar? ")
    user_atualiza_preco = input("Digite o novo preço ")
    
    try:
        user_atualiza_preco_id = int(user_atualiza_preco_id)
        user_atualiza_preco = float(user_atualiza_preco)
        if user_atualiza_preco < 0:
            print("PREÇO INVALIDO")
            return
    except ValueError:
        print("ID OU PREÇO INVALIDO")
        return
    
    try:
       cursor.execute("UPDATE produtos SET preco = %s WHERE id = %s",
                      (user_atualiza_preco, user_atualiza_preco_id)
       )
       
       conexao.commit()
       if cursor.rowcount == 0:
           print("PRODUTO NAO ATUALIZADO")
           return
       print("PRODUTO ATUALIZADO COM SUCESSO")
        
    except Exception as e:    
        print("ERRO AO ATUALIZAR O PRECO")
        print(e)      
      

    
def buscar_produto():
    user_busca_id = input("Digite o ID que seja buscar ") 
    try:
        user_busca_id = int(user_busca_id)
    except ValueError:
        print("ID INVALIDO") 
        return
    try:

        cursor.execute("SELECT * FROM produtos WHERE id = %s",
                   (user_busca_id,))
        produto = cursor.fetchone()
        if produto is None:
            print("PRODUTO NAO ENCONTRADO")
            return
        
        print(f"""
            ID: {produto[0]}
            PRODUTO: {produto[1]}
            QUANTIDADE: {produto[2]}
            PREÇO: R$ {produto[3]:.2f}
              """)         

        
    except Exception as e:
        print("ERRO AO ENCONTRAR O PRODUTO")
        print(e)