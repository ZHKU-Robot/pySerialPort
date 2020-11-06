# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1165, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.portInitGroupLayout = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.portInitGroupLayout.setFont(font)
        self.portInitGroupLayout.setFlat(True)
        self.portInitGroupLayout.setObjectName("portInitGroupLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.portInitGroupLayout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comxLabel = QtWidgets.QLabel(self.portInitGroupLayout)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.comxLabel.setFont(font)
        self.comxLabel.setObjectName("comxLabel")
        self.verticalLayout.addWidget(self.comxLabel)
        self.comxCombo = QtWidgets.QComboBox(self.portInitGroupLayout)
        self.comxCombo.setEditable(True)
        self.comxCombo.setObjectName("comxCombo")
        self.verticalLayout.addWidget(self.comxCombo)
        self.baudLabel = QtWidgets.QLabel(self.portInitGroupLayout)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.baudLabel.setFont(font)
        self.baudLabel.setObjectName("baudLabel")
        self.verticalLayout.addWidget(self.baudLabel)
        self.baudCombo = QtWidgets.QComboBox(self.portInitGroupLayout)
        self.baudCombo.setEditable(True)
        self.baudCombo.setObjectName("baudCombo")
        self.verticalLayout.addWidget(self.baudCombo)
        self.comxTimeout = QtWidgets.QLabel(self.portInitGroupLayout)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comxTimeout.setFont(font)
        self.comxTimeout.setObjectName("comxTimeout")
        self.verticalLayout.addWidget(self.comxTimeout)
        self.timeoutSpinBox = QtWidgets.QSpinBox(self.portInitGroupLayout)
        self.timeoutSpinBox.setObjectName("timeoutSpinBox")
        self.verticalLayout.addWidget(self.timeoutSpinBox)
        self.bytesizeLabel = QtWidgets.QLabel(self.portInitGroupLayout)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.bytesizeLabel.setFont(font)
        self.bytesizeLabel.setObjectName("bytesizeLabel")
        self.verticalLayout.addWidget(self.bytesizeLabel)
        self.bytesizeCombo = QtWidgets.QComboBox(self.portInitGroupLayout)
        self.bytesizeCombo.setEditable(True)
        self.bytesizeCombo.setObjectName("bytesizeCombo")
        self.verticalLayout.addWidget(self.bytesizeCombo)
        self.prrityLabel = QtWidgets.QLabel(self.portInitGroupLayout)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.prrityLabel.setFont(font)
        self.prrityLabel.setObjectName("prrityLabel")
        self.verticalLayout.addWidget(self.prrityLabel)
        self.parityCombo = QtWidgets.QComboBox(self.portInitGroupLayout)
        self.parityCombo.setEditable(True)
        self.parityCombo.setObjectName("parityCombo")
        self.verticalLayout.addWidget(self.parityCombo)
        self.stopbitLabel = QtWidgets.QLabel(self.portInitGroupLayout)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.stopbitLabel.setFont(font)
        self.stopbitLabel.setObjectName("stopbitLabel")
        self.verticalLayout.addWidget(self.stopbitLabel)
        self.stopbitsCombo = QtWidgets.QComboBox(self.portInitGroupLayout)
        self.stopbitsCombo.setEditable(True)
        self.stopbitsCombo.setIconSize(QtCore.QSize(16, 16))
        self.stopbitsCombo.setDuplicatesEnabled(False)
        self.stopbitsCombo.setObjectName("stopbitsCombo")
        self.verticalLayout.addWidget(self.stopbitsCombo)
        self.openBtn = QtWidgets.QPushButton(self.portInitGroupLayout)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.openBtn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/open_sign_128px_1291563_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openBtn.setIcon(icon)
        self.openBtn.setIconSize(QtCore.QSize(32, 32))
        self.openBtn.setFlat(True)
        self.openBtn.setObjectName("openBtn")
        self.verticalLayout.addWidget(self.openBtn)
        self.closebtn = QtWidgets.QPushButton(self.portInitGroupLayout)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.closebtn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/closed_sign_128px_1291564_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closebtn.setIcon(icon1)
        self.closebtn.setIconSize(QtCore.QSize(32, 32))
        self.closebtn.setFlat(True)
        self.closebtn.setObjectName("closebtn")
        self.verticalLayout.addWidget(self.closebtn)
        self.checkBtn = QtWidgets.QPushButton(self.portInitGroupLayout)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.checkBtn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/check_list_128px_1233674_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBtn.setIcon(icon2)
        self.checkBtn.setIconSize(QtCore.QSize(32, 32))
        self.checkBtn.setFlat(True)
        self.checkBtn.setObjectName("checkBtn")
        self.verticalLayout.addWidget(self.checkBtn)
        self.aboutBtn = QtWidgets.QPushButton(self.portInitGroupLayout)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.aboutBtn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/talking_about_love_128px_1094170_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutBtn.setIcon(icon3)
        self.aboutBtn.setIconSize(QtCore.QSize(32, 32))
        self.aboutBtn.setFlat(True)
        self.aboutBtn.setObjectName("aboutBtn")
        self.verticalLayout.addWidget(self.aboutBtn)
        self.horizontalLayout.addWidget(self.portInitGroupLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 1011, 681))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget_4)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.statisticGroupLayout = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.statisticGroupLayout.setFont(font)
        self.statisticGroupLayout.setObjectName("statisticGroupLayout")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.statisticGroupLayout)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 60, 240, 25))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sendedtext = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.sendedtext.setFont(font)
        self.sendedtext.setObjectName("sendedtext")
        self.horizontalLayout_4.addWidget(self.sendedtext)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_3)
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber_2.setDigitCount(5)
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_4.addWidget(self.lcdNumber_2)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 1)
        self.debuggroupBox = QtWidgets.QGroupBox(self.statisticGroupLayout)
        self.debuggroupBox.setGeometry(QtCore.QRect(0, 90, 251, 591))
        self.debuggroupBox.setObjectName("debuggroupBox")
        self.debugtextBrowser = QtWidgets.QTextBrowser(self.debuggroupBox)
        self.debugtextBrowser.setGeometry(QtCore.QRect(10, 30, 231, 501))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.debugtextBrowser.setFont(font)
        self.debugtextBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.debugtextBrowser.setObjectName("debugtextBrowser")
        self.cleanDebugBtn = QtWidgets.QPushButton(self.debuggroupBox)
        self.cleanDebugBtn.setGeometry(QtCore.QRect(64, 540, 121, 41))
        self.cleanDebugBtn.setAutoFillBackground(False)
        self.cleanDebugBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/cleaning_128px_1293153_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cleanDebugBtn.setIcon(icon4)
        self.cleanDebugBtn.setIconSize(QtCore.QSize(48, 48))
        self.cleanDebugBtn.setCheckable(False)
        self.cleanDebugBtn.setAutoRepeat(False)
        self.cleanDebugBtn.setAutoExclusive(False)
        self.cleanDebugBtn.setAutoDefault(False)
        self.cleanDebugBtn.setDefault(False)
        self.cleanDebugBtn.setFlat(True)
        self.cleanDebugBtn.setObjectName("cleanDebugBtn")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.statisticGroupLayout)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 28, 240, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.acceptedtext = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.acceptedtext.setFont(font)
        self.acceptedtext.setObjectName("acceptedtext")
        self.horizontalLayout_3.addWidget(self.acceptedtext)
        self.lcdNumber = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_2)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_3.addWidget(self.lcdNumber)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_2.addWidget(self.statisticGroupLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.acceptedGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.acceptedGroupBox.setFont(font)
        self.acceptedGroupBox.setFlat(True)
        self.acceptedGroupBox.setObjectName("acceptedGroupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.acceptedGroupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 281, 711, 42))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.hexRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.hexRadioButton.setCheckable(True)
        self.hexRadioButton.setAutoRepeat(True)
        self.hexRadioButton.setAutoExclusive(True)
        self.hexRadioButton.setObjectName("hexRadioButton")
        self.horizontalLayout_5.addWidget(self.hexRadioButton)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.textRadioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.textRadioButton_2.setChecked(True)
        self.textRadioButton_2.setAutoExclusive(True)
        self.textRadioButton_2.setObjectName("textRadioButton_2")
        self.horizontalLayout_5.addWidget(self.textRadioButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.octRadioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.octRadioButton_3.setChecked(False)
        self.octRadioButton_3.setAutoRepeat(False)
        self.octRadioButton_3.setAutoExclusive(True)
        self.octRadioButton_3.setObjectName("octRadioButton_3")
        self.horizontalLayout_5.addWidget(self.octRadioButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.cleanAcceptedBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cleanAcceptedBtn.setText("")
        self.cleanAcceptedBtn.setIcon(icon4)
        self.cleanAcceptedBtn.setIconSize(QtCore.QSize(32, 32))
        self.cleanAcceptedBtn.setFlat(True)
        self.cleanAcceptedBtn.setObjectName("cleanAcceptedBtn")
        self.horizontalLayout_5.addWidget(self.cleanAcceptedBtn)
        self.acceptedTextBrowser = QtWidgets.QTextBrowser(self.acceptedGroupBox)
        self.acceptedTextBrowser.setGeometry(QtCore.QRect(20, 30, 711, 241))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.acceptedTextBrowser.setFont(font)
        self.acceptedTextBrowser.setAutoFillBackground(False)
        self.acceptedTextBrowser.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.acceptedTextBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.acceptedTextBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.acceptedTextBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.acceptedTextBrowser.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.acceptedTextBrowser.setUndoRedoEnabled(False)
        self.acceptedTextBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.acceptedTextBrowser.setObjectName("acceptedTextBrowser")
        self.verticalLayout_5.addWidget(self.acceptedGroupBox)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.sendedGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.sendedGroupBox.setFont(font)
        self.sendedGroupBox.setFlat(True)
        self.sendedGroupBox.setCheckable(False)
        self.sendedGroupBox.setObjectName("sendedGroupBox")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.sendedGroupBox)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(16, 36, 721, 281))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sendedRegion = QtWidgets.QTextEdit(self.verticalLayoutWidget_6)
        self.sendedRegion.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.sendedRegion.setObjectName("sendedRegion")
        self.verticalLayout_3.addWidget(self.sendedRegion)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.autoCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_6)
        self.autoCheckBox.setChecked(False)
        self.autoCheckBox.setTristate(False)
        self.autoCheckBox.setObjectName("autoCheckBox")
        self.horizontalLayout_11.addWidget(self.autoCheckBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.sendLineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.sendLineEdit_4.setObjectName("sendLineEdit_4")
        self.horizontalLayout_11.addWidget(self.sendLineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.sendBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/send_128px_1291717_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendBtn.setIcon(icon5)
        self.sendBtn.setIconSize(QtCore.QSize(32, 32))
        self.sendBtn.setFlat(True)
        self.sendBtn.setObjectName("sendBtn")
        self.horizontalLayout_11.addWidget(self.sendBtn)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(2, 5)
        self.horizontalLayout_11.setStretch(3, 1)
        self.horizontalLayout_11.setStretch(4, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.verticalLayout_3.setStretch(1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.sendedGroupBox)
        self.lineEdit.setGeometry(QtCore.QRect(12, 403, 184, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.sendedGroupBox)
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.setStretch(0, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(-1, -1, 1021, 681))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget_4)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_11.addWidget(self.graphicsView)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.verticalLayoutWidget_4)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_11.addWidget(self.graphicsView_2)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.verticalLayoutWidget_4)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_11.addWidget(self.graphicsView_3)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.portInitGroupLayout.setTitle(_translate("MainWindow", "CcBeta0.1"))
        self.comxLabel.setText(_translate("MainWindow", "串口号"))
        self.baudLabel.setText(_translate("MainWindow", "波特率"))
        self.comxTimeout.setText(_translate("MainWindow", "超时时间"))
        self.bytesizeLabel.setText(_translate("MainWindow", "字节位"))
        self.prrityLabel.setText(_translate("MainWindow", "检验位"))
        self.stopbitLabel.setText(_translate("MainWindow", "停止位"))
        self.openBtn.setText(_translate("MainWindow", "打开串口"))
        self.closebtn.setText(_translate("MainWindow", "关闭串口"))
        self.checkBtn.setText(_translate("MainWindow", "检查串口"))
        self.aboutBtn.setText(_translate("MainWindow", "关于聪聪"))
        self.statisticGroupLayout.setTitle(_translate("MainWindow", "Statistics"))
        self.sendedtext.setText(_translate("MainWindow", "Sended"))
        self.debuggroupBox.setTitle(_translate("MainWindow", "Debug"))
        self.debugtextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">DEBUG HERE</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p></body></html>"))
        self.acceptedtext.setText(_translate("MainWindow", "Accepted"))
        self.acceptedGroupBox.setTitle(_translate("MainWindow", "接收区"))
        self.hexRadioButton.setText(_translate("MainWindow", "HEX"))
        self.textRadioButton_2.setText(_translate("MainWindow", "TEXT"))
        self.octRadioButton_3.setText(_translate("MainWindow", "OCT"))
        self.acceptedTextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sendedGroupBox.setTitle(_translate("MainWindow", "发送区"))
        self.autoCheckBox.setText(_translate("MainWindow", "自动"))
        self.sendLineEdit_4.setText(_translate("MainWindow", "1000"))
        self.label_5.setText(_translate("MainWindow", "ms/次"))
        self.sendBtn.setText(_translate("MainWindow", "冲"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "发射和接收爱心射线(づ￣3￣)づ╭❤～"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))

