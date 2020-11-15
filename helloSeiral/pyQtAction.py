"""
动作类
"""
import threading
import time

import mySerial


"""
两张图渲染的间隔
"""
DRAWINTERVAL=0.01
class MainWindowAction():
    @staticmethod
    def closeSerialPortSignals(self):
        self.debugtextBrowser.append(str(self.myPort.ser.is_open))

        self.autosend = 0
        self.open = False
        self.progressBar.setValue(0)
        self.progressBar.setFormat("等待你的再次打开么么哒(づ￣ 3￣)づ")
        self.myPort.ser.close()

        self.errorMessageBox.warning("已关闭串口", '线程还未关闭')

        #TODO 有bug
        # self.closebtn.released.disconnect(lambda :self.signals.closeSerialPortSignals(self))
        # self.closebtn.released.connect(lambda :self.signals.closeSerialPortSignals(self))


    @staticmethod
    def openMyPortSignals(self):
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
            self.open = self.myPort.ser.is_open
            mode = [k for k, v in self.opDict.items() if v == True][0]
            self.data = self.myPort.getWholeData(mode)
            th = threading.Thread(target=self.listener.acceptedDataListener, args=([self]), name='getWholedata', )
            th.start()
            if(self.tab==0):
                for i in range(101):
                    self.progressBar.setValue(i)
                    time.sleep(0.01)
                    self.progressBar.setFormat("正在为您打开串口{}%(✪ω✪)".format(self.progressBar.value()))
                self.progressBar.setFormat("串口打开成功 (*^▽^*)")
                # TODO 有bug,放进线程会崩掉
                self.initdebugTextBrowser()

            elif(self.tab==1):
                if(self.draw):
                    self.painterTextBrowser.append('串口已打开,看我绘图!')
                    self.signals.drawSignals(self)
                else:
                    self.painterTextBrowser.append('绘图没打开也!')

                # TODO 有bug这里
            self.closebtn.released.connect(lambda :MainWindowAction.closeSerialPortSignals(self))


        else:
            self.errorMessageBox.QMessageBox()

        self.open = self.myPort.ser.is_open
    def rotateLogo(self,logo,rollSub,pitchSub,yawSub):
        logo.rotate(rollSub, 1, 0, 0)
        logo.rotate(pitchSub, 0, 1, 0)
        logo.rotate(yawSub, 0, 0, 1)

    @staticmethod
    def updateText(self):

        self.rollText.setText('%0.2f°' % (self.rollData[-1]))
        self.pitchText.setText('%0.2f°' % (self.pitchData[-1]))
        self.yawText.setText('%0.2f°' % (self.yawData[-1]))
    @staticmethod
    def drawFigure(self):

        self.curRollAngle = self.mpuData[-3]
        self.curPitchAngle = self.mpuData[-2]
        self.curYawAngle = self.mpuData[-1]


        # self.rollData.append( self.curRollAngle)
        # print(self.rollData[-1])
        lastIndex = 100

        self.rollData[:-1] = self.rollData[1:]
        self.rollData[-1] =  self.mpuData[-3]
        self.curveRoll.setData(self.rollData)
        self.curveRoll.setPos(lastIndex, 0)
        self.rollText.setPos(lastIndex, self.rollData[-1])
        self.rollArrow.setPos(lastIndex, self.rollData[-1])
        # self.curveRoll.setData(self.rollData)
        # self.curveRoll.setPos(self.Index+lastIndex, 0)
        #
        # self.rollText.setPos(self.Index+lastIndex, self.rollData[-1])
        # self.rollArrow.setPos(self.Index+lastIndex, self.rollData[-1])

        self.pitchData[:-1] = self.pitchData[1:]
        self.pitchData[-1] = self.mpuData[-2]
        self.curvePitch.setData(self.pitchData)
        self.curvePitch.setPos(lastIndex, 0)
        self.pitchText.setPos(lastIndex, self.pitchData[-1])
        self.pitchArrow.setPos(lastIndex, self.pitchData[-1])



        self.yawData[:-1] = self.yawData[1:]
        self.yawData[-1] = self.mpuData[-1]
        self.curveYaw.setData(self.yawData)
        self.curveYaw.setPos(lastIndex, 0)
        self.yawText.setPos(lastIndex, self.yawData[-1])
        self.yawArrow.setPos(lastIndex, self.yawData[-1])
        # self.Index+=1
        time.sleep(DRAWINTERVAL)

    @staticmethod
    def draw3D(self):
        rollSub = self.curRollAngle - self.rollAngle
        pitchSub = self.curPitchAngle - self.pitchAngle
        yawSub = self.curYawAngle - self.yawAngle
        # 正数代表要向正方转sub度
        #这里草了

        self.positiveAxis.rotate(rollSub, 1, 0, 0)
        self.negativeAxis.rotate(rollSub, 1, 0, 0)


        self.positiveAxis.rotate(yawSub, 0, 0, 1)
        self.negativeAxis.rotate(yawSub, 0, 0, 1)

        self.negativeAxis.rotate(pitchSub, 0, 1, 0)
        self.positiveAxis.rotate(pitchSub, 0, 1, 0)

        MainWindowAction.rotateLogo(self,self.logo,rollSub,pitchSub,yawSub)
        MainWindowAction.rotateLogo(self,self.logo2,rollSub,pitchSub,yawSub)
        MainWindowAction.rotateLogo(self,self.logo3,rollSub,pitchSub,yawSub)
        MainWindowAction.rotateLogo(self,self.logo4,rollSub,pitchSub,yawSub)
        MainWindowAction.rotateLogo(self,self.logo5,rollSub,pitchSub,yawSub)
        MainWindowAction.rotateLogo(self,self.logo6,rollSub,pitchSub,yawSub)


        self.rollAngle = self.curRollAngle
        self.pitchAngle = self.curPitchAngle
        self.yawAngle = self.curYawAngle
    @staticmethod
    def sendData2MyPort(self):
        if self.open:
            self.sendtext = self.sendedRegion.toPlainText()
            self.debugtextBrowser.append("发送了{}".format(self.sendtext + '\n'))
            sendCount = self.myPort.writeData(self.sendtext + '\r\n')
            self.lcdNumber_2.display(str(self.lcdNumber_2.intValue() + sendCount))
            self.debugtextBrowser.append("你发送了 {}颗小心心 ♥(ˆ◡ˆԅ)❤".format(sendCount))
        else:
            self.errorMessageBox.warning('请先打开串口', '打开串口先哦')