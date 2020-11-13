import serial  # 导入模块
import serial.tools.list_ports
import threading
import time


# 返回 成功读入的字节数

def checkPorts():
    return [sp.device for sp in serial.tools.list_ports.comports()]


class Port:
    def __init__(self, portname='com9', bps=115200, maxtime=1, bytesize=8, parity='none', stopbits=1):
        # 波特率，标准值之一：
        # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
        # 打开串口，并得到串口对象

        self.ser = serial.Serial(portname, bps, timeout=maxtime,
                                 bytesize={5: serial.FIVEBITS, 6: serial.SIXBITS, 7: serial.SEVENBITS,
                                           8: serial.EIGHTBITS}[bytesize], parity=
                                 {'none': serial.PARITY_NONE, 'even': serial.PARITY_EVEN, 'odd': serial.PARITY_ODD,
                                  'mark': serial.PARITY_MARK, 'space': serial.PARITY_SPACE}[parity], stopbits=
                                 {1: serial.STOPBITS_ONE, 1.5: serial.STOPBITS_ONE_POINT_FIVE, 2: serial.STOPBITS_TWO}[
                                     stopbits])
        self.encoding = 'gbk'
        self.decoding = 'gbk'
        if (self.ser.is_open):
            # 读取数据
            # 详细参数
            print(self.ser)
            print("your serial port had been opened  whose info will be showed next ..")

            print("your device named", self.ser.name)  # 设备名字
            print("port type is", self.ser.port)  # 读或者写端口
            print('your baud is', self.ser.baudrate)
            print("bytesize is", self.ser.bytesize)  # 字节大小
            print("parity is", self.ser.parity)  # 校验位
            print("stopbits is", self.ser.stopbits)  # 停止位
            print("timeout is", self.ser.timeout)  # 读超时设置
            print("writeTimeout is", self.ser.writeTimeout)  # 写超时
            print("xonxoff is", self.ser.xonxoff)  # 软件流控
            print("rtscts is ", self.ser.rtscts)  # 软件流控
            print("dsrdtr is", self.ser.dsrdtr)  # 硬件流控
            print("interCharTimeout", self.ser.interCharTimeout)  # 字符间隔超时
            print('your serial port is', self.ser.port)

        else:
            raise Exception("serial port error!")


    # 读取字节数和方式  默认utf8解码
    def getInfo(self):
        return f"""your serial port had been opened  whose info will be showed next .." \n
                "your device named", {self.ser.name} \n
               "port type is", {self.ser.port}\n
               'your baud is', {self.ser.baudrate}\n
               "bytesize is", {self.ser.bytesize}\n
               "parity is", {self.ser.parity}\n
               "stopbits is", {self.ser.stopbits}\n
               "timeout is", {self.ser.timeout}\n
               "writeTimeout is", {self.ser.writeTimeout}\n
               "xonxoff is", {self.ser.xonxoff}\n
               "rtscts is ", {self.ser.rtscts}\n
               "interCharTimeout", {self.ser.interCharTimeout}\n
               'your serial port is', {self.ser.port}"""








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

    def decodeMPU6050(self, frames):
        #     //传送数据给匿名四轴上位机软件(V2.6版本)
        # //fun:功能字. 0XA0~0XAF
        # //data:数据缓存区,最多28字节!!
        # //len:data区有效数据个数
        # void usart1_niming_report(u8 fun,u8*data,u8 len)
        # {
        # 	u8 send_buf[32];
        # 	u8 i;
        # 	if(len>28)return;	//最多28字节数据
        # 	send_buf[len+3]=0;	//校验数置零
        # 	send_buf[0]=0X88;	//帧头
        # 	send_buf[1]=fun;	//功能字
        # 	send_buf[2]=len;	//数据长度
        # 	for(i=0;i<len;i++)send_buf[3+i]=data[i];			//复制数据
        # 	for(i=0;i<len+3;i++)send_buf[len+3]+=send_buf[i];	//计算校验和
        # 	for(i=0;i<len+4;i++)usart1_send_char(send_buf[i]);	//发送数据到串口1
        # }
        # void usart1_report_imu(short aacx,short aacy,short aacz,short gyrox,short gyroy,short gyroz,short roll,short pitch,short yaw)
        # {
        # 	u8 tbuf[28];
        # 	u8 i;
        # 	for(i=0;i<28;i++)tbuf[i]=0;//清0
        # 	tbuf[0]=(aacx>>8)&0XFF;
        # 	tbuf[1]=aacx&0XFF;
        # 	tbuf[2]=(aacy>>8)&0XFF;
        # 	tbuf[3]=aacy&0XFF;
        # 	tbuf[4]=(aacz>>8)&0XFF;
        # 	tbuf[5]=aacz&0XFF;
        # 	tbuf[6]=(gyrox>>8)&0XFF;
        # 	tbuf[7]=gyrox&0XFF;
        # 	tbuf[8]=(gyroy>>8)&0XFF;
        # 	tbuf[9]=gyroy&0XFF;
        # 	tbuf[10]=(gyroz>>8)&0XFF;
        # 	tbuf[11]=gyroz&0XFF;
        # 	tbuf[18]=(roll>>8)&0XFF;
        # 	tbuf[19]=roll&0XFF;
        # 	tbuf[20]=(pitch>>8)&0XFF;
        # 	tbuf[21]=pitch&0XFF;
        # 	tbuf[22]=(yaw>>8)&0XFF;
        # 	tbuf[23]=yaw&0XFF;
        # 	usart1_niming_report(0XAF,tbuf,28);//飞控显示帧,0XAF
        # }
        # 将传来的16进制数组数据解码
        # 0~2 是帧头,功能字,数据长度
        # 31是校验和
        # 3到30是数据,刚好0~27 28个数据, 现在只有24个数据被使用,剩余的是0
        #frame是32的倍数
        #如果不是88则丢弃
        # print(frames)
        if frames!=[]:
            try:
                find=frames.index('88')
            except Exception as e:
                return e

            frames=frames[find:find+32]
            frameLeng=32
            framesNum=int(len(frames)/frameLeng)

            frameList=[[bin(int('0x'+j,16)) for j in frames[i*32:i*32+32]] for i in range(framesNum)][:frameLeng]
            # mpudata=[]
            flag= bin(int('0xaf',16))

            for frame in frameList:
                # print(frame[21:27])
                if (frame[1] ==flag):  # 对应usart1_report_imu
                    #计算检验位
                    checksum = int(frame[31],2)
                    data=sum([int(i,2) for i in frame[:31]])
                    if data% 256 == checksum:
                        rpy=[]
                        for i in range(21, 27, 2):
                            sign=1
                            low=frame[i+1][2:]
                            high=frame[i][2:]

                            while(len(low)<8):
                                low='0'+low
                            # print(f"如今的high={high} low={low} ")
                            if(high[0]=='1' and len(high)==8):
                                hlist=list(high)
                                llist=list(low)
                                sign=-1
                                for h in range(len(high)):
                                    if(high[h]=='1'):
                                        hlist[h]='0'
                                    else:
                                        hlist[h]='1'
                                for l in range(len(low)):
                                    if(llist[l]=='1'):
                                        llist[l]='0'
                                    else:
                                        llist[l]='1'
                                high=''.join(hlist)
                                low=''.join(llist)
                            # print(f"现在的high={high},low={low} 即{high+low}")
                            # print('十进制为',int(high+low,2)*sign)
                            rpy.append(int(high+low,2)*sign)

                            # rpy.append(result)
                            # rpy.append(int(high+low,2))
                        roll=rpy[0]/100
                        pitch=rpy[1]/100
                        yaw=rpy[2]/10
                        return [roll,pitch,yaw]
                    # 检验和
                    # checksum = frame[31]
                    # # 检验
                    # if sum(data)%256==checksum:
                    #     # 高位aacx
                    #     aacx=frame[3]*16+frame[4]
                    #     aacy=frame[5]*16+frame[6]
                    #     aacz=frame[7]*16+frame[8]
                    #     gyrox=frame[9]*16+frame[10]
                    #     gyroy= frame[11] * 16 + frame[12]
                    #     gyroz = frame[13] * 16 + frame[14]
                    #     # +7
                    #
                    #     print([aacx,aacy,aacz,gyrox,gyroy,gyroz,roll,pitch,yaw])
                    #     print(frame[23],frame[24])
                    #     print(roll,pitch,yaw)
                    #     # mpudata.append([aacx,aacy,aacz,gyrox,gyroy,gyroz,roll,pitch,yaw])


                else:
                    pass
            # return mpudata
            pass
    def readline(self, options="text"):
        if(self.ser.is_open):
            if options == "hex":
                s=self.ser.readline().hex()

                return [s[i:i+2] for i in range(0,len(s),2)]
            elif options == "text":
                try:
                    return self.ser.readline().decode(self.decoding)
                except Exception as e:
                    return e

            elif options == "all":
                pass
            else:
                raise Exception("please input right format like hex or text but no",options)
        else:
            return Exception("串口已关闭,你在读nm呢")
    def readData(self, num: int, options="text") -> str:
        # 选择16进制或者 10进制
        if(self.ser.is_open):
            if options == "hex":
                s=self.ser.read(num).hex()
                return [s[i:i+2] for i in range(0,len(s),2)]
            elif options == "text":
                try:
                    return self.ser.read(num).decode(self.decoding)
                except Exception as e:
                    return e

            elif options == "all":
                pass
            else:
                raise Exception("please input right format like hex or text but no",options)
        else:
            return Exception("串口已关闭,你在读nm呢")

    def getWholeData(self, options='text'):
        if(self.ser.is_open):
            time.sleep(0.1)
            try:
                # print(self.ser.in_waiting)
                self.wholeData = self.readData(self.ser.in_waiting, options=options)
            except:
                Exception("串口已关闭,你在读nm呢")
            # print(self.wholeData)
            return self.wholeData
        else:
            return Exception("串口已关闭,你在读nm呢")
    def hangThread2ReadData(self,options):
        #priont("-------- start hanging to read data -------- ")
        while(self.hang):
            self.getWholeData(options)




    def writeData(self, string: str) -> int:
        # 返回成功传入的字数
        num = self.ser.write(string.encode(self.encoding))
        #priont("writed {} bytes!".format(num))
        return num

    # 默认开启线程
    def readDataByThtead(self, options='text', thread=True):
        self.wholeData = ''
        self.hang=1
        # 循环接收数据，此为死循环，可用线程实现
        if (thread):
            th = threading.Thread(target=self.hangThread2ReadData, name='getWholedata', args=([options]))
            th.start()
        else:
            self.getWholeData(options)
