from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Server ready...")

while True:
    connectionSocket, addr = serverSocket.accept()
    
    try:
        message = connectionSocket.recv(1024).decode()
        print(message)

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Kirim HTTP header
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Kirim isi file
        for i in range(len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.close()

    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.close()

serverSocket.close()