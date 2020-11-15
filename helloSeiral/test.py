import mySerial
ser=mySerial.Port('com10',500000)
# ser.writeData('atk_8266_send_cmd("AT+CWSAP?","OK",20)')
# print(ser.readline())
print(ser.readDataByThtead(options='hex'))
    # time.sleep(1)