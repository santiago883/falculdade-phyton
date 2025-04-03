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

nome = 0
nota1 = 0
nota2 = 0
nota3 = 0

while i != 0:
    if nome == 0:
        nome = input("escreva seu nome! ")
        if validarValor(nome, str) == False:
            print("valor invalido! ")
            nome = 0
    elif nota1 == 0:
        nota1 = input("escreva sa nota da primeira prova! ")
        if validarValor(nota1, float):
            nota1 = float(nota1)
        else:
            print("valor invalido! ")
            nota1 = 0

    elif nota2 == 0:
        nota2 = input("escreva sa nota da segunda prova! ")
        if validarValor(nota2, float):
            nota2 = float(nota2)
        else:
            print("valor invalido! ")
            nota2 = 0

    elif nota3 == 0:
        nota3 = input("escreva sa nota da segunda prova! ")
        if validarValor(nota3, float):
            nota3 = float(nota3)
        else:
            print("valor invalido! ")
            nota3 = 0
    else:
        media = (nota1 + nota2 + nota3)/3
        print("aluno: %s media aritmética é %.2f "%(nome, media))
        i = 0