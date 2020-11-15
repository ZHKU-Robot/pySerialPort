import os
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from AboutDiaglog import AboutDialog
from pyQTInit import PyqtMainWindowIntialization
import qdarkstyle
from PyQt5.QtCore import Qt
class MainWindow(PyqtMainWindowIntialization):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        PyqtMainWindowIntialization.__init__(self)
        self.initAll()
        # self.setWindowFlag(Qt.FramelessWindowHint )
        # self.setWindowFlag(Qt.WindowCloseButtonHint )
    def aboutDialog(self):
        about = AboutDialog()
        about.setWindowIcon(self.winIcon)
        about.setWindowTitle('关于 CC 关于 robot 关于 兴爷')
        about.setModal(1)
        about.exec_()

    # debugtextBrower--------------------------------------

    def closeEvent(self, a0) -> None:
        self.autoSendFlag = 0
        if getattr(self, 'myPort', 1) == 1:
            pass
        else:
            self.myPort.ser.close()
        self.open = 0
        self.draw = 0
        for i in range(100,0,-1):
            self.setWindowOpacity(i/100)
            time.sleep(0.002)

if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)

    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    app.setStyleSheet(dark_stylesheet)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())
