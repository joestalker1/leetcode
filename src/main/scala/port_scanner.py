#!/usr/bin/python3
import socket

ip = input("Input IP:")

# ports = []
# count = 0

# while count < 10:
#     ports.append(int(input("Input port: ")))
#     count += 1


for port in range(1, 1024):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port)) #conecta e traz a msg de erro
#Like connect(address), but return an error indicator instead of raising an exception for errors
    if code == 0: #0 = Success
        print (str(port) + " -> Port exists")

print ("Scan finished")