#Collect an email address from the user and then find
#out if the user has a custom domain name or a popular domain name. 


Dominios_populares = {
"gmail": "Google",
"hotmail":"Microsoft",
"yahoo":"Yahoo",
"outlook":"Microsoft"}

usuario_correo = input("cual es tu direccion de correo electronico? ")

usuario_nombre = usuario_correo.split('@')[0]
usuario_dominio = usuario_correo.split('@')[-1]
usuario_dominio = usuario_dominio.split('.')[0]

if usuario_dominio in Dominios_populares.keys():
    print(f"hey {usuario_nombre} al parecesr tu correo esta registrado con {Dominios_populares[usuario_dominio]}!")
else:
    print(f"Hey {usuario_nombre} parece que tienes tu propio dominio personalizado en {usuario_dominio}!")