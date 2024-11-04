import numpy as np
import matplotlib.pyplot as plt
from time import sleep

import paramiko
import paramiko.sftp_client

from datetime import datetime
from prettytable import PrettyTable

import sys
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import QTimer
from img import Ui_MainWindow

from tabla import PrintMenu

host = "192.168.100.57"
# host = "192.168.0.185"
username = "raspi"
password = "123456789"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)

sftp = client.open_sftp()
ruta_archivo_raspberry = "Desktop/log.txt"
ruta_destino_cliente = "./log.txt"
ruta_archivo_raspberryS = "Desktop/in.txt"
ruta_destino_clienteS = "./in.txt"


class Img(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    super(Img, self).__init__(*args, **kwargs)
    self.setupUi(self)
    self.label.setPixmap(QtGui.QPixmap("fig.png"))

    self.setWindowTitle('Mini proyecto 2')

    self.timer = QTimer()
    self.timer.timeout.connect(self.ftimer)

    self.timer.start(3000)

  def ftimer(self):
    graph()
    self.label.setPixmap(QtGui.QPixmap("fig.png"))

def condition(date):
  return (np.datetime64(datetime.now()) - date) <= 300_000_000

def intervalos(v, m, M):
  d = (M-m)*0.1
  if v >= (m + d) and v <= (M - d):
    return 1
  elif v >= m and v <= (m + d) or v >= (M - d) and v <= M:
    return 2
  else:
    return 3

al = [1,1,1]

def getData():
  sftp.get(ruta_archivo_raspberry, ruta_destino_cliente)
  with open('log.txt', 'r') as f:
      data = np.genfromtxt(f, dtype='datetime64[s],f,f,f', 
                          names=['date', 'temp', 'hum', 'dist'])
      data = [i for i in data if condition(i['date'])]
      data = np.array(data)
  al = [intervalos(sum(data['temp'])/len(data['temp']), 20, 24), intervalos(sum(data['hum'])/len(data['hum']), 33, 38), intervalos(sum(data['dist'])/len(data['dist']), 2,2)]
  with open('in.txt', 'w') as f:
      f.write(f'tem:{al[0]}\nhum:{al[1]}\ndis:{al[2]}')
  sftp.put(ruta_destino_clienteS, ruta_archivo_raspberryS)
  return data

def graph():
  plt.rcParams['date.converter'] = 'concise'
  data = getData()
  datetime = data['date']
  temperature = data['temp']
  hum = data['hum']
  dist = data['dist']

  fig, (ax0, ax1, ax2) = plt.subplots(3, 1, sharex=True, constrained_layout=True)

  # temperature:
  ax0.plot(datetime, temperature, label='secondly')
  ax0.legend(loc='upper right')
  ax0.set_ylabel('temperature $[^oC]$')  # note the use of TeX math formatting

  # humedad:
  ax1.plot(datetime, hum, label='secondly')
  ax1.legend(loc='upper right')
  ax1.set_ylabel('Humedad [%]')   # note the use of TeX math formatting

  # distancia
  ax2.plot(datetime, dist, label='secondly')
  ax2.legend(loc='upper right')
  ax2.set_ylabel('Distancia [m]')   # note the use of TeX math formatting

  ax0.set_title('Medición de sensores: temperatura, Humedad y Distancia', loc='left')

  plt.savefig('fig.png')


try:
  while True:
    PrintMenu(['1. Graph', '2. Table', '3. Exit'], -1, 'Info')
    inp = int(input('Select: '))
    if inp == 1:
      app = QtWidgets.QApplication(sys.argv)
      window = Img()
      window.show()
      app.exec()
    elif inp == 2:
      data = getData()
      x = PrettyTable()
      x.field_names = ['Timestamp','Temperatura [°C]', 'Humedad [%]', 'Distancia [m]']
      for row in data:
          x.add_row(row)
      # Change some column alignments; default was 'c'
      x.align['column_one'] = 'r'
      x.align['col_two'] = 'r'
      x.align['column_3'] = 'l'
      print(x)
    elif inp == 3:
      exit(1)

except Exception as err:
  raise err
  # client.close()