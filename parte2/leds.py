# Form implementation generated from reading ui file 'leds.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 562)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabWidget_3 = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_13.setSpacing(11)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label = QtWidgets.QLabel(parent=self.tab_5)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(0, 75))
        self.label.setStyleSheet("background: rgb(124, 144, 255);\n"
"height: 100px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_13.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(parent=self.tab_5)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_13.addWidget(self.pushButton)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.tab_5)
        self.tabWidget.setStyleSheet("background:white;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_4.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_6.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_7.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalSlider = QtWidgets.QSlider(parent=self.tab)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_7.addWidget(self.verticalSlider)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(parent=self.tab)
        self.lcdNumber_5.setMaximumSize(QtCore.QSize(100, 50))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.verticalLayout_11.addWidget(self.lcdNumber_5)
        self.label_5 = QtWidgets.QLabel(parent=self.tab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.tab_2)
        self.lcdNumber.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_4.addWidget(self.lcdNumber)
        self.verticalSlider_6 = QtWidgets.QSlider(parent=self.tab_2)
        self.verticalSlider_6.setMaximum(255)
        self.verticalSlider_6.setProperty("value", 100)
        self.verticalSlider_6.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.verticalLayout_4.addWidget(self.verticalSlider_6, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_4.setStyleSheet("padding:6px;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(parent=self.tab_2)
        self.lcdNumber_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.verticalLayout_2.addWidget(self.lcdNumber_3)
        self.verticalSlider_3 = QtWidgets.QSlider(parent=self.tab_2)
        self.verticalSlider_3.setMaximum(255)
        self.verticalSlider_3.setProperty("value", 100)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalLayout_2.addWidget(self.verticalSlider_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_2.setStyleSheet("padding:6px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(parent=self.tab_2)
        self.lcdNumber_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_3.addWidget(self.lcdNumber_2)
        self.verticalSlider_5 = QtWidgets.QSlider(parent=self.tab_2)
        self.verticalSlider_5.setMaximum(255)
        self.verticalSlider_5.setProperty("value", 100)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.verticalLayout_3.addWidget(self.verticalSlider_5, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_3.setStyleSheet("padding:6px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_12.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.tab_2)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(parent=self.tab_2)
        self.lcdNumber_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.horizontalLayout_2.addWidget(self.lcdNumber_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_13.addWidget(self.tabWidget)
        self.horizontalLayout_11.addLayout(self.verticalLayout_13)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_17.setSpacing(11)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_12 = QtWidgets.QLabel(parent=self.tab_5)
        self.label_12.setEnabled(True)
        self.label_12.setMinimumSize(QtCore.QSize(0, 75))
        self.label_12.setStyleSheet("background: rgb(124, 144, 255);\n"
"height: 100px;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_17.addWidget(self.label_12)
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.tab_5)
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_17.addWidget(self.pushButton_16)
        self.tabWidget_4 = QtWidgets.QTabWidget(parent=self.tab_5)
        self.tabWidget_4.setStyleSheet("background:white;")
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.tab_7)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.pushButton_17 = QtWidgets.QPushButton(parent=self.tab_7)
        self.pushButton_17.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_18.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(parent=self.tab_7)
        self.pushButton_18.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_18.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.tab_7)
        self.pushButton_19.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_18.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(parent=self.tab_7)
        self.pushButton_20.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.verticalLayout_18.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(parent=self.tab_7)
        self.pushButton_21.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.verticalLayout_18.addWidget(self.pushButton_21)
        self.pushButton_22 = QtWidgets.QPushButton(parent=self.tab_7)
        self.pushButton_22.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_22.setObjectName("pushButton_22")
        self.verticalLayout_18.addWidget(self.pushButton_22)
        self.horizontalLayout_13.addLayout(self.verticalLayout_18)
        self.verticalSlider_9 = QtWidgets.QSlider(parent=self.tab_7)
        self.verticalSlider_9.setMaximum(100)
        self.verticalSlider_9.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_9.setObjectName("verticalSlider_9")
        self.horizontalLayout_13.addWidget(self.verticalSlider_9)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.lcdNumber_11 = QtWidgets.QLCDNumber(parent=self.tab_7)
        self.lcdNumber_11.setMaximumSize(QtCore.QSize(100, 50))
        self.lcdNumber_11.setObjectName("lcdNumber_11")
        self.verticalLayout_19.addWidget(self.lcdNumber_11)
        self.label_13 = QtWidgets.QLabel(parent=self.tab_7)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_19.addWidget(self.label_13, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout_13.addLayout(self.verticalLayout_19)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.tabWidget_4.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.tab_8)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.lcdNumber_12 = QtWidgets.QLCDNumber(parent=self.tab_8)
        self.lcdNumber_12.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcdNumber_12.setObjectName("lcdNumber_12")
        self.verticalLayout_21.addWidget(self.lcdNumber_12)
        self.verticalSlider_10 = QtWidgets.QSlider(parent=self.tab_8)
        self.verticalSlider_10.setMaximum(255)
        self.verticalSlider_10.setProperty("value", 100)
        self.verticalSlider_10.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_10.setObjectName("verticalSlider_10")
        self.verticalLayout_21.addWidget(self.verticalSlider_10, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_14 = QtWidgets.QLabel(parent=self.tab_8)
        self.label_14.setStyleSheet("padding:6px;")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_21.addWidget(self.label_14, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_14.addLayout(self.verticalLayout_21)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.lcdNumber_13 = QtWidgets.QLCDNumber(parent=self.tab_8)
        self.lcdNumber_13.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcdNumber_13.setObjectName("lcdNumber_13")
        self.verticalLayout_22.addWidget(self.lcdNumber_13)
        self.verticalSlider_11 = QtWidgets.QSlider(parent=self.tab_8)
        self.verticalSlider_11.setMaximum(255)
        self.verticalSlider_11.setProperty("value", 100)
        self.verticalSlider_11.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_11.setObjectName("verticalSlider_11")
        self.verticalLayout_22.addWidget(self.verticalSlider_11, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_15 = QtWidgets.QLabel(parent=self.tab_8)
        self.label_15.setStyleSheet("padding:6px;")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_22.addWidget(self.label_15, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_14.addLayout(self.verticalLayout_22)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.lcdNumber_14 = QtWidgets.QLCDNumber(parent=self.tab_8)
        self.lcdNumber_14.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcdNumber_14.setObjectName("lcdNumber_14")
        self.verticalLayout_23.addWidget(self.lcdNumber_14)
        self.verticalSlider_12 = QtWidgets.QSlider(parent=self.tab_8)
        self.verticalSlider_12.setMaximum(255)
        self.verticalSlider_12.setProperty("value", 100)
        self.verticalSlider_12.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider_12.setObjectName("verticalSlider_12")
        self.verticalLayout_23.addWidget(self.verticalSlider_12, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_16 = QtWidgets.QLabel(parent=self.tab_8)
        self.label_16.setStyleSheet("padding:6px;")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_23.addWidget(self.label_16, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_14.addLayout(self.verticalLayout_23)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem6)
        self.verticalLayout_20.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalSlider_3 = QtWidgets.QSlider(parent=self.tab_8)
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalLayout_15.addWidget(self.horizontalSlider_3)
        self.lcdNumber_15 = QtWidgets.QLCDNumber(parent=self.tab_8)
        self.lcdNumber_15.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcdNumber_15.setObjectName("lcdNumber_15")
        self.horizontalLayout_15.addWidget(self.lcdNumber_15)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem7)
        self.verticalLayout_20.addLayout(self.horizontalLayout_15)
        self.tabWidget_4.addTab(self.tab_8, "")
        self.verticalLayout_17.addWidget(self.tabWidget_4)
        self.horizontalLayout_11.addLayout(self.verticalLayout_17)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_11)
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setMinimumSize(QtCore.QSize(629, 475))
        self.tab_6.setMaximumSize(QtCore.QSize(16777215, 475))
        self.tab_6.setObjectName("tab_6")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(parent=self.tab_6)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 611, 461))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_11 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_11.setStyleSheet("background-color: rgb(129, 125, 255);")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("gatos/4.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_24.addWidget(self.label_11)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_6)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_17.addWidget(self.pushButton_15)
        self.label_17 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_17.addWidget(self.label_17)
        self.verticalLayout_24.addLayout(self.horizontalLayout_17)
        self.tabWidget_3.addTab(self.tab_6, "")
        self.verticalLayout_9.addWidget(self.tabWidget_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 21))
        self.menubar.setObjectName("menubar")
        self.menuRaspi = QtWidgets.QMenu(parent=self.menubar)
        self.menuRaspi.setObjectName("menuRaspi")
        self.menuPin_leds = QtWidgets.QMenu(parent=self.menuRaspi)
        self.menuPin_leds.setObjectName("menuPin_leds")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionActivar = QtGui.QAction(parent=MainWindow)
        self.actionActivar.setObjectName("actionActivar")
        self.actionLed_1 = QtGui.QAction(parent=MainWindow)
        self.actionLed_1.setObjectName("actionLed_1")
        self.actionLed_2 = QtGui.QAction(parent=MainWindow)
        self.actionLed_2.setObjectName("actionLed_2")
        self.menuPin_leds.addAction(self.actionLed_1)
        self.menuPin_leds.addAction(self.actionLed_2)
        self.menuRaspi.addAction(self.menuPin_leds.menuAction())
        self.menubar.addAction(self.menuRaspi.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.verticalSlider_6.valueChanged['int'].connect(self.lcdNumber.display) # type: ignore
        self.verticalSlider_3.valueChanged['int'].connect(self.lcdNumber_3.display) # type: ignore
        self.verticalSlider_5.valueChanged['int'].connect(self.lcdNumber_2.display) # type: ignore
        self.horizontalSlider.valueChanged['int'].connect(self.lcdNumber_4.display) # type: ignore
        self.verticalSlider.valueChanged['int'].connect(self.lcdNumber_5.display) # type: ignore
        self.verticalSlider_9.valueChanged['int'].connect(self.lcdNumber_11.display) # type: ignore
        self.verticalSlider_10.valueChanged['int'].connect(self.lcdNumber_12.display) # type: ignore
        self.verticalSlider_11.valueChanged['int'].connect(self.lcdNumber_13.display) # type: ignore
        self.verticalSlider_12.valueChanged['int'].connect(self.lcdNumber_14.display) # type: ignore
        self.horizontalSlider_3.valueChanged['int'].connect(self.lcdNumber_15.display) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Led : On"))
        self.pushButton_5.setText(_translate("MainWindow", "Red"))
        self.pushButton_4.setText(_translate("MainWindow", "Green"))
        self.pushButton_3.setText(_translate("MainWindow", "Blue"))
        self.pushButton_6.setText(_translate("MainWindow", "purple"))
        self.pushButton_2.setText(_translate("MainWindow", "Cyan"))
        self.pushButton_7.setText(_translate("MainWindow", "Magenta"))
        self.label_5.setText(_translate("MainWindow", "Intensity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basic"))
        self.label_4.setText(_translate("MainWindow", "Red"))
        self.label_2.setText(_translate("MainWindow", "Green"))
        self.label_3.setText(_translate("MainWindow", "Blue"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Advance"))
        self.pushButton_16.setText(_translate("MainWindow", "Led : On"))
        self.pushButton_17.setText(_translate("MainWindow", "Red"))
        self.pushButton_18.setText(_translate("MainWindow", "Green"))
        self.pushButton_19.setText(_translate("MainWindow", "Blue"))
        self.pushButton_20.setText(_translate("MainWindow", "purple"))
        self.pushButton_21.setText(_translate("MainWindow", "Cyan"))
        self.pushButton_22.setText(_translate("MainWindow", "Magenta"))
        self.label_13.setText(_translate("MainWindow", "Intensity"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_7), _translate("MainWindow", "Basic"))
        self.label_14.setText(_translate("MainWindow", "Red"))
        self.label_15.setText(_translate("MainWindow", "Green"))
        self.label_16.setText(_translate("MainWindow", "Blue"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_8), _translate("MainWindow", "Advance"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "Leds"))
        self.pushButton_15.setText(_translate("MainWindow", "Timer"))
        self.label_17.setText(_translate("MainWindow", "00:00"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "Gatos locos"))
        self.menuRaspi.setTitle(_translate("MainWindow", "Raspi"))
        self.menuPin_leds.setTitle(_translate("MainWindow", "Pin leds"))
        self.actionActivar.setText(_translate("MainWindow", "Activar"))
        self.actionLed_1.setText(_translate("MainWindow", "Led 1"))
        self.actionLed_2.setText(_translate("MainWindow", "Led 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
