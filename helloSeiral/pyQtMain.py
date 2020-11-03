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
        self.initMenuBar()
        self.initCombox()
        self.initMainBoxLayout()

        # self.initButton()

        #
        self.moveCenter()
        self.initMain()
        self.show()

    def initSerialPort(self):
        self.curSerPort = serial.tools.list_ports.comports()

    def initCombox(self):
        self.combo = QComboBox(self)
        for port in self.curSerPort:
            self.combo.addItem(port)
    def initconfigBoxLayout(self):

        self.configBoxLayout = QVBoxLayout()

        self.configGridLayout=QGridLayout()
        self.configBoxLayout.addLayout(self.configGridLayout)

        self.comx=QLabel("COMX:")
        self.configGridLayout.addWidget(self.comx,0,0)
        self.configGridLayout.addWidget(self.combo,0,1)

    def initfigureBoxLayout(self):
        self.figureBoxLayout = QVBoxLayout()


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
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
