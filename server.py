import socket

HOST = ''
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on http://localhost:{PORT}")

    conn, addr = s.accept()
    with conn:
        request = conn.recv(1024)
        print(request.decode())

        response = b"""HTTP/1.1 200 OK

Hello, World!
"""
        conn.sendall(response)
