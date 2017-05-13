from gopigo import *
import bluetooth

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()


data = client_sock.recv(1024)
print(data)
'''while True:
    try:
        if data == "UP":
            fwd()
            break
        elif data == "UP_RIGHT":
            right()
            break
        elif data == "RIGHT":
            right()
            break
        elif data == "DOWN_RIGHT":
            right()
            break
        elif data == "DOWN":
            bwd()
            break
        elif data == "DOWN_LEFT":
            left()
            break
        elif data == "LEFT":
            left()
            break
        elif data == "UP_LEFT":
            left()
            break
        elif data == "CENTER":
            stop()
            break
        else:
            stop()
            break
    except ValueError:
        print("Prišlo je do napake!")
        break'''
        
        

client_sock.close()
server_sock.close()
