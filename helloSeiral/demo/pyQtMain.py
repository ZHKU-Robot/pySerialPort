import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QLabel, QPushButton, QMessageBox, \
    QDesktopWidget, QHBoxLayout, QVBoxLayout, QWidget, QMenuBar, QGroupBox, QGridLayout, QComboBox
from PyQt5.QtGui import QIcon

import mySerial
import serial  # 导入模块
import serial.tools.list_ports

class SerialPortWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initSerialPort()
        self.initIcon()
        self.initAction()
        self.initButton()
        self.initLabel()
        self.initCombox()
        self.initTextInput()
        self.initMainBoxLayout()
        #
        self.moveCenter()
        self.initMain()
        self.show()
    def initTextInput(self):
        self.acceptedTextInput=QTextEdit()
        self.acceptedTextInput.setMinimumHeight(20)
        self.acceptedTextInput.setText(str(self.accNum))

        self.sendedTextInput=QTextEdit()
        self.sendedTextInput.setMinimumHeight(20)
        self.sendedTextInput.setText(str(self.senNum))
    def initLabel(self):
        self.comx=QLabel("COMX:")
        self.baud = QLabel("baud:")
        self.bytesize=QLabel("bytesize:")
        self.parity=QLabel("parity:")
        self.stopbits=QLabel("stopbits:")
        self.accepted = QLabel("accepted:")
        self.accNum=0
        self.sended = QLabel("sended:  ")
        self.senNum=0
    def initSerialPort(self):
        self.ports=mySerial.checkPorts()
        # self.port=mySerial.Port()

    def initCombox(self):
        self.comboPort = QComboBox(self)
        self.comboBaud= QComboBox(self)
        self.comboByteSizes= QComboBox(self)
        self.comboByteSizes.addItems([str(i) for i in [5,6,7,8][::-1]])
        self.comboParity= QComboBox(self)
        self.comboParity.addItem('N')
        self.comboStopbits= QComboBox(self)
        self.comboStopbits.addItem('1')



    def initconfigBoxLayout(self):
        self.configBoxLayout = QVBoxLayout()
        self.configGridLayout=QGridLayout()
        self.configBoxLayout.setStretchFactor(self.configGridLayout,11)
        self.configBoxLayout.setSpacing(10)
        self.configGridLayout.setHorizontalSpacing(10)
        self.configGridLayout.setVerticalSpacing(20)
        self.configBoxLayout.addLayout(self.configGridLayout)
        self.configGridLayout.setSpacing(20)

        self.configGridLayout.addWidget(self.comboPort,0,1)
        self.configGridLayout.addWidget(self.checkPortBtn,0,0)
        self.configGridLayout.addWidget(self.baud,1,0)
        self.configGridLayout.addWidget(self.comboBaud, 1, 1)
        self.configGridLayout.addWidget(self.bytesize,2,0)
        self.configGridLayout.addWidget(self.comboByteSizes, 2, 1)
        self.configGridLayout.addWidget(self.parity,3,0)
        self.configGridLayout.addWidget(self.comboParity,3,1)
        self.configGridLayout.addWidget(self.stopbits,4,0)
        self.configGridLayout.addWidget(self.comboStopbits, 4, 1)
        self.configGridLayout.addWidget(self.openPortBtn,5,0)
        self.configGridLayout.addWidget(self.closePortBtn,5,1)
        #

        self.displayBoxLayout=QVBoxLayout()
        self.configBoxLayout.setStretchFactor(self.displayBoxLayout,2)
        self.configBoxLayout.addLayout(self.displayBoxLayout)

        self.acceptedGridLayout=QGridLayout()

        self.acceptedGridLayout.addWidget(self.accepted,0,0)

        self.acceptedGridLayout.addWidget(self.acceptedTextInput,0,1)
        self.sendedGridLayout = QGridLayout()
        self.sendedGridLayout.addWidget(self.sended,1,0)
        self.sendedGridLayout.addWidget(self.sendedTextInput,1,1)

        self.displayBoxLayout.addLayout(self.acceptedGridLayout)
        self.displayBoxLayout.addLayout(self.sendedGridLayout)



    def initfigureBoxLayout(self):
        self.figureBoxLayout = QVBoxLayout()
        self.figureBoxLayout.addWidget(QLabel("figure"))
        self.figureBoxLayout.addWidget(QLabel("figure"))
        self.figureBoxLayout.addWidget(QLabel("figure"))


    def initMenuBar(self):
        self.menubar = QMenuBar()
        self.fileMenu = self.menubar.addMenu('&File')
        self.fileMenu.addAction(self.exitAct)

    # 只有 Qwidget才有setlayout嗷
    def initMainBoxLayout(self):
        self.mainBoxLayout = QHBoxLayout()
        # self.mainBoxLayout.setMenuBar(self.menubar)
        self.initfigureBoxLayout()
        self.initconfigBoxLayout()
        # #这个导航栏sb
        # self.mainBoxLayout.set
        self.mainBoxLayout.addLayout(self.configBoxLayout)
        self.mainBoxLayout.addLayout(self.figureBoxLayout)

        self.setLayout(self.mainBoxLayout)

    def initButton(self):
        # self.qbtn = QPushButton('Quit', self)
        # self.qbtn.clicked.connect(QCoreApplication.instance().quit)
        #
        self.checkPortBtn = QPushButton("check-COMX",self)
        self.checkPortBtn.setStatusTip('Check port')
        self.checkPortBtn.clicked.connect(self.freshCombox)

        self.openPortBtn=QPushButton("open",self)
        self.closePortBtn = QPushButton("close", self)

    # def closeEvent(self, event) -> None:
    #     reply = QMessageBox.question(self, '求你了,再学一会吧',"你想被兴爷吊打吗?再学会吧..", QMessageBox.Yes |QMessageBox.No, QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()
    def moveCenter(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initIcon(self):
        self.exitIcon = QIcon('5g.png')
        self.winIcon = QIcon('label.png')

    def initAction(self):
        self.exitAct = QAction(self.exitIcon, 'Exit', self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip('Exit application')
        self.exitAct.triggered.connect(self.close)


    def initMain(self):
        # self.setCentralWidget(QLabel("SERIAL PORT ASSISTANT"))
        self.setGeometry(500, 600, 550, 550)
        self.setWindowIcon(self.winIcon)
        self.setWindowTitle('SERIAL PORT ASSISTANT by yjc')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SerialPortWindow()
    sys.exit(app.exec_())
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     def initUI(self):
#         textEdit = QTextEdit()
#         self.setCentralWidget(textEdit)
#         exitAct = QAction(QIcon('5g.png'), 'Exit', self)
#         exitAct.setShortcut('Ctrl+Q')
#         exitAct.setStatusTip('Exit application')
#         exitAct.triggered.connect(self.close)
#         self.statusBar()
#
#         toolbar = self.addToolBar('Exit')
#         toolbar.addAction(exitAct)
#         self.setGeometry(300, 300, 350, 250)
#         self.setWindowTitle('Main window')
#         self.show()


