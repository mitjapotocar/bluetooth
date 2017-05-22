import bluetooth
import RPi.GPIO as GPIO        #calling for header file which helps in using GPIOs of PI
 
  
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
  
client_socket,address = server_socket.accept()
print "Accepted connection from ",address
while 1:
  data = client_socket.recv(1024)
  print "Received: %s" % data
  print(data)
  if (data == "Up"):
    print("Up")
    fwd()
  elif (data == "Down"):
    print("Down")
    fwd()
  elif (data == "Left"):
    print("Left")
    fwd()
  elif (data == "Right"):
    print("Right")
    fwd()
  elif (data == "q"):
    print ("Quit")
    break
  else:
    print("Niste napisali nič pametnega!")
  
client_socket.close()
server_socket.close()
