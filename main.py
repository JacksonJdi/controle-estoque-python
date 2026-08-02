from crud import cadastrar,listar,remover_produto,atualizar_qtd_produto,atualizar_preco_produto, buscar_produto


def menu():
    while True:
        print("------CONTROLE DE ESTOQUE------")
        print("1 - Cadastrar produto")
        print("2 - Listar produto")
        print("3 - Atualizar quantidade")
        print("4 - Atualizar preço")
        print("5 - Buscar produto")
        print("6 - Remover produto")
        print("7 - Sair")

        opcao = input("ESCOLHA UMA OPCAO: ")
                
        if opcao == "1":
            cadastrar()
            
        elif opcao == "2":
            listar()
            
        elif opcao == "3":
            print("Quantidade atualizada")
            atualizar_qtd_produto()

        elif opcao == "4":
            print("Preço atualizado")
            atualizar_preco_produto()
        
        elif opcao == "5":
            print("Buscando produto")
            buscar_produto()
            
        elif opcao == "6":
            remover_produto()  

        
        elif opcao == "7":
            print("SAINDO DO MENU")  
                
        else:
            print("OPÇAO INVALIDA")

menu()