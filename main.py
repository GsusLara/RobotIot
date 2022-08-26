import urequests 

#Solicitud y direccion de la API
res = urequests.get(url='https://direccion/web/acá')
#REspuesta del servidor en consola
print(res.text)