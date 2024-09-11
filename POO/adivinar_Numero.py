def multiplo(number, secrect_number):
  if number % secrect_number == 0:
    print(f"{number} es multiplo del numero secreto")
  elif secrect_number % number == 0:
    print(f"{number} es multiplo del numero secreto")
  else:
    print(f"{number} no es multiplo del numero secreto")

secret_number = 20
while True:
  number = input(("Adivina el numero: "))

  try:
    number = int(number)
  except:
    print("Lo siento, eo que tecleaste no es un numero")
    continue
  
  if number != secret_number:
    if number > secret_number:
      print(f"{number} es mayor que el numero secreto")
      multiplo(number, secret_number)
    elif number < secret_number:
      print(f"{number} es menor que el numero secreto")
      multiplo(number, secret_number)
  else:
    print("Adivinaste el numero secreto")
    break