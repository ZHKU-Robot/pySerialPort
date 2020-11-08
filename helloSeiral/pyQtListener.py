import time


class Listener():
    def __init__(this,self):
        this.self=self
    def autoSend(this, itv):
        this.self.autosend = this.self.autoCheckBox.isChecked()
        if (this.self.autosend):
            this.self.debugtextBrowser.append("已开启 自动 发送 模式 ")
        else:
            this.self.debugtextBrowser.append("已关闭 自动 发送 模式 ")
        while (this.self.autosend):
            this.self.sendData2MyPort()
            time.sleep(int(itv) / 1000)
    # TODO 待改进

    def listenAcceptedData(this):
        print("--------已经开始自动接收数据-------- ")
        this.self.acceptedTextBrowser.textChanged.connect(this.self.signals.acceptedTextBrowserSignals)

        while (this.self.open):
            if this.self.acceptedData==2:
                mode=[k for k, v in this.self.opDict.items() if v == True][0]
                this.self.data = this.self.myPort.getWholeData(mode)
                # time.sleep(this.self.interval)
                if (this.self.tab == 0):
                    if(type(this.self.data)==UnicodeDecodeError):
                        this.self.debugtextBrowser.append("error.."+str (this.self.data))
                    else:
                        this.self.acceptedTextBrowser.append(str(this.self.data))
                        this.self.lcdNumber.display(str(this.self.lcdNumber.intValue() + len(this.self.data)))
                elif(this.self.tab == 1):
                    if(type(this.self.data)==UnicodeDecodeError):
                        this.self.painterTextBrowser.append("error.."+str (this.self.data))

                    else:
                        this.self.lcdNumber.display(str(this.self.lcdNumber.intValue() + len(this.self.data)))