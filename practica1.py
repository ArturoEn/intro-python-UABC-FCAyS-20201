nom = input("como te llamas: ")
print ("hola " + nom)

edad = input ("cuantos años tienes: ")
x = int(edad)
if x < 18:
  print("tienes", x, "años, eres menor de edad")
if x >= 18:
  print("tienes", x, "años, eres mayor de edad")

print("buen día")