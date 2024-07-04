from machine import Pin
import time

"""
Super TOOLS LP
El siguiente código simula el funcionamiento
de un semáforo.

Si tienes problemas o dudas comunícate en 
https://supertoolslp.blogspot.com/p/contacto.html
"""

# definición de pines para los segmentos del display
segments = {
    'a': Pin(2, Pin.OUT),
    'b': Pin(3, Pin.OUT),
    'c': Pin(4, Pin.OUT),
    'd': Pin(5, Pin.OUT),
    'e': Pin(6, Pin.OUT),
    'f': Pin(7, Pin.OUT),
    'g': Pin(8, Pin.OUT)
}

# mapeo de números a segmentos
numbers = {
    0: ['a', 'b', 'c', 'd', 'e', 'f'],
    1: ['b', 'c'],
    2: ['a', 'b', 'g', 'e', 'd'],
    3: ['a', 'b', 'g', 'c', 'd'],
    4: ['f', 'g', 'b', 'c'],
    5: ['a', 'f', 'g', 'c', 'd'],
    6: ['a', 'f', 'g', 'c', 'd', 'e'],
    7: ['a', 'b', 'c'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

def apagar_display():
    for segment in segments.values():
        segment.value(0)

def mostrar_numero(numero):
    apagar_display()
    for segment in numbers[numero]:
        segments[segment].value(1)

def contar_segundos(segundos):
    for i in range(1, segundos + 1):
        mostrar_numero(i % 10)
        time.sleep(1)
        apagar_display()

# definición de pines para los LEDs del semáforo
led_verde = Pin(20, Pin.OUT)
led_amarillo = Pin(19, Pin.OUT)
led_rojo = Pin(18, Pin.OUT)

while True:
    led_amarillo.value(0)
    led_verde.value(1)
    contar_segundos(9) # cuenta hasta 9 segundos
    led_verde.value(0)
    led_amarillo.value(1)
    contar_segundos(2) # cuenta hasta 2 segundos
    led_amarillo.value(0)
    led_rojo.value(1)
    contar_segundos(9) 
    led_rojo.value(0)
    led_amarillo.value(1)
    contar_segundos(2)
