#estoque de produtos, com cada estoque, tendo estoque de alimentos, bebidas, produtos de limpeza.
#cada estoque tem seu produtos, no maximo de 8 listas de produtos em um estoque.
#passar no caixa para ver quanto vai custar, o caixa pergunta cartao ou dinheiro, sendo dinheiro tendo um desconto de 15%, e no cartao o valor encheio.
import pandas as pd
alimentos= pd.DataFrame({
    "indice": [1,2,3,4,5,6,7,8,9],
    "produto": ["Pao de sal", "Farofa pronta", "Frango desfiado", "Carne bovina", "Feijao", "Arroz branco", "Salgadinho de pacote", "Cartela de ovos", "Manteiga"],
    "preço":[5.50, 8.90, 19.90, 36.90, 9.80, 22.90, 6.50,	9.90, 4.80],
    "categoria": ["alimentos"] * 9 #aqui vai imprimir 9 vezes a categoria 
})
bebidas= pd.DataFrame({
    "indice": [1,2,3,4,5,6,7,8,9],
    "produto":["Cerveja", "Refrigerantes", "Caldo de Cana", "Cafe", "Energeticos", "Cha", "Pacotinho de Suco", "Agua com Gas", "Corotinho"],
    "preço": [3.50, 7.90, 4.00, 39.90, 10.50, 5.20, 0.80, 2.50, 5.90],
    "categoria": ["bebidas"] * 9 
})
produtos_de_limpeza= pd.DataFrame({
    "indice": [1,2,3,4,5,6,7,8,9],
    "produto": ["Detergente Liquido", "Candida", "Desengordurante", "Vassoura", "Balde", "Multiuso", "Desinfetante", "Rodo", "Pano de Microdibras"],
    "preço": [2.50, 4.20, 6.90, 14.90, 12.00, 5.80, 5.50, 19.90, 3.50],
    "categoria": ["produtos de limpeza"] * 9
})
doces_sobremesas= pd.DataFrame({
    "indice": [1,2,3,4,5,6,7,8,9],
    "produto": ["Chocolate em barra", "Bala de goma","Pirulito", "Gelatina em pó", "Rosquinha doce", "Doce de leite", "Achocolatado em pó", "Biscoito recheado", "Picolé"],
    "preço": [5.99, 2.89, 0.75, 2.49, 6.99, 7.50, 6.49, 3.29, 4.00],
    "categoria": ["doces e sobremesas"]* 9
})
massas_molhos= pd.DataFrame({
    "indice": [1,2,3,4,5,6,7,8,9],
    "produto": ["Macarrão penne", "Macarrão instantâneo", "Lasanha congelada", "Molho de tomate", "Molho branco", "Extrato de tomate", "Azeite de oliva", "Parmesão ralado", "Orégano"],
    "preço": [ 5.79, 2.39, 17.90, 3.49, 4.99, 2.99, 24.90, 6.50, 1.89],
    "categoria": ["massas e molhos"] * 9
})
prateleira= pd.concat([ #nossa prateleira !!!
    alimentos,
    bebidas,
    produtos_de_limpeza,
    doces_sobremesas,
    massas_molhos
],ignore_index=True)

#todas as pratileiras e nomes 
print("Seja bem vindo ao Mercadin!")
#aqui fica o menu principal aonde sera sempre usado
def mostrar_prateleira(categoria_escolhida): #troca de nome 
    if categoria_escolhida in prateleira["categoria"].unique(): 
        produtos = prateleira[prateleira["categoria"] == categoria_escolhida]
        print(f"\n Produto disponiveis na prateleira '{categoria_escolhida.title()}': ") #filtra a categoria/prateleira escolhida e tira o indice do pandas e deixa bonito a categoria escolhida
        print(produtos[["indice", "produto", "preço"]].to_string(index=False))
    else:
        print("Prateleira invalida")

def mostrar_carrinho():
    if not carrinho:
        print("Seu carrinho esta vazio.")
        return
    total = 0
    for item in carrinho:
        print(f"{item['produto']} - R$ {item["preço"]:.2f}")#visualizar o carrinho 
        total += item ["preço"]
    print(f"Total: R${total:.2f}")        

def menu_principal():
    escolha_prateleira= ""
    while escolha_prateleira != "sair":
        print("Prateleira do Mercadin: \nAlimentos \nBebidas \nProdutos de limpeza \nDoces e Sobremesas \nMassas e Molhos \nTudo para sua casa!!!")
        
        escolha_prateleira= input("Escreva o nome da prateleira ou 'sair': ").lower().strip()
        
        print("----------------------------------------------")
        
        # Verifica se o usuário quer sair do mercado
        if escolha_prateleira == "sair":
            print("Obrigado por visitar o Mercadin")
            break  # Encerra o loop principal do menu
        # Verifica se o usuário quer ver o carrinho
        elif escolha_prateleira == "carrinho": 
            mostrar_carrinho() #mostra o carrinho 
            continue
        elif escolha_prateleira not in prateleira["categoria"].unique():
            print("Prateleira invalida, tente novamente ")
            continue # Volta para o início do menu principal
        #se tudo passou certo, agora o usuario entra na prateleira 
        while True:
            mostrar_prateleira(escolha_prateleira)  # Mostra todos os produtos disponíveis na prateleira escolhida
            try:
                escolha_indice = int(input("Digite o numero do produto: "))
            except ValueError:
                print("Numero invalido, tente novamente")
                continue #se algum numero estiver errado, ele volta tudo de novo
            
             # Filtra os produtos disponíveis da prateleira atual
            produto_disponivel= prateleira[prateleira["categoria"] == escolha_prateleira]
            
            #Filtra o produto com base no número digitado
            produto_escolhido= produto_disponivel[produto_disponivel["indice"]== escolha_indice]
             # Verifica se o produto foi encontrado
            if not produto_escolhido.empty: #empty verifica se esta vazio ou nao 
                carrinho.append({   # Adiciona o produto ao carrinho
                    "produto": produto_escolhido.iloc[0]["produto"],
                    "preço": produto_escolhido.iloc[0]["preço"]
                })
                print(f"\n '{produto_escolhido.iloc[0]['produto']} Adicionario no carrinho")
            else: #se o produto nao for encontrado, ele avisa e repete a pergunta de novo 
                print("Produto não encontrado, verificar o numero de novo")
                continue 
            print("-----------------------------------------")
            #menu de opçoes do mercado
            print("\nO que você deseja fazer agora?")
            print("1 - Adicionar um produto dessa mesma prateleira")
            print("2 - Voltar ao menu de prateleiras")
            print("3 - Ver carrinho")
            print("4 - Sair")
            escolha = input("Escolha uma dessas opções: ").strip()
            if escolha == "1":
                continue
            elif escolha == "2":
                break
            elif escolha == "3":
                mostrar_carrinho()
                break
            elif escolha == "4":
                print("Muito obrigado, volte mais tarde")
                return
            else:
                print("Opção errada, voltando ao menu das prateleiras") 
carrinho=[]

menu_principal()
#escolher a pratilheira do mercado ou sair dele, proximo passo seria colocar para escolher os produtos e adicionar e remover do carrinho 
#Usuário escolhe prateleira,  Mostra os produtos
#Pergunta: "Deseja comprar algo? Digite o número do produto ou 'voltar'",  Adiciona ao carrinho se for número válido
#Loopa até ele digitar 'voltar',  De volta ao menu principal
#A qualquer momento pode digitar 'carrinho' para ver os itens ou 'remover'

