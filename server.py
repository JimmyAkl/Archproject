import socket
import pickle
import CreateDB
import sqlite3
from sqlite3 import Error
import benchmarks

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432            # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print ('Connected by', addr)
    data = conn.recv(1024)
    times = pickle.loads(data)
    print(times)
    conn.close()

#connection to db
try:
    connDB = sqlite3.connect(r"benchmarks.db")
except Error as e:
    print(e)


cur = connDB.cursor()

#adding reference if it doesnt exist
try:
    cur.execute("SELECT * FROM benchmarks")

except:
    benchmarks.dict["NAME"] = socket.gethostname()
    CreateDB.insert(benchmarks.dict, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

cur.execute("SELECT * FROM benchmarks")
rows = cur.fetchall()

#fetching reference row
reference=rows[0]
#calculating spec for latest test
spec={}
spec["Astar"]=reference[2]/times["Astar"]
spec["remove_duplicates"]=reference[4]/times["remove_duplicates"]
spec["bubbleSort"]=reference[6]/times["bubbleSort"]
spec["insertionSort"]=reference[8]/times["insertionSort"]
spec["selectionSort"]=reference[10]/times["selectionSort"]
spec["quickSort"]=reference[12]/times["quickSort"]
spec["merge"]=reference[14]/times["merge"]
spec["heapSort"]=reference[16]/times["heapSort"]
spec["huff"]=reference[18]/times["huff"]
spec["queen"]=reference[20]/times["queen"]

#calculating geometric mean
geometricMean=1
for test in spec.keys():
    geometricMean=geometricMean*spec[test]

geometricMean=geometricMean**(1/len(spec.keys()))

print(" gemoteric mean " ,geometricMean)

# inserting new test
CreateDB.insert(times, spec["Astar"], spec["remove_duplicates"], spec["bubbleSort"], spec["insertionSort"], spec["selectionSort"], spec["quickSort"], spec["merge"], spec["heapSort"], spec["huff"], spec["queen"], geometricMean)


#all tests
cur.execute("SELECT * FROM benchmarks")
rows = cur.fetchall()
print(rows)
