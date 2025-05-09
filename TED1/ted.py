# santiago
nome = input("qual o teu nome?")
genero = input("qual o teu genero M/F?")
idade = int(input("qual a tua idade?"))
altura = float(input("qual a tua altura?"))
peso = float(input("qual o teu  peso?"))
PI = 0

if (genero == "M") or (genero == "m"):
  PI = (72.7*altura)-58
elif (genero == "F") or (genero == "F"):
  PI = (62.1*altura)-44,7
else :
  print("infelizmente o campo genero ")
