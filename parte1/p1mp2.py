import logging
import datetime
from time import sleep
import board
import adafruit_dht as ada
from gpiozero import DistanceSensor, RGBLED
import subprocess
from gpiozero import Buzzer

from random import randrange
buzzer = Buzzer(17)
LEDs = [
    RGBLED(red=19, green=13, blue=26, pwm=True),
    RGBLED(red=5, green=0, blue=6,pwm=True)
    #RGBLED(red=16, green=20, blue=21,pwm=True)
    ]
EstadoLeds = [1,1,1]
FILE_LOG = '/home/raspi/Desktop/log.txt'
script_path = '/home/raspi/Desktop/correct_sensor.sh'
result = subprocess.run([script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


dhtDevice = ada.DHT11(board.D23)
DS = DistanceSensor(25, 24, max_distance=3, threshold_distance=0.2)

logging.basicConfig(
    filename=FILE_LOG,
    level=logging.INFO,
    datefmt="%Y-%m-%dT%H:%M:%S",
    format = "%(asctime)s   %(message)s"
)

w = True
try:
    while w:
       	try:
            with open('in.txt', 'r') as f:
                f = f.read()
                data = f.split('\n')
                data = [i.split(':')[1] for i in data]
            print(data)
            for i in range(len(data)-1):
                if data[i] == '1':
                    if EstadoLeds[i] != 1:          
                        buzzer.beep()
                        print('Estado actualizado')
                    EstadoLeds[i] = 1
                    LEDs[i].color = (0,1,0)
                elif data[i] == '2':
                    if EstadoLeds[i] != 2:          
                        buzzer.beep()
                        print('Estado actualizado')
                    EstadoLeds[i] = 2
                    LEDs[i].color = (1,1,0)
                elif data[i] =='3':
                    if EstadoLeds[i] != 3:          
                        buzzer.beep()
                        print('Estado actualizado')
                    EstadoLeds[i] = 3
                    LEDs[i].color = (1,0,0)
            logging.info('{:.3f}  {:.3f}  {:.3f}'.format(randrange(18,25,1), randrange(30,40,1), randrange(0,3,1)))
	    #tem_c = dhtDevice.temperature
            #tem_f = tem_c * (9/5) + 32
            #humidity = dhtDevice.humidity
            #dis = DS.distance
            #logging.info('{:.3f}    {:.3f}  {:.3f}'.format(tem_c, humidity,dis)) 
            #print('Temp: {:.1f} F / {:.3f} C	Humidity:{}%	Distance: {:.3f}'.format(tem_f,tem_c, humidity, dis))
        except RuntimeError as error:
            print(error.args[0])
            sleep(2.0)
            continue
        except Exception as err:
            raise err
        sleep(2)
except Exception as err:
    print(str(err))
    exit(1)

if dhtDevice:
    dhtDevice.exit()
