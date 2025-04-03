#santiago

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
    num = input("digite um numero")
    if validarValor(num, int) == True:
        num = int(num)
        print("o antecesor de %d é %d" %(num, num-1))
        i = 0
    else:
        print("valor digitado não é um numero")
        



