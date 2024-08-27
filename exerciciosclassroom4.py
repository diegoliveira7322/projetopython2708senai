inicio = int(input("Digite o valor inicial"))
fim = int(input("Digite o fim:"))
passo = int(input("Digite o valor de quantidade de passos:"))



def contador(inicio,fim,passo):
 
 if  passo == 0:
     print("Passo não pode ser zero.")
     return

   
print("Contagem normal:")
if inicio < fim:
     for i in range(inicio, fim + 1, passo):
       print(i, end=' ')
else:
   print("Início deve ser menor que o fim para contagem normal.")
print()


 
print("Contagem reversa:")
 
if inicio > fim:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
else:
        print("Início deve ser maior que o fim para contagem reversa.")
print()