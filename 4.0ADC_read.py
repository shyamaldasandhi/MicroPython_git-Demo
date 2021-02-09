#ADC OF ESP32
from machine import Pin, ADC
from time import sleep

ADC_obj = ADC(Pin(32))

while True:
    ADC_val = ADC_obj.read()
    print("ADC Value:",ADC_val)
    sleep(1)