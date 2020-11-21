import threading
from PyQt5.QtCore import QTimer, QPoint
from PyQt5.QtGui import QIcon, QVector3D, QPixmap, QImage, QPainter, QPen, QColor
from PyQt5.QtWidgets import QMainWindow
from mainwindow import Ui_MainWindow  # 加载我们的布局
from pyQtErrorMessage import ErrorMessage
import numpy as np
import mySerial
from pyQtSignal import MainWindowSignal
from pyQtListener import MainWindowListener
import pyqtgraph.opengl as gl
import pyqtgraph as pg
from pyQtAction import MainWindowAction
"""
用于初始化所有的变量
"""


class PyqtMainWindowIntialization(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(PyqtMainWindowIntialization, self).__init__(*args, **kwargs)
        self.setupUi(self)  # 初始化ui
    def initAll(self):

        self.initAction()
        self.initSingals()

        self.initVar()
        self.initCombox()
        self.initButton()
        self.initListener()
        self.initIcon()
        self.initFigure()
        self.init3D()
        self.initMain()
    def init3D(self):
        self.window3D = gl.GLViewWidget()
        self.window3D.opts['distance'] = 10
        self.window3D.opts['azimuth'] = 0
        self.window3D.opts['bgcolor'] = (0.1, 0.1, 0.1, 1)
        # ax.plot_surface(x, y, z, color='b')
        ## create three grids, add each to the view
        self.positiveAxis = gl.GLAxisItem(QVector3D(10, 10, 10), )
        self.positiveAxis.scale(2, 2, 2)
        self.negativeAxis = gl.GLAxisItem(QVector3D(10, 10, 10), )
        self.negativeAxis.scale(2, 2, 2)
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
        logo = QImage("img/logo.jpg")
        ptr = logo.constBits()
        ptr.setsize(logo.byteCount())

        mat = np.array(ptr).reshape(logo.height(), logo.width(), 4)  # 注意这地方通道数一定要填4，否则出错
        logosize = 0.005
        self.logo = gl.GLImageItem(mat)

        self.logo.scale(logosize, logosize, 0)
        self.logo.translate(-logo.width() * logosize / 2, -logo.height() * logosize / 2, -5 * logosize * 100)

        self.logo2 = gl.GLImageItem(mat)
        self.logo2.scale(logosize, logosize, 0)
        self.logo2.translate(-logo.width() * logosize / 2, -logo.height() * logosize / 2, 5 * logosize * 100)

        self.logo3 = gl.GLImageItem(mat)
        self.logo3.scale(logosize, logosize, 0)
        self.logo3.translate(-logo.width() * logosize / 2, -logo.height() * logosize / 2, 5 * logosize * 100)
        self.logo3.rotate(90, 0, 1, 0)

        self.logo4 = gl.GLImageItem(mat)
        self.logo4.scale(logosize, logosize, 0)
        self.logo4.translate(-logo.width() * logosize / 2, -logo.height() * logosize / 2, -5 * logosize * 100)
        self.logo4.rotate(90, 0, 1, 0)

        self.logo5 = gl.GLImageItem(mat)
        self.logo5.scale(logosize, logosize, 0)
        self.logo5.translate(-logo.width() * logosize / 2, -logo.height() * logosize / 2, -5 * logosize * 100)
        self.logo5.rotate(90, 1, 0, 0)

        self.logo6 = gl.GLImageItem(mat)
        self.logo6.scale(logosize, logosize, 0)
        self.logo6.translate(-logo.width() * logosize / 2, -logo.height() * logosize / 2, 5 * logosize * 100)
        self.logo6.rotate(90, 1, 0, 0)

        self.window3D.addItem(self.logo)
        self.window3D.addItem(self.logo2)
        self.window3D.addItem(self.logo3)
        self.window3D.addItem(self.logo4)
        self.window3D.addItem(self.logo5)
        self.window3D.addItem(self.logo6)
        self.window3DBoxLayout.addWidget(self.window3D)
    def initAction(self):
        self.action=MainWindowAction
    def initListener(self):
        self.listener = MainWindowListener()

    def initSingals(self):
        self.signals = MainWindowSignal
    def initLCD(self):
        frames=self.myPort.readLCD()
        self.lcdFigure=QPainter()
        self.lcdFigure.setRenderHint(QPainter.Antialiasing, True);
        #每一行由06隔开
        def list_split(items, n):
            return [items[i:i + n] for i in range(0, len(items), n)]
        for yIndex,yframe in enumerate(list_split(frames,964)):
            yframeLeng=len(yframe)
            while len(yframe)<964:
                yframe+=['00']
            for xIndex in range(2,yframeLeng):
                if xIndex==481:
                    break
                try:
                    low=int(yframe[xIndex],16)
                    high=int(yframe[xIndex+480],16)
                    self.lcdFigure.setPen(QPen(QColor(0,high,low),1))
                    self.lcdFigure.drawPoint(QPoint(xIndex,yIndex))
                except Exception as e:
                    print("不知道咋回事",e,"反正就是好像越界了,看看先",len(frames),xIndex+480)

        self.horizontalLayout_20.addWidget(self.lcdFigure)

    def initFigure(self):
        self.getMCUThread = threading.Thread(target=self.listener.getMCU8050DataListener,args=[self])
        # pg.setConfigOption('background',(0,0,0,0))
        # pg.mkColor(0.5)
        self.rollDrawing = pg.PlotWidget()

        self.pitchDrawing = pg.PlotWidget()
        self.yawDrawing = pg.PlotWidget()
        self.Index = 0

        self.rollData = list(np.random.normal(size=100))
        self.curveRoll = self.rollDrawing.plot(self.rollData, pen=(255, 0, 0))
        self.rollText = pg.TextItem("roll", anchor=(1, 0), color=pg.mkColor(255))
        self.rollText.setParentItem(self.curveRoll)
        self.rollArrow = pg.ArrowItem(angle=90)
        self.rollArrow.setParentItem(self.curveRoll)

        self.pitchData = np.random.normal(size=100)
        self.curvePitch = self.pitchDrawing.plot(self.pitchData, pen=(255, 0, 0))
        #
        self.pitchText = pg.TextItem("pitch", anchor=(1, 0), color=pg.mkColor(255))
        self.pitchText.setParentItem(self.curvePitch)
        self.pitchArrow = pg.ArrowItem(angle=90)
        self.pitchArrow.setParentItem(self.curvePitch)

        self.yawData = np.random.normal(size=100)
        self.curveYaw = self.yawDrawing.plot(self.yawData, pen=(255, 0, 0))
        self.yawText = pg.TextItem("yaw", anchor=(1, 0), color=pg.mkColor(255))
        self.yawText.setParentItem(self.curveYaw)
        self.yawArrow = pg.ArrowItem(angle=90)
        self.yawArrow.setParentItem(self.curveYaw)

        self.Timer = QTimer()
        self.Timer.timeout.connect(lambda :self.action.updateText(self))
        self.Timer.start(10)

        self.rollLayout.addWidget(self.rollDrawing)
        self.pitchLayout.addWidget(self.pitchDrawing)
        self.yawLayout.addWidget(self.yawDrawing)

    def initdebugTextBrowser(self):
        self.debugtextBrowser.setText(self.myPort.getInfo())
        self.debugtextBrowser.textChanged.connect(lambda :self.signals.debugtextBrowerSignals(self))

    def initautoSend(self):
        if self.open:
            interval = self.sendLineEdit_4.text()
            if (not interval.isdigit()):
                self.autoCheckBox.setChecked(0)
                self.errorMessageBox.warning('请不要随意输入字母', '是数字啊')

            else:
                th = threading.Thread(target=self.listener.autoSendListener, args=([self, interval]))
                th.start()

        else:
            self.errorMessageBox.warning('请先打开串口', '打开串口先哦')
            self.autoCheckBox.setChecked(0)

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
        self.tab = self.tabWidget.currentIndex()
        self.rollAngle = 0
        self.pitchAngle = 0
        self.yawAngle = 0
        self.autoSendFlag = 0
        self.open = False
        self.draw = self.drawCheckBtn.isChecked()
        self.signals.tabChangedSingals(self)
        self.acceptedData = self.acceptedcheckBox.isChecked()
        self.errorMessageBox = ErrorMessage(self)

    def initButton(self):
        # self.qbtn = QPushButton('Quit', self)
        # self.qbtn.clicked.connect(QCoreApplication.instance().quit)
        #
        self.initLcdBtn.clicked.connect(self.initLCD)
        self.checkBtn.setStatusTip('Check port')
        self.checkBtn.clicked.connect(lambda :self.signals.freshComboxSignals(self))

        self.openBtn.clicked.connect(lambda :self.action.openMyPortSignals(self))
        self.sendBtn.clicked.connect(lambda :self.action.sendData2MyPort(self))

        self.cleanDebugBtn.clicked.connect(self.debugtextBrowser.clear)
        self.cleanAcceptedBtn.clicked.connect(self.acceptedTextBrowser.clear)
        self.autoCheckBox.stateChanged.connect(self.initautoSend)
        self.aboutBtn.clicked.connect(self.aboutDialog)
        self.tabWidget.currentChanged.connect(lambda :self.signals.tabChangedSingals(self))
        self.textRadioButton_2.clicked.connect(lambda :self.signals.textRadioButtonChangeSingals(self))
        self.hexRadioButton.clicked.connect(lambda :self.signals.textRadioButtonChangeSingals(self))
        self.acceptedcheckBox.stateChanged.connect(lambda :self.signals.acceptedBtnSingals(self))
        self.drawCheckBtn.stateChanged.connect(lambda :self.signals.drawSignals(self))

    def initIcon(self):
        self.winIcon = QIcon("img/kissing_face_with_closed_eyes_128px_1214135_easyicon.net.ico")

        self.setWindowIcon(self.winIcon)

    def initMain(self):
        # self.setCentralWidget(QLabel("SERIAL PORT ASSISTANT"))
        # self.setGeometry(500, 600, 550, 550)

        self.setWindowTitle('SerialPort Assistant By YJC')
