
import time

from PyQt5.QtCore import QThread, pyqtSignal


class Pic(QThread):
    # 使用信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    finishSignal = pyqtSignal(str)

    # 带参数示例
    def __init__(self,figure,data,parent=None):
        super(Pic, self).__init__(parent)
        self.f=figure
        self.data=data
    def run(self):
        '''
        重写
        '''
        self.f.drawRPY(self.data)
        self.finishSignal.emit('update')
        # return
