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

vendasMes = 0
nomeV = 0
salFix = 0

while i != 0:
  if nomeV == 0:
    nomeV = input("qual o nome do vendedor?")
    if validarValor(nomeV, str):
      nomeV == str(nomeV)
    else:
      nomeV = 0
      print("o valor fornecido invalido")
  elif salFix == 0:
    salFix = input("qual o salario fixo do vendedor?")
    if validarValor(salFix, float):
      salFix = float(salFix)
    else:
      salFix = 0
      print("o valor fornecido invalido")
      
  elif vendasMes == 0:
    vendasMes = input("qual o valor vendido pelo vendedor?")
    if validarValor(vendasMes, float):
      vendasMes = float(vendasMes)
    else:
      vendasMes = 0
      print("o valor fornecido invalido")
  else:
    comi = (vendasMes*15)/100
    print("o valor do salario de %s somada com sua comição é R$ %.2f" %(nomeV, salFix+comi))
    i = 0
    
  
    
  
  
