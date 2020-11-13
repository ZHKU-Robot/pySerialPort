import threading
import time

from PyQt5.QtGui import QTextCursor

import mySerial


class Signal():
    def __init__(this,self):
        this.self=self


    def closeSerialPortSignals(this):
        this.self.debugtextBrowser.append(str(this.self.myPort.ser.is_open))
        if this.self.open:
            this.self.autosend = 0
            this.self.open = False
            this.self.progressBar.setValue(0)
            this.self.progressBar.setFormat("等待你的再次打开么么哒(づ￣ 3￣)づ")
            this.self.myPort.ser.close()
        else:
            this.self.errorMessageBox.warning("请先打开串口", '我求你了')
        this.self.closebtn.released.disconnect(this.self.signals.closeSerialPortSignals)
        this.self.closebtn.released.connect(this.self.signals.closeSerialPortSignals)
    def openMyPortSignals(this):
        if not this.self.open:
            comx = this.self.comxCombo.currentText().lower()
            baud = eval(this.self.baudCombo.currentText())
            maxtime = eval(this.self.timeoutSpinBox.text())
            bytesize = eval(this.self.bytesizeCombo.currentText())
            parity = this.self.parityCombo.currentText()
            stopbit = eval(this.self.stopbitsCombo.currentText())
            try:
                this.self.myPort = mySerial.Port(comx, baud, maxtime, bytesize, parity, stopbit)
            except Exception as e:
                this.self.errorMessageBox.warning(str(e), "参数设置错误,无法打开串口")
                return
            # TODO 有bug,放进线程会崩掉
            this.self.open = this.self.myPort.ser.is_open
            mode = [k for k, v in this.self.opDict.items() if v == True][0]
            this.self.data = this.self.myPort.getWholeData(mode)
            th = threading.Thread(target=this.self.listener.listenAcceptedData, name='getWholedata', )
            th.start()
            if(this.self.tab==0):
                for i in range(101):
                    this.self.progressBar.setValue(i)
                    time.sleep(0.01)
                    this.self.progressBar.setFormat("正在为您打开串口{}%(✪ω✪)".format(this.self.progressBar.value()))
                this.self.progressBar.setFormat("串口打开成功 (*^▽^*)")
                # TODO 有bug,放进线程会崩掉
                this.self.init.debugTextBrowserInit(this.self)

            elif(this.self.tab==1):
                if(this.self.draw):
                    this.self.painterTextBrowser.append('串口已打开,看我绘图!')
                    this.drawSignals()
                else:
                    this.self.painterTextBrowser.append('绘图没打开也!')

                # TODO 有bug这里
            this.self.closebtn.released.connect(this.self.signals.closeSerialPortSignals)


        else:
            this.self.errorMessageBox.QMessageBox()

        this.self.open = this.self.myPort.ser.is_open


    def drawSignals(this):
        if this.self.drawCheckBtn.checkState():
            this.self.draw = 1
            this.self.painterTextBrowser.append('开启绘图模式')
            if (this.self.open):
                if (this.self.draw):
                    # self.timer1=QTimer(self)
                    # self.timer1.timeout.connect(self.getMCU8050Data)
                    # self.timer1.start(50)
                    if this.self.getMCUThread.is_alive():
                        pass
                    else:
                        this.self.getMCUThread = threading.Thread(target=this.self.getMCU8050Data)
                        this.self.getMCUThread.start()
                    # QMessageBox.warning(self, '串口未打开', '串口未打开ε＝ε＝ε＝(#>д<)ﾉ无法绘图')
                else:
                    if (not this.self.open):
                        this.self.painterTextBrowser.append('串口未打开,无法绘图')
            else:

                this.self.painterTextBrowser.append('等待打开串口')
        else:
            this.self.draw = 0
            this.self.painterTextBrowser.append('已中断绘图')
    def acceptedBtnSingals(this):
        this.self.acceptedData=this.self.acceptedcheckBox.checkState()
    def tabChangedSingals(this):
        this.self.tab=this.self.tabWidget.currentIndex()
        if(this.self.tab==0):
            this.self.debugtextBrowser.append("欢迎来到实力至上主义的接收发送区")
            # this.self.textRadioButton_2.setChecked(1)
        elif(this.self.tab==1):
            if(this.self.draw):
                this.self.hexRadioButton.setChecked(1)

                if(this.self.open):
                    this.self.painterTextBrowser.append('开始自动绘图..')
                    this.drawSignals()
                else:
                    this.self.painterTextBrowser.append("已经自动切换至16进制模式,等待打开串口")

            else:
                this.self.painterTextBrowser.append('正在等待打开绘画模式')
        this.textRadioButtonChangeSingals()
    def textRadioButtonChangeSingals(this):
        this.self.opDict = {'hex': this.self.hexRadioButton.isChecked(), 'text': this.self.textRadioButton_2.isChecked(), }
    def debugtextBrowerSignals(this):
        this.self.debugtextBrowser.moveCursor(QTextCursor.End)
    def freshComboxSignals(this):
        ports = mySerial.checkPorts()
        this.self.comxCombo.clear()
        for port in ports:
            this.self.comxCombo.addItem(port)
        this.self.ports=ports
    def acceptedTextBrowserSignals(this):
        this.self.acceptedTextBrowser.moveCursor(QTextCursor.End)
    def freshComboxSignals(this):
        ports = mySerial.checkPorts()
        this.self.comxCombo.clear()
        for port in ports:
            this.self.comxCombo.addItem(port)
