#Touch PAD
from machine import TouchPad,Pin
from time import sleep

Led_Obj   = Pin(2,Pin.OUT)
Touch_obj = TouchPad(Pin(4))

while True:
    Touch_Val = Touch_obj.read()
    print("Touch Value:",Touch_Val)
    if Touch_Val < 350:
        Led_Obj.on()
    else:
        Led_Obj.off()