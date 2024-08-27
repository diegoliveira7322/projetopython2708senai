

def calcular_reajuste(salario):

    if salario > 5000:
        reajuste = salario * 0.10  # 10% de reajuste
    else:
        reajuste = salario * 0.15  # 15% de reajuste
    salario_reajustado = salario + reajuste
    return salario_reajustado

def main():
    
   
        salario = float(input("Digite o seu salário: R$ "))
        
        # Calcula o salário reajustado
        salario_reajustado = calcular_reajuste(salario)
        
        # Exibe o resultado
        print(f"Salário original: R$ {salario:.2f}")
        print(f"Salário reajustado: R$ {salario_reajustado:.2f}")
    
   
        print("Por favor, insira um valor de salário válido.")
