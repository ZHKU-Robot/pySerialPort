import serial  # 导入模块
import serial.tools.list_ports
import threading
import time
# 返回 成功读入的字节数


class Port:
    def __init__(self, portname: str, bps: int, maxtime: int):
        # 波特率，标准值之一：
        # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
        # 打开串口，并得到串口对象
        if(portname.upper() not in self.checkPorts()):
            raise Exception("cant connect to serial port")
        self.ser = serial.Serial(portname, bps, timeout=maxtime)
        self.encoding='gbk'
        self.decoding='gbk'
        if (self.ser.is_open):
            # 读取数据
            # 详细参数
            print(self.ser)
            print("your serial port had been opened \n whose info will be showed next ..")

            print("your device named",self.ser.name)  # 设备名字
            print("port type is",self.ser.port)  # 读或者写端口
            print('your baud is', self.ser.baudrate)
            print("bytesize is",self.ser.bytesize)  # 字节大小
            print("parity is",self.ser.parity)  # 校验位
            print("stopbits is",self.ser.stopbits)  # 停止位
            print("timeout is",self.ser.timeout)  # 读超时设置
            print("writeTimeout is",self.ser.writeTimeout)  # 写超时
            print("xonxoff is",self.ser.xonxoff)  # 软件流控
            print("rtscts is ",self.ser.rtscts)  # 软件流控
            print("dsrdtr is",self.ser.dsrdtr)  # 硬件流控
            print("interCharTimeout",self.ser.interCharTimeout)  # 字符间隔超时
            print('your serial port is', self.ser.port)

        else:
            raise Exception("serial port error!")

    def __del__(self):
        # 关闭串口
        self.ser.close()  # 关闭串口
        print("serial port closed")
    def checkPorts(self):
        return [sp.device for sp in serial.tools.list_ports.comports()]
    # 读取字节数和方式  默认utf8解码
    def help(self):
        # 打印能使用的方法
        # print(ser.read())#读一个字节
        # print(ser.read(10).decode("utf8"))#读十个字节
        # print(ser.readline().decode("utf8"))#读一行
        # print(ser.readlines())#读取多行，返回列表，必须匹配超时（timeout)使用
        # print(ser.in_waiting)#获取输入缓冲区的剩余字节数
        # print(ser.out_waiting)#获取输出缓冲区的字节数
        print(__doc__)

        print("""
        ser=serial.Serial("/dev/ttyUSB0",9600,timeout=0.5) #使用USB连接串行口
        ser=serial.Serial("/dev/ttyAMA0",9600,timeout=0.5) #使用树莓派的GPIO口连接串行口
        ser=serial.Serial(1,9600,timeout=0.5)#winsows系统使用com1口连接串行口
        ser=serial.Serial("com1",9600,timeout=0.5)#winsows系统使用com1口连接串行口
        ser=serial.Serial("/dev/ttyS1",9600,timeout=0.5)#Linux系统使用com1口连接串行口
        """)
        print("Port对象属性")
        print("""
        name:设备名字
        port：读或者写端口
        baudrate：波特率
        bytesize：字节大小
        parity：校验位
        stopbits：停止位
        timeout：读超时设置
        writeTimeout：写超时
        xonxoff：软件流控
        rtscts：硬件流控
        dsrdtr：硬件流控
        interCharTimeout:字符间隔超时
        """)
        print("常用方法")
        print("""
        ser.isOpen()：查看端口是否被打开。
        ser.open() ：打开端口‘。
        ser.close()：关闭端口。
        ser.read()：从端口读字节数据。默认1个字节。
        ser.read_all():从端口接收全部数据。
        ser.write("hello")：向端口写数据。
        ser.readline()：读一行数据。
        ser.readlines()：读多行数据。
        in_waiting()：返回接收缓存中的字节数。
        flush()：等待所有数据写出。
        flushInput()：丢弃接收缓存中的所有数据。
        flushOutput()：终止当前写操作，并丢弃发送缓存中的数据。
        """)
        print("本类的方法")
        print(self.__dict__)

    def readData(self, num: int, options="text") -> str:
        # 选择16进制或者 10进制
        if options == "hex":
            return self.ser.read(num).hex()
        elif options == "text":
            return self.ser.read(num).decode(self.decoding)
        elif options=='oct':
            return int(self.ser.read(num).hex(),16)
        elif options=="all":
            pass
        else:
            raise Exception("please input right format like hex or text or oct")

    def getWholeData(self, options='text'):
        print("current input buffer size is",self.ser.in_waiting)
        self.wholeData= self.readData(self.ser.in_waiting, options=options)
        print("whole data is")
        print(self.wholeData)
        return self.wholeData

    def writeData(self, string: str) -> int:
        # 返回成功传入的字数
        num = self.ser.write(string.encode(self.encoding))
        print("writed {} bytes!".format(num))
        time.sleep(0.1)
        return num

    # 默认开启线程
    def readDataByThtead(self, options='text', thread=True):
        self.wholeData = ''
        # 循环接收数据，此为死循环，可用线程实现
        if (thread):
            th = threading.Thread(target=self.getWholeData(), name='getWholedata', args=(options, self.decoding))
            th.start()
        else:
            self.getWholeData(options, self.decoding)
