import sys
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import QTimer, QDateTime
from leds import Ui_MainWindow
from pinLed import Ui_Dialog
# from PyQt6 import QtCore, QtGui, QtWidgets
from random import randint as random

from gpiozero import RGBLED

LED1 = RGBLED(red=19, green=13, blue=26, pwm=True)
LED2 = RGBLED(red=5, green=0, blue=6,pwm=True)


class DialogoPin(QtWidgets.QDialog, Ui_Dialog):
  def __init__(self, pin=1, current=0, *args, **kwargs):
    super(DialogoPin, self).__init__(*args, **kwargs)
    self.setupUi(self)
    self.pin = pin
    self.label.setText(f'Led {self.pin} GPI pin: ')
    self.spinBox.setValue(current)
    self.setWindowTitle(f'Set Led Pin {self.pin}')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)
    self.setupUi(self)

    self.setWindowTitle('Mini proyecto 2')

    # setup

    self.currentColor1 = [124, 144, 255, 255]
    self.currentColor2 = [124, 144, 255, 255]
    self.b1 = False
    self.b2 = False
    self.timer_ = False
    self.gatos = ['gatos/1.png', 'gatos/2.png', 'gatos/3.png', 'gatos/4.png',]

    self.verticalSlider.valueChanged['int'].connect(lambda x: self.horizontalSlider.setValue(x))
    self.horizontalSlider.valueChanged['int'].connect(lambda x: self.verticalSlider.setValue(x))
    
    self.verticalSlider.valueChanged['int'].connect(lambda x: self.changeColor(1, [i for i in self.currentColor1[:-1]]+[(x*255)/100]))
    
    self.verticalSlider_6.valueChanged['int'].connect(lambda x: self.changeColor(1, [x]+self.currentColor1[1::]))
    self.verticalSlider_3.valueChanged['int'].connect(lambda x: self.changeColor(1, self.currentColor1[0:1]+[x]+self.currentColor1[2::]))
    self.verticalSlider_5.valueChanged['int'].connect(lambda x: self.changeColor(1, self.currentColor1[0:2]+[x]+self.currentColor1[3::]))

    self.pushButton_5.clicked.connect(lambda: self.changeColor(1, [255,0,0, self.currentColor1[3]]))
    self.pushButton_4.clicked.connect(lambda: self.changeColor(1, [0,255,0, self.currentColor1[3]]))
    self.pushButton_3.clicked.connect(lambda: self.changeColor(1, [0,0,255, self.currentColor1[3]]))
    self.pushButton_6.clicked.connect(lambda: self.changeColor(1, [125,33,129, self.currentColor1[3]]))
    self.pushButton_2.clicked.connect(lambda: self.changeColor(1, [0,255,255, self.currentColor1[3]]))
    self.pushButton_7.clicked.connect(lambda: self.changeColor(1, [255,0,255, self.currentColor1[3]]))

##

    self.verticalSlider_9.valueChanged['int'].connect(lambda x: self.horizontalSlider_3.setValue(x))
    self.horizontalSlider_3.valueChanged['int'].connect(lambda x: self.verticalSlider_9.setValue(x))
    
    self.verticalSlider_9.valueChanged['int'].connect(lambda x: self.changeColor(2, [i for i in self.currentColor2[:-1]]+[(x*255)/100]))
    
    self.verticalSlider_10.valueChanged['int'].connect(lambda x: self.changeColor(2, [x]+self.currentColor2[1::]))
    self.verticalSlider_11.valueChanged['int'].connect(lambda x: self.changeColor(2, self.currentColor2[0:1]+[x]+self.currentColor2[2::]))
    self.verticalSlider_12.valueChanged['int'].connect(lambda x: self.changeColor(2, self.currentColor2[0:2]+[x]+self.currentColor2[3::]))

    self.pushButton_17.clicked.connect(lambda: self.changeColor(2, [255,0,0, self.currentColor2[3]]))
    self.pushButton_18.clicked.connect(lambda: self.changeColor(2, [0,255,0, self.currentColor2[3]]))
    self.pushButton_19.clicked.connect(lambda: self.changeColor(2, [0,0,255, self.currentColor2[3]]))
    self.pushButton_20.clicked.connect(lambda: self.changeColor(2, [125,33,129, self.currentColor2[3]]))
    self.pushButton_21.clicked.connect(lambda: self.changeColor(2, [0,255,255, self.currentColor2[3]]))
    self.pushButton_22.clicked.connect(lambda: self.changeColor(2, [255,0,255, self.currentColor2[3]]))


    self.verticalSlider.setValue(100)
    self.verticalSlider_9.setValue(100)
    self.changeColor(1, self.currentColor1)
    self.changeColor(2, self.currentColor2)

    self.pushButton.setText('Led : Off')
    self.pushButton_16.setText('Led : Off')


    self.label_11.setPixmap(QtGui.QPixmap("gatos/1.png"))

    ## on/off
    self.pushButton.clicked.connect(lambda: self.onOff(1))
    self.pushButton_16.clicked.connect(lambda: self.onOff(2))
    ## timer

    self.label_17.setText('')
    self.timer = QTimer()
    self.timer.timeout.connect(self.showTime)
    self.pushButton_15.setText('Timer: Start')
    self.pushButton_15.clicked.connect(self.startTimer)

    self.t = 5

    self.LED_PIN = [12,14]

    #GPIO.setup(LED_PIN[0], GPIO.OUT)
    #GPIO.setup(LED_PIN[1], GPIO.OUT)

    self.actionLed_1.triggered.connect(lambda: self.pinSelect(1))
    self.actionLed_2.triggered.connect(lambda: self.pinSelect(2))

  def pinSelect(self, led):
    a,b = QtWidgets.QInputDialog.getInt(self, f'Set Led Pin {led}', f'Led {led} Pin GPI:', self.LED_PIN[led-1], 0,25,1)
    if b:
        #GPIO.cleanup()
        self.LED_PIN[led-1] = a
        #GPIO.setup(LED_PIN[0], GPIO.OUT)
        #GPIO.setup(LED_PIN[1], GPIO.OUT)
  def showTime(self):
    if self.t == 0:
      self.label_11.setPixmap(QtGui.QPixmap(self.gatos[random(0,3)]))
      self.t = 5
      self.label_17.setText(str(self.t))
      self.t -= 1

    else:
      self.label_17.setText(str(self.t))
      self.t -= 1

  def startTimer(self):
    if self.timer_ == True:
      self.timer.stop()
      self.pushButton_15.setText('Timer: Start')
      self.timer_ = False
      self.label_17.setText('')
    else:
      self.timer.start(1000)
      self.t = 5
      self.pushButton_15.setText('Timer: Stop')
      self.timer_ = True
      
  def onOff(self, n):
    if n == 1:
      if self.b1 == True:
        self.pushButton.setText('Led : Off')
        LED1.color = (self.currentColor1[0]/255,self.currentColor1[1]/255,self.currentColor1[2]/255)
        self.b1 = False
      else:
        self.pushButton.setText('Led : On')
        LED1.color = (0,0,0)
        self.b1 = True
    elif n == 2:
      if self.b2 == True:
        self.pushButton_16.setText('Led : Off')
        LED2.color = (self.currentColor2[0]/255,self.currentColor2[1]/255,self.currentColor2[2]/255)
        self.b2 = False
      else:
        self.pushButton_16.setText('Led : On')
        LED2.color = (0,0,0)
        self.b2 = True

  def changeColor(self, label, color):
    if label == 1:
      self.label.setStyleSheet(f'background: rgba({color[0]}, {color[1]}, {color[2]}, {color[3]}); height: 100px;')
    
      LED1.color = (color[0]/255,color[1]/255,color[2]/255)
    
      self.verticalSlider_6.setValue(color[0])
      self.verticalSlider_3.setValue(color[1])
      self.verticalSlider_5.setValue(color[2])

      self.currentColor1 = color
    elif label == 2:
      self.label_12.setStyleSheet(f'background: rgba({color[0]}, {color[1]}, {color[2]}, {color[3]}); height: 100px;')

      LED2.color = (color[0]/255,color[1]/255,color[2]/255)

      self.verticalSlider_10.setValue(color[0])
      self.verticalSlider_11.setValue(color[1])
      self.verticalSlider_12.setValue(color[2])

      self.currentColor2 = color

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec()
