import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from mainwindow import Ui_MainWindow  # 加载我们的布局
import mySerial


class UsingTest(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(UsingTest, self).__init__(*args, **kwargs)
        self.setupUi(self)  # 初始化ui
        self.initCombox()
        self.freshCombox()
        self.initButton()
        self.initIcon()
        self.initMain()
    def listenAcceptedData(self):
        pass
    def debugPrint(self):
        self.debugtextBrowser.setText(self.myPort.getInfo())
    def sendData2MyPort(self):
        self.sendtext=self.sendedRegion.toPlainText()
        self.debugtextBrowser.append("writed {} bytes!".format(self.myPort.writeData(self.sendtext)))
    def openMyPort(self):

        comx = self.comxCombo.currentText().lower()
        baud = eval(self.baudCombo.currentText())
        maxtime =eval( self.timeoutSpinBox.text())
        bytesize = eval(self.bytesizeCombo.currentText())
        parity = self.parityCombo.currentText()
        stopbit = eval(self.stopbitsCombo.currentText())

        self.myPort = mySerial.Port(comx, baud, maxtime,bytesize,parity,stopbit)
        self.debugPrint()
    def initIcon(self):
        self.exitIcon = QIcon('5g.png')
        self.winIcon = QIcon('label.png')

    def initCombox(self):
        self.comxCombo.addItems(mySerial.checkPorts())
        self.baudCombo.addItems([str(i) for i in [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
                                                  9600, 19200, 38400, 57600, 115200, 230400, 460800, 500000,
                                                  576000, 921600, 1000000, 1152000, 1500000, 2000000, 2500000,
                                                  3000000, 3500000, 4000000][::-1]])
        self.baudCombo.setCurrentText('115200')
        self.bytesizeCombo.addItems([str(i) for i in [5, 6, 7, 8][::-1]])
        self.parityCombo.addItems(['none','even','odd','mark','space'])
        self.stopbitsCombo.addItems(['1','1.5','2'])

    def initButton(self):
        # self.qbtn = QPushButton('Quit', self)
        # self.qbtn.clicked.connect(QCoreApplication.instance().quit)
        #
        self.checkBtn.setStatusTip('Check port')
        self.checkBtn.clicked.connect(self.freshCombox)
        self.closebtn.clicked.connect(sys.exit)
        self.openBtn.clicked.connect(self.openMyPort)
        self.sendBtn.clicked.connect(self.sendData2MyPort)


    def freshCombox(self):
        ports = mySerial.checkPorts()
        self.comxCombo.clear()
        for port in ports:
            self.comxCombo.addItem(port)

    def initMain(self):
        # self.setCentralWidget(QLabel("SERIAL PORT ASSISTANT"))
        # self.setGeometry(500, 600, 550, 550)
        self.setWindowIcon(self.winIcon)
        self.setWindowTitle('SERIAL PORT ASSISTANT by yjc')


if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    win = UsingTest()
    win.show()
    sys.exit(app.exec_())
