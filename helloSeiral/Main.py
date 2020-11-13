import os
import sys
import time
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from mainwindow import Ui_MainWindow  # 加载我们的布局
from AboutDiaglog import AboutDialog
from pyQTInit import PyQtInitialization
import qdarkstyle
from PyQt5.QtCore import Qt
class UsingTest(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):

        super(UsingTest, self).__init__(*args, **kwargs)
        self.setupUi(self)  # 初始化ui
        # self.setWindowFlag(Qt.FramelessWindowHint )
        # self.setWindowFlag(Qt.WindowCloseButtonHint )
        self.init = PyQtInitialization(self)
    def rotateLogo(self,logo,rollSub,pitchSub,yawSub):
        logo.rotate(rollSub, 1, 0, 0)
        logo.rotate(pitchSub, 0, 1, 0)
        logo.rotate(yawSub, 0, 0, 1)
    def draw3D(self):



        rollSub = self.curRollAngle - self.rollAngle
        pitchSub = self.curPitchAngle - self.pitchAngle

        yawSub = self.curYawAngle - self.yawAngle

        # 正数代表要向正方转sub度
        self.positiveAxis.rotate(rollSub, 1, 0, 0)
        self.positiveAxis.rotate(pitchSub, 0, 1, 0)
        self.positiveAxis.rotate(yawSub, 0, 0, 1)

        self.rotateLogo(self.logo,rollSub,pitchSub,yawSub)
        self.rotateLogo(self.logo2,rollSub,pitchSub,yawSub)
        self.rotateLogo(self.logo3,rollSub,pitchSub,yawSub)
        self.rotateLogo(self.logo4,rollSub,pitchSub,yawSub)
        self.rotateLogo(self.logo5,rollSub,pitchSub,yawSub)
        self.rotateLogo(self.logo6,rollSub,pitchSub,yawSub)


        self.negativeAxis.rotate(rollSub, 1, 0, 0)
        self.negativeAxis.rotate(pitchSub, 0, 1, 0)
        self.negativeAxis.rotate(yawSub, 0, 0, 1)

        # pass
        self.rollAngle = self.curRollAngle
        self.pitchAngle = self.curPitchAngle
        self.yawAngle = self.curYawAngle

    def updateText(self):
        self.rollText.setText('%0.1f°' % (self.rollData[-1]))
        self.pitchText.setText('%0.1f°' % (self.pitchData[-1]))
        self.yawText.setText('%0.1f°' % (self.yawData[-1]))

    def drawFigure(self):
        if issubclass(type(self.mpuData), Exception):
            self.drawTextBrowser.append('出错了!!' + '这可能是由于你传输了错误的8050帧格式')
        # print(se)
        if self.mpuData:
            self.curRollAngle = self.mpuData[-3]
            self.curPitchAngle = self.mpuData[-2]
            self.curYawAngle = self.mpuData[-1]

            # self.rollData[:-1] = self.rollData[1:]
            # self.rollData[-1] = self.curRollAngle
            self.rollData.append( self.curRollAngle)
            # print(self.rollData[-1])
            # self.positiveAxis.rotate(self.rollData[-1], 1, 0, 0)
            # self.negativeAxis.rotate(self.rollData[-1], 0, 0, 0)
            lastIndex = 100

            self.curveRoll.setData(self.rollData)
            self.curveRoll.setPos(self.Index+lastIndex, 0)

            self.rollText.setPos(self.Index+lastIndex, self.rollData[-1])
            self.rollArrow.setPos(self.Index+lastIndex, self.rollData[-1])

            self.curvePitch.setData(self.pitchData)
            self.curvePitch.setPos(lastIndex, 0)
            self.pitchText.setPos(lastIndex, self.pitchData[-1])
            self.pitchArrow.setPos(lastIndex, self.pitchData[-1])

            self.curveYaw.setData(self.yawData)
            self.curveYaw.setPos(lastIndex, 0)
            self.yawText.setPos(lastIndex, self.yawData[-1])
            self.yawArrow.setPos(lastIndex, self.yawData[-1])

            self.pitchData[:-1] = self.pitchData[1:]
            self.pitchData[-1] = self.mpuData[-2]
            self.curvePitch.setData(self.pitchData)
            self.curvePitch.setPos(lastIndex, 0)

            self.yawData[:-1] = self.yawData[1:]
            self.yawData[-1] = self.mpuData[-1]
            self.curveYaw.setData(self.yawData)
            self.curveYaw.setPos(lastIndex, 0)
            self.Index+=1
            time.sleep(.01)

    def getMCU8050Data(self):

        code = getattr(self, 'data', 1)
        while (code == 1):
            code = getattr(self, 'data', 1)
            self.painterTextBrowser.append('data错误data错误')
        self.painterTextBrowser.append('数据流一切正常,给我冲')
        while self.open:
            if self.acceptedData == 2:
                if (self.draw):
                    self.mpuData = self.myPort.decodeMPU6050(self.data)
                    if (type(self.mpuData) == Exception):
                        self.debugtextBrowser.append('mpudata错误')
                    else:
                        self.drawFigure()
                        self.draw3D()
                else:
                    self.painterTextBrowser.append('绘图已中断,开始等待')
                    time.sleep(1)

            else:
                self.painterTextBrowser.append('数据流已中断,正在重试,1s后再次检测!!!')
                time.sleep(1)

    def sendData2MyPort(self):
        if self.open:
            self.sendtext = self.sendedRegion.toPlainText()
            self.debugtextBrowser.append("发送了{}".format(self.sendtext + '\n'))
            sendCount = self.myPort.writeData(self.sendtext + '\r\n')
            self.lcdNumber_2.display(str(self.lcdNumber_2.intValue() + sendCount))
            self.debugtextBrowser.append("你发送了 {}颗小心心 ♥(ˆ◡ˆԅ)❤".format(sendCount))
        else:
            self.errorMessageBox.warning('请先打开串口', '打开串口先哦')

    def aboutDialog(self):
        about = AboutDialog()
        about.setWindowIcon(self.winIcon)
        about.setWindowTitle('关于 CC 关于 robot 关于 兴爷')
        about.setModal(1)
        about.exec_()

    # debugtextBrower--------------------------------------

    def closeEvent(self, a0) -> None:
        self.autosend = 0
        if getattr(self, 'myPort', 1) == 1:
            pass
        else:
            self.myPort.ser.close()
        self.open = 0
        self.draw = 0
        for i in range(100,0,-1):
            self.setWindowOpacity(i/100)
            time.sleep(0.005)

if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)

    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    app.setStyleSheet(dark_stylesheet)
    win = UsingTest()

    win.show()
    sys.exit(app.exec_())
