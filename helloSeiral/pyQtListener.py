import time


"""
出现错误后重试的时间
"""
BREAK=3

class MainWindowListener():
    @staticmethod
    def autoSendListener(self, inv):
        self.autoSendFlag = self.autoCheckBox.isChecked()
        if (self.autoSendFlag):
            self.debugtextBrowser.append("已开启 自动 发送 模式 ")
        else:
            self.debugtextBrowser.append("已关闭 自动 发送 模式 ")

        while (self.autoSendFlag):
            self.action.sendData2MyPort(self)
            time.sleep(int(inv) / 1000)
    # TODO 待改进
    @staticmethod
    def acceptedDataListener(self):

        print("--------已经开始自动接收数据-------- ")
        self.acceptedTextBrowser.textChanged.connect(self.signals.acceptedTextBrowserSignals)

        while (self.open and self.acceptedData):
            mode=[k for k, v in self.opDict.items() if v == True][0]
            self.data = self.myPort.getWholeData(mode)
            if self.data!=[]:
                if (issubclass(type(self.data) ,Exception)):
                    pass
                    self.debugtextBrowser.append("error.." + str(self.data))
                    self.painterTextBrowser.append("error.." + str(self.data))
                else:
                    self.acceptedTextBrowser.append(str(self.data))
                    self.lcdNumber.display(str(self.lcdNumber.intValue() + len(self.data)))
    @staticmethod
    def getMCU8050DataListener(self):
        self.painterTextBrowser.append('开启MCU8050数据流监听')
        while self.open and self.acceptedData:
            if self.data!=[]:
                self.mpuData = self.myPort.decodeMPU6050(self.data)
                if (issubclass(type(self.mpuData),Exception)):
                    self.painterTextBrowser.append('mpudata错误'+str(self.mpuData))
                    time.sleep(BREAK)
                else:
                    if (self.draw):
                        self.action.drawFigure(self)
                        self.action.draw3D(self)
                    else:
                        self.painterTextBrowser.append('绘图已中断,开始等待')
                        time.sleep(BREAK)
            else:
                self.painterTextBrowser.append('数据流是空,等待3s后再次尝试')
                time.sleep(BREAK)
