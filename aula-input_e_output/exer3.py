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

while i != 0:
    raio = input("forneça o raio da esfera")
    if validarValor(raio, int):
        raio = int(raio)
        volumem = (4*3.14*(pow(raio,3)))/3
        print("o valor do volumen dessa esfera é %.2f"%(volumem))
        i = 0
    else:
         print("o valor fornecido nâo é um numero")

