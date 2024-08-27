base =int(input("Digite o valor da base:"))
altura = int(input("Digite o valor:"))

def area(base,altura):
  resultado = base * altura / 2
  return  resultado

res = area(base,altura)
print(f"AREA DO TRIANGULO É {res}")
