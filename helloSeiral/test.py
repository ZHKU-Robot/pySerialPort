import mySerial
import time
ser=mySerial.Port('com9',500000)
f=[1,2,3]

while 1:
    ser.decodeMPU6050(ser.readline('hex'))
    # time.sleep(1)