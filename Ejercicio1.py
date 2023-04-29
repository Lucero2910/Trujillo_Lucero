
nombre = input("¿Cual es tu nombre? ")
apellido = input("¿Cual es tu primer apellido ")
segundoapellido = input("¿Cual es tu segundo apellido? ")

nombre_lower = nombre.lower()
apellido_lower = apellido.lower()
segundoapellido_lower = segundoapellido.lower()

nombre_upper = nombre.upper()
apellido_upper = apellido.upper()
segundoapellido_upper = segundoapellido.upper()


año_de_nacimiento = int(input("En que año naciste? "))
a, b, c, d, f = input("¿En qué mes y día naciste?(“MM/DD”) ")

año_actual = 2023

a = {año_actual - año_de_nacimiento + 20}
media = mean(a)

print(f"Este es tu nombre completo en mayúsculas {nombre_upper} {apellido_upper}{segundoapellido_upper}")
print(f"Este es tu nombre completo en minusculas {nombre_lower} {apellido_lower} {segundoapellido_lower}")
print("Esta es tu fecha de nacimiento ")
print(d + f + c + a + b) 
print(año_de_nacimiento)
print(f"Tu edad es {año_actual - año_de_nacimiento}")
print(f"Tu nombre completo tiene _________ vocales")
print(f"Tu nombre completo tiene _________ letras")
print("¿Tu edad es un carácter de tipo número? ___True____")
print("¿Tu nombre completo es un carácter de tipo alfanumérico? ___True____")
print(f"Tu edad en 10 años sera {año_actual - año_de_nacimiento +10}")
print(F"La media de tu edad actual y tu edad en 20 años es {media}")