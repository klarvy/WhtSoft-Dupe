import os
import sys
import socket
os.system('cls||clear')
print("WhtSoft codded by Klarvy")
print ("Автор: WhtSoft")
a = input("Введитe token:")
b = input("Введи хекс для дюпа:")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('3.125.105.137', 2222))
sock.send(bytes.fromhex(a))
while 1:
    sock.send(bytes.fromhex(b))
    
    print("УСПЕШНО")
