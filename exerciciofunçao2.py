# função com parâmetro e retorno(return)
def numero(num):
    if num % 2 == 0:
     return "PAR"
    else:
     return "IMPAR"
  
resultado = input(int (numero("Digite um numero")))
print(resultado)      