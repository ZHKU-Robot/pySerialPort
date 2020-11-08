import mySerial
import time
ser=mySerial.Port('com9',500000)

print(ser.decodeMPU6050(ser.readline('hex')))
    # time.sleep(1)