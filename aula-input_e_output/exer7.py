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

vhora = 0
htrab = 0

while i != 0:
    if vhora == 0:
        vhora = input("quanto tu ganha por hora? ")
        if validarValor(vhora, float):
            vhora = float(vhora)
        else:
            vhora = 0
    elif htrab == 0:
        htrab = input("quantas horas tu trabalha por mês? ")
        if validarValor(htrab, float):
            htrab = float(htrab)
        else:
            htrab = 0
    else:
        print("voce ganhou %.2f este mês! "%(htrab* vhora))
        i = 0

