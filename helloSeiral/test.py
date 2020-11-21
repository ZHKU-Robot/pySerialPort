import mySerial

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

ser=mySerial.Port('com10',1500000)
ser.readLCD()
mySerial.Port.decodeLcd()
# ser.readDataByThtead('hex')

with open('decoded.txt','r') as f:
    file=f.read()
frames = [file[i:i+2] for i in range(0,len(file),2)]

framsLeng=len(frames)
print(framsLeng)
WIDTHLINE=20

# print([frames[j:j+800] for j in range(0,framesLeng,800)])
class Drawing(QWidget):
    def __init__(self,parent=None):
        super(Drawing,self).__init__(parent)
        self.resize(800,480)
        self.setWindowTitle('在窗口画点')
    def initLCD(self,qp):
        yIndex=0
        temp = ''
        for yframe in  (frames[j:j+960] for j in range(0,framsLeng,960)):
            if len(yframe)==960:
                for xIndex in range(960):
                    if xIndex==480:
                        break

                    high=int(yframe[xIndex],16)
                    low=int(yframe[xIndex+480],16)
                    highbin = bin(high)[2:]
                    lowbin = bin(low)[2:]
                    while len(lowbin)!=8:
                        lowbin='0'+lowbin
                    while len(highbin)!=8:
                        highbin='0'+highbin
                    #     如果上一个画笔的颜色和下一个不同时,再设置画笔,否则
                    #
                    # print(temp,'1')
                    if highbin+lowbin!=temp:
                        # print(temp)
                        # print(int(highbin[:5], 2), int(highbin[5:] + lowbin[:3], 2), int(lowbin[3:], 2))
                        # print(temp,2)
                        # print(int(highbin[:5], 2), int(highbin[5:] + lowbin[2:], 2), int(lowbin[2:], 2))
                        qp.setPen(QPen(QColor(int(highbin[:5], 2), int(highbin[5:] + lowbin[:3], 2), int(lowbin[3:], 2))))
                        temp = highbin + lowbin
                    else:
                        pass
                    qp.drawPoint(QPoint(xIndex,yIndex))
            yIndex+=1
    def paintEvent(self,event):
        #初始化绘图工具
        qp=QPainter()
        qp.setRenderHint(QPainter.Antialiasing, True);
        #开始在窗口绘制
        qp.begin(self)
        #自定义画点方法
        self.initLCD(qp)
        #结束在窗口的绘制
        qp.end()


app=QApplication(sys.argv)
demo=Drawing()
demo.show()
sys.exit(app.exec_())
