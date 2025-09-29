import socket
import tqdm

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen(1)

print("📡 Server listening...")
client, addr = server.accept()
print(f"Connected with {addr}")

# Step 1: Read header (filename and size)
header = b""
while not header.endswith(b"\n"):
    header += client.recv(1)

file_name, file_size = header.decode().strip().split("|")
file_size = int(file_size)

print("Receiving:", file_name)
print("Size:", file_size, "bytes")

# Step 2: Receive file data
progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1024, total=file_size)

received = 0
with open(file_name, "wb") as f:
    while received < file_size:
        data = client.recv(1024)
        if not data:
            break
        f.write(data)
        received += len(data)
        progress.update(len(data))

print("File received successfully!")

client.close()
server.close()
