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
distancia = 0
gasolina =0

while i != 0:
    
    if distancia == 0:
        distancia = input("qual foi a distancia que o carro percorreu? ")
        if validarValor(distancia, float):
            distancia = float(distancia)
        else:
            distancia = 0
    elif gasolina == 0:
        gasolina = input("quanto de gasolina foi gasto em litros? ")
        if validarValor(gasolina, float):
            gasolina = float(gasolina)
        else:
            gasolina = 0
    else:
        print("o carro fez %.2f kilometros por lintro"%(distancia/gasolina))
        i = 0
         
