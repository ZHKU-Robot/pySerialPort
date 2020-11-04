
import mySerial
myPort=mySerial.Port("com9",115200,1)
print(myPort.checkPorts())
myPort.writeData("wdnmd\r\n")
myPort.getWholeData()



