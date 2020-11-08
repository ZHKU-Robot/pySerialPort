from PyQt5.QtWidgets import QMessageBox


class ErrorMessage():
    def __init__(self, qWindow):
        self.qMainWindow = qWindow

    def warning(self, title, content):
        QMessageBox.warning(self.qMainWindow, title, content)



    def QMessageBox(self):
        self.qMainWindow.qmb = QMessageBox()
        self.qMainWindow.qmb.setText("你已经打开了串口啦(* ￣3)(ε￣ *)")
        self.qMainWindow.qmb.setInformativeText("o(>﹏<)o不要再打开了,呜呜呜")
        self.qMainWindow.qmb.setStandardButtons(QMessageBox.Ok)
        self.qMainWindow.qmb.setWindowTitle("(づ￣3￣)づ╭❤～BIUBIU")
        self.qMainWindow.qmb.show()
        pass