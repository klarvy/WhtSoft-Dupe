import os
import sys
import socket
os.system('cls||clear')
print("WhtSoft codded by Klarvy")
print ("Автор: WhtSoft")
import socket
a = input("Введитe token:")
b = input("Введи хекс для дюпа:")
v = "700A2432356365376166332D353534362D346163372D623062322D6334353066383062356437371213506C6179657252656D6F7465536572766963651A0A736574506C617965724E616D6522241A220A20574854534F46542044555020544F50"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('3.125.105.137', 2222))
sock.send(bytes.fromhex(a))
while 1:
    sock.send(bytes.fromhex(b))
    sock.send(bytes.fromhex(v))
    
    print("УСПЕШНО")
