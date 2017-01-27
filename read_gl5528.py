import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin_sensor = 14

def rc_time(pin_sensor):
  count = 0

  GPIO.setup(pin_sensor, GPIO.OUT)
  GPIO.output(pin_sensor, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(pin_sensor, GPIO.IN)

  while(GPIO.input(pin_sensor) == GPIO.LOW):
    count += 1

  return count

try:
  while True:
    print rc_time(pin_sensor)
except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()
