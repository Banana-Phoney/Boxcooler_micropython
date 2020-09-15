#controll o

import machine
import time
import dht

red = machine.Pin(13, machine.Pin.OUT)
gul = machine.Pin(4, machine.Pin.OUT)
blue = machine.Pin(5, machine.Pin.OUT)
hvit = machine.Pin(15, machine.Pin.OUT)

pwmduty = 0
sensor = dht.DHT11(machine.Pin(12))

p14 = machine.Pin(14)
pwm14 = machine.PWM(p14)
pwm14.freq(500)
pwm14.duty(pwmduty)

def lightsoff():
  red.off()
  gul.off()
  blue.off()
  hvit.off()

lightsoff()

while True:
  try:
    time.sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature:', temp)
  except OSError as e:
    print('Failed to read sensor.')
    temp = 99
  if(temp <=29):
    print("Just chilling")
    pwmduty = 0
    lightsoff()
    hvit.on()
  elif(temp >= 30 and temp <=39):
    print("Warm")
    pwmduty = 600
    lightsoff()
    blue.on()
  elif(temp >= 40 and temp <=49):
    print("Things are heating up!")
    pwmduty = 800
    lightsoff()
    gul.on()
  elif(temp >= 50 and temp <=98):
    print("HIGH TEMPERATURE")
    pwmduty = 1023
    lightsoff()
    red.on()
  elif(temp >= 99):
    print("FULL SPEED AHEAD!")
    pwmduty = 1023
    lightsoff()
    red.on()
    gul.on()
  else:
    pwmduty = 0
  pwm14.duty(pwmduty)