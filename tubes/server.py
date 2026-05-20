import socket
import threading

HOST = '0.0.0.0'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server berjalan di port {PORT}")

clients = []
usernames = []


# Kirim pesan ke semua client
def broadcast(message):
    for client in clients:
        client.send(message)


# Handle tiap client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            broadcast(message)

        except:
            index = clients.index(client)

            clients.remove(client)
            client.close()

            username = usernames[index]
            usernames.remove(username)

            print(f"{username} keluar")

            break


# Terima koneksi client
def receive():
    while True:
        client, address = server.accept()

        print(f"Terhubung dengan {address}")

        # Minta username
        client.send("USERNAME".encode())

        username = client.recv(1024).decode()

        usernames.append(username)
        clients.append(client)

        print(f"Username client: {username}")

        broadcast(f"{username} bergabung ke chat".encode())

        client.send("Berhasil terhubung ke server".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


receive()