import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Masukkan username: ")


# Menerima pesan dari server
def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "USERNAME":
                client.send(username.encode())

            else:
                print(message)

        except:
            print("Terputus dari server")
            client.close()
            break


# Mengirim pesan ke server
def write():
    while True:
        message = input("")

        full_message = f"{username}: {message}"

        client.send(full_message.encode())


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()