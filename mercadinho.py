compras = []
valor_total = 0
print("Bem-vindo ao mercadinho do Seu Zé")
opcao = input("Deseja realizar compras? \ns(sim) \nn(Não)\n")

if opcao != "n":
    print("\nVamos começar as compras")
    
    while opcao != "n":
        produtos = input("\nQual produto você deseja comprar? ")
        valor = float(input("\nQual o valor? R$"))
        compras.append(produtos)
        valor_total += valor
        opcao = input("Deseja realizar outra compra? \ns(sim) \nn(Não)\n")
    
    print(f"\nVocê comprou os seguintes itens: {', '.join(compras)}")
    print(f"O valor total da sua compra foi de R${valor_total:.2f}")
    print("Volte sempre!")
    
else:
    print("Volte sempre!")
