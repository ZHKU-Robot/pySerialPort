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
    def initIcon(self):
        self.exitIcon = QIcon('5g.png')
        self.winIcon = QIcon('label.png')
    def initCombox(self):
        self.baudCombo.addItems([str(i) for i in [50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200][::-1]])
        self.bytesizeCombo.addItems([str(i) for i in [5, 6, 7, 8][::-1]])
        self.parityCombo.addItem('N')
        self.stopbitsCombo.addItem('1')
    def initButton(self):
        # self.qbtn = QPushButton('Quit', self)
        # self.qbtn.clicked.connect(QCoreApplication.instance().quit)
        #
        self.checkBtn.setStatusTip('Check port')
        self.checkBtn.clicked.connect(self.freshCombox)

        # self.openBtn.clicked.connect()
        self.closebtn .clicked.connect(sys.exit)
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