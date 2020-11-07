import sys
import time

import numpy as np
from PyQt5 import sip
from PyQt5.QtCore import QObject, QTimer
from PyQt5.QtGui import QIcon, QTextCursor, QCloseEvent
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic.properties import QtGui
from QplotThread import Pic
from mainwindow import Ui_MainWindow  # 加载我们的布局
from dialog import Ui_AboutRobot
import mySerial
import threading
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用pyqt5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg  # pyqt5的画布
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation


class MyMatPlotAnimation(FigureCanvasQTAgg):
    """
    创建一个画板类，并把画布放到容器（画板上）FigureCanvasQTAgg，再创建一个画图区
    """

    def __init__(self, width=10, heigh=10, dpi=100):
        # 创建一个Figure,该Figure为matplotlib下的Figure，不是matplotlib.pyplot下面的Figure
        self.figs = Figure(figsize=(width, heigh), dpi=dpi)
        super(MyMatPlotAnimation, self).__init__(self.figs)
        self.figs.patch.set_facecolor('#01386a')  # 设置绘图区域颜色
        self.axes = self.figs.add_subplot(111)
        self.startIndex=0
        self.endIndex=5
        self.step=0.01
        self.t = np.array(np.arange(0, 5, self.step))



    def set_mat_func(self,s):
        """
        初始化设置函数
        """
        self.s =np.cos(self.t*np.pi*s)
        self.axes.cla()
        self.axes.patch.set_facecolor("#01386a")  # 设置ax区域背景颜色
        self.axes.patch.set_alpha(0.5)  # 设置ax区域背景颜色透明度

        # self.axes.spines['top'].set_color('#01386a')
        self.axes.spines['top'].set_visible(False)  # 顶边界不可见
        self.axes.spines['right'].set_visible(False)  # 右边界不可见

        self.axes.xaxis.set_ticks_position('bottom')  # 设置ticks（刻度）的位置为下方
        self.axes.yaxis.set_ticks_position('left')  # 设置ticks（刻度） 的位置为左侧
        # 设置左、下边界在（0，0）处相交
        # self.axes.spines['bottom'].set_position(('data', 0))  # 设置x轴线再Y轴0位置
        self.axes.spines['left'].set_position(('data', 0))  # 设置y轴在x轴0位置
        self.axes.set_ylim([-180,180])
        self.plot_line, = self.axes.plot([], [], 'r-', linewidth=1)  # 注意‘,’不可省略


    def plot_tick(self):
        plot_line = self.plot_line
        plot_axes = self.axes
        t = self.t

        def upgrade(i):  # 注意这里是plot_tick方法内的嵌套函数
            x_data = []  # 这里注意如果是使用全局变量self定义，可能会导致绘图首位相联
            y_data = []
            for i in range(len(t)):
                x_data.append(i)
                y_data.append(self.s[i])
            plot_axes.plot(x_data, y_data, 'r-', linewidth=1)
            return plot_line,  # 这里也是注意‘,’不可省略，否则会报错

        ani = FuncAnimation(self.figs, upgrade, blit=True, repeat=False)
        self.figs.canvas.draw()  # 重绘还是必须要的
        self.t=np.hstack([self.t[1:],[self.t[-1]+self.step]])



    #第四步：就是画图，【可以在此类中画，也可以在其它类中画】
    # def plot
    # def plotsin(self):
    #     self.axes0 = self.fig.add_subplot(111)
    #     t = np.arange(0.0, 3.0, 0.01)
    #     s = np.sin(2 * np.pi * t)
    #     self.axes0.plot(t, s)
    # def plotcos(self):
    #     t = np.arange(0.0, 3.0, 0.01)
    #     s = np.sin(2 * np.pi * t)
    #     self.axes.plot(t, s)

class ErrorMessage():
    def __init__(self, qWindow):
        self.qMainWindow = qWindow

    def warning(self, title, content):
        QMessageBox.warning(self.qMainWindow, title, content)



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
        self.figureInit()
        self.initMain()
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
            # TODO 有bug,放进线程会崩掉
            for i in range(101):
                self.progressBar.setValue(i)
                time.sleep(0.01)
                self.progressBar.setFormat("正在为您打开串口{}%(✪ω✪)".format(self.progressBar.value()))
            self.progressBar.setFormat("串口打开成功 (*^▽^*)")
            th = threading.Thread(target=self.listenAcceptedData, name='getWholedata',
                                  )
            th.start()
            #TODO 有bug这里
            self.closebtn.released.connect(self.closeSerialPort)
            self.debugTextBrowserInit()
        else:
            self.errorMessageBox.QMessageBox()

        self.open=self.myPort.ser.is_open
    def closeSerialPort(self):
        self.debugtextBrowser.append(str(self.myPort.ser.is_open))
        if  self.myPort.ser.is_open:
            self.autosend = 0

            self.open=False
            self.progressBar.setValue(0)
            self.progressBar.setFormat("等待你的再次打开么么哒(づ￣ 3￣)づ")
            self.myPort.ser.close()
            self.rollfigure.startTimer(1000)



        else:
            self.errorMessageBox.warning("请先打开串口", '我求你了')
        self.closebtn.released.disconnect(self.closeSerialPort)
        self.closebtn.released.connect(self.closeSerialPort)

    def getMCU8050Data(self):
        if(self.tabWidget.currentIndex()==1):
            if(self.open==1):
                mpuData=self.myPort.decodeMPU6050(self.data)
                if mpuData:
                    for singleMpudata in mpuData:

                        # print(singleMpudata)
                        self.rollfigure.set_mat_func(singleMpudata[-3] )
                        self.rollfigure.plot_tick()
                        # self.rollfigure
                        # time.sleep(0.1)
                        self.timer.start(10)
            else:
                # time.sleep(1)
                pass
        else:
            pass
    def figureDraw(self):
        if(self.tabWidget.currentIndex()==1):
            #自动切换
            if(self.open==1):
                self.hexRadioButton.setChecked(1)
                self.textRadioButtonChange()
                self.timer=QTimer(self)
                self.timer.timeout.connect(self.getMCU8050Data)
                self.timer.start(10)
                # threading.Thread(target=self.getMCU8050Data).start()
            else:
                QMessageBox.warning(self, '串口未打开', '串口未打开ε＝ε＝ε＝(#>д<)ﾉ')
        else:
            pass


    def figureInit(self):
        self.tabWidget.currentChanged.connect(self.figureDraw)
        self.rollfigure = MyMatPlotAnimation(width=5, heigh=4, dpi=100)
        self.pitchfigure =MyMatPlotAnimation(width=5, heigh=4, dpi=100)
        self.yawfigure = MyMatPlotAnimation(width=5, heigh=4, dpi=100)

        self.rollLayout.addWidget(self.rollfigure)
        self.pitchLayout.addWidget(self.pitchfigure)
        self.yawLayout.addWidget(self.yawfigure)
    def textRadioButtonChange(self):
        self.opDict = {'hex': self.hexRadioButton.isChecked(), 'text': self.textRadioButton_2.isChecked(), }
    def aboutDialog(self):
        about = AboutDialog()
        about.setWindowIcon(self.winIcon)
        about.setWindowTitle('关于 CC 关于 robot 关于 兴爷')
        about.setModal(1)
        about.exec_()

    #debugtextBrower--------------------------------------
    def debugtextBrowerSignals(self):
        self.debugtextBrowser.moveCursor(QTextCursor.End)
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



    # TODO 待改进

    def acceptedTextBrowserSignals(self):
        self.acceptedTextBrowser.moveCursor(QTextCursor.End)


    def listenAcceptedData(self):
        print("-------- start hanging to read data -------- ")
        self.acceptedTextBrowser.textChanged.connect(self.acceptedTextBrowserSignals)
        while (self.myPort.ser.is_open):
                self.data = self.myPort.getWholeData([k for k, v in self.opDict.items() if v == True][0])
                # time.sleep(self.interval)
                if(type(self.data)==UnicodeDecodeError):
                    self.debugtextBrowser.append("error.."+str (self.data))
                else:
                    if(self.tabWidget.currentIndex()==0):
                        self.acceptedTextBrowser.append(str(self.data))
                    self.lcdNumber.display(str(self.lcdNumber.intValue() + len(self.data)))

    def sendData2MyPort(self):

        if self.open:
            self.sendtext = self.sendedRegion.toPlainText()
            self.debugtextBrowser.append("发送了{}".format(self.sendtext + '\n'))
            sendCount = self.myPort.writeData(self.sendtext + '\r\n')
            self.lcdNumber_2.display(str(self.lcdNumber_2.intValue() + sendCount))
            self.debugtextBrowser.append("你发送了 {}颗小心心 ♥(ˆ◡ˆԅ)❤".format(sendCount))
        else:
            self.errorMessageBox.warning('请先打开串口', '打开串口先哦')





    #
    def freshCombox(self):
        ports = mySerial.checkPorts()
        self.comxCombo.clear()
        for port in ports:
            self.comxCombo.addItem(port)
    def initCombox(self):
        self.comxCombo.addItems(mySerial.checkPorts())
        self.baudCombo.addItems([str(i) for i in [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
                                                  9600, 19200, 38400, 57600, 115200, 230400, 460800, 500000,
                                                  576000, 921600, 1000000, 1152000, 1500000, 2000000, 2500000,
                                                  3000000, 3500000, 4000000][::-1]])
        self.baudCombo.setCurrentText('500000')
        self.bytesizeCombo.addItems([str(i) for i in [5, 6, 7, 8][::-1]])
        self.parityCombo.addItems(['none', 'even', 'odd', 'mark', 'space'])
        self.stopbitsCombo.addItems(['1', '1.5', '2'])
    def initVar(self):
        self.interval=0.01
        self.autosend = 0
        self.open = False
        self.errorMessageBox = ErrorMessage(self)
        self.opDict = {'hex': self.hexRadioButton.isChecked(), 'text': self.textRadioButton_2.isChecked(), }

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

        self.textRadioButton_2.clicked.connect(self.textRadioButtonChange)
        self.hexRadioButton.clicked.connect(self.textRadioButtonChange)
    def initIcon(self):
        self.winIcon = QIcon("img/kissing_face_with_closed_eyes_128px_1214135_easyicon.net.ico")

        self.setWindowIcon(self.winIcon)

    def initMain(self):
        # self.setCentralWidget(QLabel("SERIAL PORT ASSISTANT"))
        # self.setGeometry(500, 600, 550, 550)

        self.setWindowTitle('SrialPort Assistant By YJC')


    def closeEvent(self, a0) -> None:
        self.autosend = 0
        if getattr(self,'myPort',1)==1:
            pass
        else:
            self.myPort.ser.close()
if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    win = UsingTest()
    win.show()
    sys.exit(app.exec_())
