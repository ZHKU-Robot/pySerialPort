import threading
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon, QVector3D, QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow
from mainwindow import Ui_MainWindow  # 加载我们的布局
from pyQtErrorMessage import ErrorMessage
import numpy as np
import mySerial
from pyQtSignal import Signal
from pyQtListener import Listener
import pyqtgraph.opengl as gl
import pyqtgraph as pg
class PyQtInitialization(QMainWindow, Ui_MainWindow):
    def __init__(this, self):
        super(PyQtInitialization, this).__init__()
        this.self = self
        this.initSingals(self)
        this.initVar(self)
        this.initCombox(self)
        this.initButton(self)
        this.initListener(self)
        this.initIcon(self)
        this.figureInit(self)
        this.init3D(self)
        # this.autoCheckBox(self)
        this.initMain(self)

    def init3D(this, self):
        self.window3D = gl.GLViewWidget()

        self.window3D.opts['distance']=10
        self.window3D.opts['azimuth'] = 0
        self.window3D.opts['bgcolor'] = (0.1,0.1,0.1,1)

        # ax.plot_surface(x, y, z, color='b')

        ## create three grids, add each to the view
        self.positiveAxis = gl.GLAxisItem(QVector3D(10, 10, 10), )
        self.positiveAxis.scale(2,2,2)
        self.negativeAxis = gl.GLAxisItem(QVector3D(10, 10, 10), )
        self.negativeAxis.scale(2,2,2)
        # xgrid.setSize(x=10)

        # zgrid = gl.GLAxisItem(QVector3D(10,10,10))
        self.window3D.addItem(self.positiveAxis)
        self.window3D.addItem(self.negativeAxis)
        # self.window3D.addItem(ygrid)
        # self.window3D.addItem(zgrid)

        ## rotate x and y grids to face the correct direction
        self.negativeAxis.rotate(180, 0, 0, 0)
        # ygrid.rotate(90, 1, 0, 0)

        # n = 51
        # y = np.linspace(-10, 10, n)
        # x = np.linspace(-10, 10, 100)
        # self.rand=np.random.uniform(-10,10,size=1)
        # for i in range(n):
        #     yi = np.array([y[i]] * 100)
        #     d = (x ** 2 + yi ** 2) ** 0.5
        #     z = self.rand*d
        # u = np.linspace(0, 4 * np.pi, 100)
        # v = np.linspace(0, 4 * np.pi, 100)
        # x = np.outer(np.cos(u), np.sin(v))
        # y = np.outer(np.sin(u), np.sin(v))
        # z = np.outer(np.ones(np.size(u)), np.cos(v))
        # pts = [x, y, z]
        # sp2 = gl.GLScatterPlotItem(pos=np.array(pts).swapaxes(0, 2), color=(
        # np.random.uniform(), np.random.uniform(), np.random.uniform(), np.random.uniform()))
        # self.window3D.addItem(sp2)
        # sp2.scale(4,4,4)
        # self.window3D.addItem(pgl)


        # levels = (-0.08, 0.08)
        # shape = (1, 1, 1)
        # data = pg.gaussia nFilter(np.random.normal(size=shape), (4, 4, 4))
        # data += pg.gaussianFilter(np.random.normal(size=shape), (15, 15, 15)) * 15
        # tex1 = pg.makeRGBA(data[shape[0] // 2], levels=levels)[0]  # yz plane
        logo=QImage("img/logo.jpg")
        ptr = logo.constBits()
        ptr.setsize(logo.byteCount())

        mat = np.array(ptr).reshape(logo.height(), logo.width(), 4)  # 注意这地方通道数一定要填4，否则出错
        logosize = 0.005
        self.logo = gl.GLImageItem(mat)

        self.logo .scale(logosize,logosize,0)
        self.logo .translate(-logo.width()*logosize/2,-logo.height()*logosize/2, -5*logosize*100)

        self.logo2=gl.GLImageItem(mat)
        self.logo2 .scale(logosize,logosize,0)
        self.logo2 .translate(-logo.width()*logosize/2,-logo.height()*logosize/2, 5*logosize*100)


        self.logo3=gl.GLImageItem(mat)
        self.logo3 .scale(logosize,logosize,0)
        self.logo3 .translate(-logo.width()*logosize/2,-logo.height()*logosize/2, 5*logosize*100)
        self.logo3.rotate(90, 0, 1, 0)

        self.logo4=gl.GLImageItem(mat)
        self.logo4 .scale(logosize,logosize,0)
        self.logo4 .translate(-logo.width()*logosize/2,-logo.height()*logosize/2, -5*logosize*100)
        self.logo4.rotate(90, 0, 1, 0)

        self.logo5=gl.GLImageItem(mat)
        self.logo5 .scale(logosize,logosize,0)
        self.logo5 .translate(-logo.width()*logosize/2,-logo.height()*logosize/2, -5*logosize*100)
        self.logo5.rotate(90, 1, 0, 0)

        self.logo6=gl.GLImageItem(mat)
        self.logo6 .scale(logosize,logosize,0)
        self.logo6 .translate(-logo.width()*logosize/2,-logo.height()*logosize/2, 5*logosize*100)
        self.logo6.rotate(90, 1, 0, 0)


        self.window3D.addItem(self.logo )
        self.window3D.addItem(self.logo2)
        self.window3D.addItem(self.logo3)
        self.window3D.addItem(self.logo4)
        self.window3D.addItem(self.logo5)
        self.window3D.addItem(self.logo6)
        self.window3DBoxLayout.addWidget(self.window3D)

    def initListener(this, self):
        self.listener = Listener(self)

    def initSingals(this, self):
        self.signals = Signal(self)

    def figureInit(this, self):
        self.getMCUThread = threading.Thread(target=self.getMCU8050Data)
        # pg.setConfigOption('background',(0,0,0,0))
        # pg.mkColor(0.5)
        self.rollDrawing = pg.PlotWidget()

        self.pitchDrawing = pg.PlotWidget()
        self.yawDrawing = pg.PlotWidget()
        self.Index = 0
        ###############################
        self.rollData = list(np.random.normal(size=100))
        self.curveRoll = self.rollDrawing.plot(self.rollData,pen=(255,0,0))
        self.rollText = pg.TextItem("roll", anchor=(1, 0),color=pg.mkColor(255))
        self.rollText.setParentItem(self.curveRoll)
        self.rollArrow = pg.ArrowItem(angle=90)
        self.rollArrow.setParentItem(self.curveRoll)
############################################################
        self.pitchData = np.random.normal(size=100)
        self.curvePitch = self.pitchDrawing.plot(self.pitchData,pen=(255,0,0))
        #
        self.pitchText = pg.TextItem("pitch", anchor=(1, 0),color=pg.mkColor(255))
        self.pitchText.setParentItem(self.curvePitch)
        self.pitchArrow = pg.ArrowItem(angle=90)
        self.pitchArrow.setParentItem(self.curvePitch)
        ###############################################
        self.yawData = np.random.normal(size=100)
        self.curveYaw = self.yawDrawing.plot(self.yawData,pen=(255,0,0))
        self.yawText = pg.TextItem("yaw", anchor=(1, 0),color=pg.mkColor(255))
        self.yawText.setParentItem(self.curveYaw)
        self.yawArrow = pg.ArrowItem(angle=90)
        self.yawArrow.setParentItem(self.curveYaw)
        #
        self.Timer = QTimer()
        self.Timer.timeout.connect(self.updateText)
        self.Timer.start(10)

        self.rollLayout.addWidget(self.rollDrawing)
        self.pitchLayout.addWidget(self.pitchDrawing)
        self.yawLayout.addWidget(self.yawDrawing)




    def debugTextBrowserInit(this, self):
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

    def initCombox(this, self):
        self.comxCombo.addItems(mySerial.checkPorts())
        self.baudCombo.addItems([str(i) for i in [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
                                                  9600, 19200, 38400, 57600, 115200, 230400, 460800, 500000,
                                                  576000, 921600, 1000000, 1152000, 1500000, 2000000, 2500000,
                                                  3000000, 3500000, 4000000][::-1]])
        self.baudCombo.setCurrentText('500000')
        self.bytesizeCombo.addItems([str(i) for i in [5, 6, 7, 8][::-1]])
        self.parityCombo.addItems(['none', 'even', 'odd', 'mark', 'space'])
        self.stopbitsCombo.addItems(['1', '1.5', '2'])

    def initVar(this, self):
        self.tab = self.tabWidget.currentIndex()
        self.rollAngle = 0
        self.pitchAngle=0
        self.yawAngle=0
        self.autosend = 0
        self.open = False
        self.draw = self.drawCheckBtn.isChecked()
        self.signals.tabChangedSingals()
        self.acceptedData = 2
        self.errorMessageBox = ErrorMessage(self)

    def initButton(this, self):
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

    def initIcon(this, self):
        self.winIcon = QIcon("img/kissing_face_with_closed_eyes_128px_1214135_easyicon.net.ico")

        self.setWindowIcon(self.winIcon)

    def initMain(this, self):
        # self.setCentralWidget(QLabel("SERIAL PORT ASSISTANT"))
        # self.setGeometry(500, 600, 550, 550)

        self.setWindowTitle('SerialPort Assistant By YJC')
