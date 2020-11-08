from PyQt5.QtWidgets import QDialog, QWidget

from dialog import Ui_AboutRobot


class AboutDialog(Ui_AboutRobot,QDialog,QWidget):
    def __init__(self, parent=None):
        # Here you're passing self as a parent argument to QMainWindow.__init__,
        # so you're trying to set the not yet fully-initialized object as a
        # parent of itself.
        # > You probably want either "super().__init__()" or
        # > "QtWidgets.QMainWindow.__init__(self)" here.
        super(AboutDialog,self).__init__(parent=parent)
        # Ui_AboutRobot.__init__(self)
        self.setupUi(self)  # 初始化ui