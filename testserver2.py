import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_image(encrypted_image_path, key):
    with open(encrypted_image_path, 'rb') as file:
        encrypted_data = file.read()
    
    cipher = AES.new(key.encode(), AES.MODE_ECB)  # Ensure key is bytes
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    
    with open('decrypted_image.jpg', 'wb') as file:
        file.write(decrypted_data)
    
    print("Hình ảnh đã được giải mã thành công!")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9999
server_socket.bind((host, port))
server_socket.listen(5)
print("Server is listening...")
client_socket, addr = server_socket.accept()

print("Connection from", addr)

# Nhận kích thước file
file_size_data = client_socket.recv(8)  # Giả sử kích thước file không quá lớn để vượt quá 8 byte
file_size = int.from_bytes(file_size_data, 'big')
received_bytes = 0

with open('received_image.jpg', 'wb') as image_file:
    while received_bytes < file_size:
        data = client_socket.recv(1024)
        if not data:
            break  # Dừng nếu không nhận được thêm dữ liệu
        received_bytes += len(data)
        image_file.write(data)

print("File has been received successfully.")

# Đường dẫn của hình ảnh đã được mã hóa và khóa
encrypted_image_path = 'received_image.jpg'
key = "ThisIsA16ByteKey"  # Ensure the key is correctly handled as bytes in the decrypt function

# Giải mã hình ảnh
decrypt_image(encrypted_image_path, key)
