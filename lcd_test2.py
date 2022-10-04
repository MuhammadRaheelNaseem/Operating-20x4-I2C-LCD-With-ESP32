from machine import Pin, I2C, ADC
from time import sleep, sleep_ms
from machine_i2c_lcd import I2cLcd
import dht 

sensor = dht.DHT22(Pin(12))
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

addr = i2c.scan()[0]
lcd = I2cLcd(i2c, addr, 2, 16)

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    lcd.putstr("Welcome To Weather Station..\n")
    sleep(1)
    lcd.clear()
    lcd.putstr(f"Temp: {temp} °C")
    sleep(1)
    lcd.clear()
    lcd.putstr(f"Humidity: {hum} %")
    lcd.clear()
    sleep(0.5)
