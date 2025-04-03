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
val = 0
bas = 0
alt = 0
while i != 0:
    if bas == 0:
        bas = input("digite o valor da basse do retângulo! ")
        val = validarValor(bas, float)
        if val == True:
            bas = float(bas)
            val = 0
        else:
            print("valor fornecido não é um numero")
            bas = 0
            val = 0
    elif alt == 0:
        alt = input("digite o valor da altura do retângulo! ")
        val = validarValor(alt, float)
        if val == True:
            alt = float(alt)
            val = 0
        else:
            print("valor fornecido não é um numero")
            bas = 0
            val = 0
    else:
        print("dado a base %.2f e a altura %.2f a área é %.2f"%(bas, alt, bas*alt))
        i = 0


#print("entrou")
    
    