import threading
import pyqtgraph as pg
from PyQt5.QtGui import QIcon
from pyQtErrorMessage import ErrorMessage
import numpy as np
import mySerial
from pyQtSignal import Signal
from pyQtListener import Listener

class PyQtInitialization():
    def __init__(this,self):
        this.self=self
        this.initSingals(self)
        this.initVar(self)
        this.initCombox(self)
        this.initButton(self)
        this.initListener(self)
        this.initIcon(self)
        this.figureInit(self)
        # this.autoCheckBox(self)
        this.initMain(self)
    def initListener(this,self):
        self.listener=Listener(self)
    def initSingals(this,self):
        self.signals=Signal(self)
    def figureInit(this,self):
        self.rollDrawing=pg.PlotWidget()
        self.Index=0
        self.rollData=np.random.normal(size=100)
        self.curveRoll=self.rollDrawing.plot(self.rollData)

        self.pitchData = np.random.normal(size=100)
        self.yawData = np.random.normal(size=100)

        self.pitchDrawing=pg.PlotWidget()
        self.curvePitch=self.pitchDrawing.plot(self.pitchData)

        self.yawDrawing=pg.PlotWidget()
        self.curveYaw=self.yawDrawing.plot(self.yawData)
        self.rollLayout.addWidget(self.rollDrawing)
        self.pitchLayout.addWidget(self.pitchDrawing)
        self.yawLayout.addWidget(self.yawDrawing)

    def debugTextBrowserInit(this,self):
        self.debugtextBrowser.setText(self.myPort.getInfo())
        self.debugtextBrowser.textChanged.connect(self.signals.debugtextBrowerSignals)
    def autoSendinit(this):
        if this.self.open:
            interval = this.self.sendLineEdit_4.text()
            if (not interval.isdigit()):
                this.self.autoCheckBox.setChecked(0)

            else:
                th = threading.Thread(target=this.self.listener.autoSend, args=([interval]))
                th.start()

        else:
            this.self.errorMessageBox.warning('请先打开串口', '打开串口先哦')
    def initCombox(this,self):
        self.comxCombo.addItems(mySerial.checkPorts())
        self.baudCombo.addItems([str(i) for i in [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
                                                  9600, 19200, 38400, 57600, 115200, 230400, 460800, 500000,
                                                  576000, 921600, 1000000, 1152000, 1500000, 2000000, 2500000,
                                                  3000000, 3500000, 4000000][::-1]])
        self.baudCombo.setCurrentText('500000')
        self.bytesizeCombo.addItems([str(i) for i in [5, 6, 7, 8][::-1]])
        self.parityCombo.addItems(['none', 'even', 'odd', 'mark', 'space'])
        self.stopbitsCombo.addItems(['1', '1.5', '2'])

    def initVar(this,self):
        self.tab=self.tabWidget.currentIndex()
        self.autosend = 0
        self.open = False
        self.draw = self.drawCheckBtn.isChecked()
        self.signals.tabChangedSingals()
        self.acceptedData=2
        self.errorMessageBox = ErrorMessage(self)


    def initButton(this,self):
        # self.qbtn = QPushButton('Quit', self)
        # self.qbtn.clicked.connect(QCoreApplication.instance().quit)
        #
        self.checkBtn.setStatusTip('Check port')
        self.checkBtn.clicked.connect(self.signals.freshComboxSignals)

        self.openBtn.clicked.connect(self.signals.openMyPortSignals)
        self.sendBtn.clicked.connect(self.sendData2MyPort)
        self.cleanDebugBtn.clicked.connect(self.debugtextBrowser.clear)
        self.cleanAcceptedBtn.clicked.connect(self.acceptedTextBrowser.clear)
        self.autoCheckBox.stateChanged.connect(this.autoSendinit)
        self.aboutBtn.clicked.connect(self.aboutDialog)
        self.tabWidget.currentChanged.connect(self.signals.tabChangedSingals)
        self.textRadioButton_2.clicked.connect(self.signals.textRadioButtonChangeSingals)
        self.hexRadioButton.clicked.connect(self.signals.textRadioButtonChangeSingals)
        self.acceptedcheckBox.stateChanged.connect(self.signals.acceptedBtnSingals)
        self.drawCheckBtn.stateChanged.connect(self.signals.drawSignals)
    def initIcon(this,self):
        self.winIcon = QIcon("img/kissing_face_with_closed_eyes_128px_1214135_easyicon.net.ico")

        self.setWindowIcon(self.winIcon)

    def initMain(this,self):
        # self.setCentralWidget(QLabel("SERIAL PORT ASSISTANT"))
        # self.setGeometry(500, 600, 550, 550)

        self.setWindowTitle('SrialPort Assistant By YJC')