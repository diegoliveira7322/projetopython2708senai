nota1 =float(input("Digite uma nota"))
nota2 =float(input("Digite outra nota"))
nota3 =float(input("Digite a terceira nota"))

try:

    def soma (nota1,nota2,nota3):
        resultado = float (nota1,nota2,nota3)/ 3
      
        if (nota1 < 0 or nota2 < 0 or nota3 < 0):
            print("Digite uma nota maior que a media")

        return resultado

    res = soma (nota1,nota2,nota3)
    print(res)

except:
    print("digite uma nota!")
      