import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 49000))
send_message1 = input("Enter a: ")
send_message2 = input("Enter b: ")
sock.send(send_message1.encode())
sock.send(send_message2.encode())
message_result = sock.recv(1024).decode()
print(f"Result: \n{message_result}")
sock.close()