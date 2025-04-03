#santiago
import math
def validarValor(valor, tipo):
    if tipo == str:
        if type(valor) == str and valor.isdigit() == False:
            return True
        else:
            return False
    elif tipo == int :
        if valor.isdigit():
            valor = int(valor)
            if type(valor) == int:
                return True
            else:
                return False
        else:
            return False
    elif tipo == float:
        valor = float(valor)
        if type(valor) == float:
            valor = float(valor)
            if type(valor) == float:
                return True
            else:
                return False
        else:
            return False
i = 1
nota1 = 0
nota2 = 0 
while i != 0:
    if nota1 == 0:
        nota1 = input("forneça a nota da primeira prova")
        if validarValor(nota1, float): 
            nota1 = float(nota1)
        else:
            print("valor fornecido não é valido!")
            nota1 = 0
    elif nota2 == 0:
        nota2 = input("forneça a nota da segunda prova")
        if validarValor(nota2, float): 
            nota2 = float(nota2)
        else:
            print("valor fornecido não é valido!")
            nota1 = 0
    else:
        mediaPonderada = ((nota1*2.3)+(nota2*5))/(2.3+5)
        print("dado as seguintes notas %.2f e %.2f e levando en consideração os pessos 2,3 e 5 a media ponderada é %.2f" %(nota1, nota2, mediaPonderada))
        i = 0

