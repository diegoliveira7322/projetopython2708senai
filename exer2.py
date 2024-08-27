try:
    dividendo = int(input("Digite o dividendo" ))
    divisor = int(input("Digite o divisor" ))
    resultado = dividendo/divisor


except ValueError:
  print("numero digitado invalido")


except ZeroDivisionError:
   print("divisao por zero não permitida")

   