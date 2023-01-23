import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 49000))
sock.listen()
print('Server is running...')

while True:
    conn, addr = sock.accept()
    a = conn.recv(1024).decode()
    b = conn.recv(1024).decode()
    a = int(a)
    b = int(b)


    async def multiplication_numbers():
        await asyncio.sleep(2)
        return a * b

    async def sum_numbers():
        await asyncio.sleep(2)
        return a + b

    async def difference_numbers():
        await asyncio.sleep(2)
        return a - b


    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(sum_numbers()),
        ioloop.create_task(difference_numbers()),
        ioloop.create_task(multiplication_numbers())
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    result = f"{a} + {b} = {tasks[0].result()}\n{a} - {b} = {tasks[1].result()}\n{a} * {b} = {tasks[2].result()}"
    conn.send(result.encode())
    conn.close()



