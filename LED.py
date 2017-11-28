# Importamos la libreria GPIO
import RPi.GPIO as GPIO

# Importamos la libreria para el teclado
import curses

# Importamos la libreria del LED
from gpiozero import RGBLED

# Declaramos la entrada de teclado
key = curses.initscr()

# Declaramos el led
led = RGBLED(12,16,20)

# Definimos el modo BCH
GPIO.setmode(GPIO.BCM)

# Ahora definimos el pin GPIO 18 como salida
GPIO.setup(18,GPIO.OUT)

# Realizamos el ciclo
while True:
    
    tecla = key.getch() # obtenemos la tecla presionada
    if tecla == 27: # Teclas direccionales, que va a encender el LED Rojo
        led.on()
        led.off()
        led.color = (1 , 0 , 0) # Rojo
        
    if tecla == 32: # Tecla de espacio, que va a encender el LED Verde
        led.on()
        led.off()
        led.color = (0, 1 , 0) # Verde
       
    if tecla == 119 :  #  Tecla W , que va a encender el LED Azul
        led.on()
        led.off()
        led.color = (0, 0 , 1) # Azul
        
    if tecla == 103: # Tecla G, para apagar LEDS
        GPIO.cleanup() # Limpiamos los Pines
        
