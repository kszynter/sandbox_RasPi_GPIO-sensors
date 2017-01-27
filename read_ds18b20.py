import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folders = glob.glob(base_dir + '28*')

device_files = []
for f in device_folders:
  device_files.append(f + '/w1_slave')

def read_temp_raw(device_file):
  f = open(device_file, 'r')
  lines = f.read().splitlines()

  f.close()
  return lines

def temp_read_successfuly(lines):
  if lines != None:
    for l in lines:
      if l.strip()[-3:] == 'YES':
        return True

  return False

def parse_temp_values(lines):
  temps = []

  for l in lines:
    index = l.find('t=')
    if index != -1:
      temps.append(l[index+2:])

  return temps

def convert_to_celsius(temp):
  return float(temp) / 1000.0

def convert_to_fahrenheit(temp):
  return convert_to_celsius(float(temp) * 9.0 / 5.0 + 32.0)

def print_celsius(temps):
  for t in temps:
    print(str(convert_to_celsius(t)) + 'C')

def print_fahrenheit(temps):
  for t in temps:
    print(str(convert_to_fahrenheit(t)) + 'F')

def main():
  lines = []

  for df in device_files:
    lines.extend(read_temp_raw(df))

  while not temp_read_successfuly(lines):
    print('no temperatures')
    time.sleep(1)
    for df in device_files:
      lines = read_temp_raw(df)

  temps = parse_temp_values(lines)
  if temps != None:
    print_celsius(temps)
    # print_fahrenheit(temps)

while True:
  main()
  time.sleep(5)
