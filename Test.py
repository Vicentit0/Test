#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Escribe tu ip: ")
port = int(input("Escribe tu puerto: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("El puerto esta cerrado")
    else:
        print("El puerto esta abierto")



