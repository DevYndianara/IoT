from machine import Pin
from utime import sleep
import _thread
#-------       Configuracao (Pinos na Pi Pico) ----------- #
ledR=Pin(0, Pin.OUT)
ledY=Pin(1, Pin.OUT)
ledG=Pin(2, Pin.OUT)
button=Pin(3, Pin.IN, Pin.PULL_DOWN)
buzzer=Pin(4, Pin.OUT)
sensor=Pin(18, Pin.IN, Pin.PULL_DOWN)
#---------    Variaveis (Como irá se agir cada componente físico da protoboard)  --------- #
global buttonPressed
global sensorDetected
buttonPressed=False
sensorDetected=False
#---------   thread Alarme    ---------#
def Alarme():
    global buttonPressed
    global sensorDetected
    while True:
        if sensor.value() == 1:
            sensorDetected=True
        if button.value()==1:
            buttonPressed=True
    sleep(0.1)
_thread.start_new_thread(Alarme,())
#------------ Main  ------------------#
while True:
    buttonPressed = False
    ledG.value(1)
    ledR.value(0)
    ledY.value(0)
    buzzer.value(0)
    while sensorDetected==True:
        ledG.value(0)
        ledR.toggle()
        ledY.toggle()
        sleep(0.05)
        buzzer.toggle()
        if buttonPressed==True:
            sensorDetected=False
