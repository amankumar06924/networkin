import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))

file_path = "file transfer/download.jpeg"
file_size = os.path.getsize(file_path)

# Send header: "filename|size\n"
header = f"received_image.png|{file_size}\n"
client.send(header.encode())

# Send file content
with open(file_path, "rb") as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        client.sendall(data)

print("File sent successfully!")

client.close()
