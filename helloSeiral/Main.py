import sys
import time

from PyQt5.QtGui import QIcon, QTextCursor
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic.properties import QtGui

from mainwindow import Ui_MainWindow  # 加载我们的布局
from dialog import Ui_AboutRobot
import mySerial
import threading
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
#创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self,width=5, height=4, dpi=100):
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)
    #第四步：就是画图，【可以在此类中画，也可以在其它类中画】
    def plotsin(self):
        self.axes0 = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes0.plot(t, s)
    def plotcos(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)

class ErrorMessage():
    def __init__(self, qWindow):
        self.qMainWindow = qWindow

    def warning(self, title, content):
        QMessageBox.warning(self.qMainWindow, title, content, QMessageBox.Ok, QMessageBox.Ok)

    def QMessageBox(self):
        self.qMainWindow.qmb = QMessageBox()
        self.qMainWindow.qmb.setText("你已经打开了串口啦(* ￣3)(ε￣ *)")
        self.qMainWindow.qmb.setInformativeText("o(>﹏<)o不要再打开了,呜呜呜")
        self.qMainWindow.qmb.setStandardButtons(QMessageBox.Ok)
        self.qMainWindow.qmb.setWindowTitle("(づ￣3￣)づ╭❤～BIUBIU")
        self.qMainWindow.qmb.show()
        pass


class AboutDialog(Ui_AboutRobot,QDialog,QWidget):
    def __init__(self, parent=None):
        # Here you're passing self as a parent argument to QMainWindow.__init__,
        # so you're trying to set the not yet fully-initialized object as a
        # parent of itself.
        # > You probably want either "super().__init__()" or
        # > "QtWidgets.QMainWindow.__init__(self)" here.
        super(AboutDialog,self).__init__(parent=parent)
        # Ui_AboutRobot.__init__(self)
        self.setupUi(self)  # 初始化ui


class UsingTest(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(UsingTest, self).__init__(*args, **kwargs)
        self.setupUi(self)  # 初始化ui
        self.initIcon()
        self.initVar()
        self.initCombox()
        self.freshCombox()
        self.initButton()
        self.initMain()

    def aboutDialog(self):
        about = AboutDialog()
        about.setWindowIcon(self.winIcon)
        about.setWindowTitle('关于 CC 关于 robot 关于 兴爷')
        about.setModal(1)
        about.exec_()

    def closeSerialPort(self):
        if self.open:
            self.myPort.ser.close()
            self.open = self.myPort.ser.is_open
            self.autosend = 0
            self.hang = 0
        else:
            self.errorMessageBox.warning("请先打开串口", '我求你了')

    def debugTextBrowserInit(self):
        self.debugtextBrowser.setText(self.myPort.getInfo())
        self.debugtextBrowser.textChanged.connect(self.debugtextBrowerSignals)

    def autoSend(self, itv):
        self.autosend = self.autoCheckBox.isChecked()
        if (self.autosend):
            self.debugtextBrowser.append("已开启 自动 发送 模式 ")
        else:

            self.debugtextBrowser.append("已关闭 自动 发送 模式 ")

        while (self.autosend):
            self.sendData2MyPort()
            time.sleep(int(itv) / 1000)

    def autoSendinit(self):
        if self.open:
            interval = self.sendLineEdit_4.text()
            if (not interval.isdigit()):
                self.autoCheckBox.setChecked(0)

            else:
                th = threading.Thread(target=self.autoSend, args=([interval]))
                th.start()

        else:
            self.errorMessageBox.warning('请先打开串口', '打开串口先哦')

    def closeEvent(self, a0) -> None:
        self.hang = False
        self.autosend = 0

    # TODO 待改进
    def debugtextBrowerSignals(self):

        self.debugtextBrowser.moveCursor(QTextCursor.End)

    def acceptedTextBrowserSignals(self):
        self.acceptedTextBrowser.moveCursor(QTextCursor.End)

    def initVar(self):
        self.autosend = 0
        self.open = False
        self.errorMessageBox = ErrorMessage(self)

    def listenAcceptedData(self, options):
        print("-------- start hanging to read data -------- ")
        self.acceptedTextBrowser.textChanged.connect(self.acceptedTextBrowserSignals)
        while (self.hang):
            try:
                data = self.myPort.getWholeData(options)
            except Exception as e:
                self.debugtextBrowser.append(str(e))
            if (data):
                self.acceptedTextBrowser.append(data)
                self.lcdNumber.display(str(self.lcdNumber.intValue() + len(data)))

            elif (data == False):
                self.debugtextBrowser.append('sorry,爱心光波无法到达,出现了编码错误')

    def sendData2MyPort(self):

        if self.open:
            self.sendtext = self.sendedRegion.toPlainText()
            self.debugtextBrowser.append("发送了{}".format(self.sendtext + '\n'))
            sendCount = self.myPort.writeData(self.sendtext + '\r\n')
            self.lcdNumber_2.display(str(self.lcdNumber_2.intValue() + sendCount))
            self.debugtextBrowser.append("你发送了 {}颗小心心 ♥(ˆ◡ˆԅ)❤".format(sendCount))
        else:
            self.errorMessageBox.warning('请先打开串口', '打开串口先哦')

    def openMyPort(self):

        if not self.open:
            comx = self.comxCombo.currentText().lower()
            baud = eval(self.baudCombo.currentText())
            maxtime = eval(self.timeoutSpinBox.text())
            bytesize = eval(self.bytesizeCombo.currentText())
            parity = self.parityCombo.currentText()
            stopbit = eval(self.stopbitsCombo.currentText())
            try:
                self.myPort = mySerial.Port(comx, baud, maxtime, bytesize, parity, stopbit)
            except Exception as e:
                self.errorMessageBox.warning(str(e), "参数设置错误,无法打开串口")
                return

            self.open = self.myPort.ser.is_open
            self.closebtn.clicked.connect(self.closeSerialPort)
            self.debugTextBrowserInit()
            self.opDict = {'hex': self.hexRadioButton.isChecked(), 'text': self.textRadioButton_2.isChecked(),
                           'oct': self.octRadioButton_3.isChecked()}
            self.hang = 1
            th = threading.Thread(target=self.listenAcceptedData, name='getWholedata',
                                  args=([[k for k, v in self.opDict.items() if v == True][0]]))
            th.start()
            self.progressBar.moveToThread(self.thread())
            for i in range(101):
                self.progressBar.setValue(i)
                time.sleep(0.01)
                self.progressBar.setFormat("正在为您打开串口{}%(✪ω✪)".format(self.progressBar.value()))
            self.progressBar.setFormat("串口打开成功 (*^▽^*)")
        else:

            self.errorMessageBox.QMessageBox()

    def initCombox(self):
        self.comxCombo.addItems(mySerial.checkPorts())
        self.baudCombo.addItems([str(i) for i in [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
                                                  9600, 19200, 38400, 57600, 115200, 230400, 460800, 500000,
                                                  576000, 921600, 1000000, 1152000, 1500000, 2000000, 2500000,
                                                  3000000, 3500000, 4000000][::-1]])
        self.baudCombo.setCurrentText('115200')
        self.bytesizeCombo.addItems([str(i) for i in [5, 6, 7, 8][::-1]])
        self.parityCombo.addItems(['none', 'even', 'odd', 'mark', 'space'])
        self.stopbitsCombo.addItems(['1', '1.5', '2'])

    def initButton(self):
        # self.qbtn = QPushButton('Quit', self)
        # self.qbtn.clicked.connect(QCoreApplication.instance().quit)
        #
        self.checkBtn.setStatusTip('Check port')
        self.checkBtn.clicked.connect(self.freshCombox)

        self.openBtn.clicked.connect(self.openMyPort)
        self.sendBtn.clicked.connect(self.sendData2MyPort)
        self.cleanDebugBtn.clicked.connect(self.debugtextBrowser.clear)
        self.cleanAcceptedBtn.clicked.connect(self.acceptedTextBrowser.clear)
        self.autoCheckBox.stateChanged.connect(self.autoSendinit)
        self.aboutBtn.clicked.connect(self.aboutDialog)

    def freshCombox(self):
        ports = mySerial.checkPorts()
        self.comxCombo.clear()
        for port in ports:
            self.comxCombo.addItem(port)

    def initIcon(self):
        self.winIcon = QIcon("img/kissing_face_with_closed_eyes_128px_1214135_easyicon.net.ico")

        self.setWindowIcon(self.winIcon)

    def initMain(self):
        # self.setCentralWidget(QLabel("SERIAL PORT ASSISTANT"))
        # self.setGeometry(500, 600, 550, 550)

        self.setWindowTitle('SrialPort Assistant By YJC')


if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    win = UsingTest()
    win.show()
    sys.exit(app.exec_())
