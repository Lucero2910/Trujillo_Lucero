
nombre = input("¿Cual es tu nombre? ")
apellido = input("¿Cual es tu primer apellido ")
segundoapellido = input("¿Cual es tu segundo apellido? ")
nombre_lower = nombre.lower()
apellido_lower = apellido.lower()
segundoapellido_lower = segundoapellido.lower()


año_de_nacimiento = input("En que año naciste? ")
fecha = input("¿En qué mes y día naciste?(“DD/MM”) ")



año_actual = 2023
print(f"Este es tu nombre completo en mayúsculas {nombre} {apellido}{segundoapellido}")
print(f"Este es tu nombre completo en minusculas {nombre.lower} {apellido.lower} {segundoapellido.lower}")
print(f"Esta es tu fecha de nacimiento “dd-mm-aaaa” {fecha} {año_de_nacimiento}")
print(año_actual - año_de_nacimiento)
