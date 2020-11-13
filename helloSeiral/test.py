import mySerial
ser=mySerial.Port('com9',115200)
ser.writeData('AT+RST')
print(ser.readline())
# print(ser.decodeMPU6050(ser.readline('hex')))
    # time.sleep(1)