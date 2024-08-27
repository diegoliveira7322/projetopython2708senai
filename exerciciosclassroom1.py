

def verificar_idade(nome, idade):




    if idade >= 18:
        return f"{nome} é maior de idade."
    else:
        return f"{nome} é menor de idade."

def main():
    #o nome e a idade do usuário
    try:
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite a sua idade: "))
        
        resultado = verificar_idade(nome, idade)
        
        # Exibe o resultado
        print(resultado)
    
    except ValueError:
        print("Por favor, insira uma idade válida.")

