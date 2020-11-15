import threading
import time

from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QMainWindow
from mainwindow import Ui_MainWindow  # 加载我们的布局
import mySerial
"""
信号类:
管理全局所有各种各样的信号
"""
class MainWindowSignal(QMainWindow,Ui_MainWindow):

    @staticmethod
    def drawSignals(self):
        if self.drawCheckBtn.isChecked():
            self.draw = 1
            self.painterTextBrowser.append('开启绘图线程')
            if (self.open):
                if (self.draw):
                    # self.timer1=QTimer(self)
                    # self.timer1.timeout.connect(self.getMCU8050Data)
                    # self.timer1.start(50)
                    if self.getMCUThread.is_alive():
                        pass
                    else:
                        self.getMCUThread = threading.Thread(target=self.listener.getMCU8050DataListener, args=[self])
                        self.getMCUThread.start()
                    # QMessageBox.warning(self, '串口未打开', '串口未打开ε＝ε＝ε＝(#>д<)ﾉ无法绘图')
            else:
                self.painterTextBrowser.append('等待打开串口')
        else:
            self.draw = 0
            self.painterTextBrowser.append('已中断绘图')
    @staticmethod
    def acceptedBtnSingals(self):
        """
        从1到0
        """
        if self.acceptedData:
            self.errorMessageBox.warning("获取数据线程已退出","如要使用请重新再次勾选")
            self.acceptedData=self.acceptedcheckBox.isChecked()
        else:
            self.acceptedData=self.acceptedcheckBox.isChecked()
            #开启线程
            MainWindowSignal.drawSignals(self)
            threading.Thread(target=self.listener.acceptedDataListener, args=([self]), name='getWholedata', ).start()

    @staticmethod
    def tabChangedSingals(self):

        self.tab=self.tabWidget.currentIndex()
        if(self.tab==0):
            self.debugtextBrowser.append("欢迎来到实力至上主义的接收发送区")
            # this.self.textRadioButton_2.setChecked(1)
        elif(self.tab==1):
            if(self.draw):
                self.hexRadioButton.setChecked(1)
                if(self.open):
                    self.painterTextBrowser.append('自动绘图初始化成功..')
                    MainWindowSignal.drawSignals(self)
                else:
                    self.painterTextBrowser.append("已经自动切换至16进制模式,等待打开串口")

            else:
                self.painterTextBrowser.append('正在等待打开绘画模式')
        MainWindowSignal.textRadioButtonChangeSingals(self)

    def textRadioButtonChangeSingals(self):
        self.opDict = {'hex': self.hexRadioButton.isChecked(), 'text': self.textRadioButton_2.isChecked(), }
    @staticmethod
    def debugtextBrowerSignals(self):
        self.debugtextBrowser.moveCursor(QTextCursor.End)
    @staticmethod
    def freshComboxSignals(self):
        ports = mySerial.checkPorts()
        self.comxCombo.clear()
        for port in ports:
            self.comxCombo.addItem(port)
        self.ports=ports
    @staticmethod
    def acceptedTextBrowserSignals(self):
        self.acceptedTextBrowser.moveCursor(QTextCursor.End)
    @staticmethod
    def freshComboxSignals(self):
        ports = mySerial.checkPorts()
        self.comxCombo.clear()
        for port in ports:
            self.comxCombo.addItem(port)
