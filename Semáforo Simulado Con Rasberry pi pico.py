from machine import *
import time

""" Super TOOLS LP
El siguiente código simula el funcionamiento
de un semáforo, el código se puede optimizar
mas pero está implementado de tal forma, para
que los principiantes puedan entender. Sin embargo
también les dejo otro que está implementado de forma
avanzada para que lo analicen.

Si no tienes aun la rasberry pi pico, usa la simulación en WOKWI
https://wokwi.com/projects/402503035708492801

Si tienes problemas o dudas comunícate en 
https://supertoolslp.blogspot.com/p/contacto.html
"""

# apaga los leds del display
def apagar():
  a.value(0)
  b.value(0)
  c.value(0)
  d.value(0)
  e.value(0)
  f.value(0)
  g.value(0)

led_verde = Pin(20, Pin.OUT) # 14
led_amarillo = Pin(19, Pin.OUT) # 15
led_rojo = Pin(18, Pin.OUT) # 16

# se definen los pines del display como salida
a = Pin(2, Pin.OUT) # 4
b = Pin(3, Pin.OUT) # 5
c = Pin(4, Pin.OUT) # 6
d = Pin(5, Pin.OUT) # 7
e = Pin(6, Pin.OUT) # 9
f = Pin(7, Pin.OUT) # 10
g = Pin(8, Pin.OUT) # 11

# contar 9 segundos
def nueve_seg():
  b.value(1) # 1 seg
  c.value(1)
  time.sleep(1)
  apagar()
  a.value(1) # 2 seg
  b.value(1)
  g.value(1)
  e.value(1)
  d.value(1)
  time.sleep(1)
  apagar()
  a.value(1) # 3 seg
  b.value(1)
  g.value(1)
  c.value(1)
  d.value(1)
  time.sleep(1)
  apagar()
  f.value(1) # 4 seg
  b.value(1)
  g.value(1)
  c.value(1)
  time.sleep(1)
  apagar()
  a.value(1) # 5 seg
  f.value(1)
  g.value(1)
  c.value(1)
  d.value(1)
  time.sleep(1)
  apagar()
  a.value(1) # 6 seg
  f.value(1)
  g.value(1)
  e.value(1)
  c.value(1)
  d.value(1)
  time.sleep(1)
  apagar()
  a.value(1) # 7 seg
  b.value(1)
  c.value(1)
  time.sleep(1)
  apagar()
  a.value(1) # 8 seg
  b.value(1)
  c.value(1)
  d.value(1)
  e.value(1)
  f.value(1)
  g.value(1)
  time.sleep(1)
  apagar()
  a.value(1) # 9 seg
  b.value(1)
  f.value(1)
  g.value(1)
  c.value(1)
  d.value(1)
  time.sleep(1)
  apagar()

# contar 2 segundos
def dos_seg():
  b.value(1) # 1 seg
  c.value(1)
  time.sleep(1)
  apagar()
  a.value(1) # 2 seg
  b.value(1)
  g.value(1)
  e.value(1)
  d.value(1)
  time.sleep(1)
  apagar()

while True:

  # bucle principal
  led_amarillo.value(0)
  led_verde.value(1)
  nueve_seg()
  led_verde.value(0)
  led_amarillo.value(1)
  dos_seg()
  led_amarillo.value(0)
  led_rojo.value(1)
  nueve_seg()
  led_rojo.value(0)
  led_amarillo.value(1)
  dos_seg()