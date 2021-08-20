import bluetooth

bd_addr = "E0:B5:5F:F1:A7:96"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()