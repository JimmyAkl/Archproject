#clientside
import socket
import pickle
import benchmarks

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    benchmarks.dict["NAME"] = socket.gethostname()
    serialized_dict = pickle.dumps(benchmarks.dict)
    s.connect((HOST, PORT))
    s.sendall(serialized_dict)
    data = s.recv(1024)

print('Received', repr(data))
