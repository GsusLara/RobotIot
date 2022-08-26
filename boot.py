# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import network

global sta_if
# Instanciamos el objeto -sta_if- para controlar la interfaz STA
sta_if = network.WLAN(network.STA_IF)
# COMIENZA EL BUCLE - SI NO EXISTE CONEXION
if not sta_if.isconnected():
    # Activamos el interfaz STA del ESP32
    sta_if.active(True)
    # Iniciamos la conexion con el AP
    sta_if.connect("SSID", "Password")
    print('Conectando a la red')
    # SI NO SE ESTABLECE
    while not sta_if.isconnected():
        # REPITE EL BUCLE
        pass
# MUESTRA EN PANTALLA
print('CONFIGURACION DE RED(IP/MASCARA/GATEWAY/DNS:', sta_if.ifconfig())

