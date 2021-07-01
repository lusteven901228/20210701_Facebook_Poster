import json
from multiprocessing import Process, Queue
from upload_files import upload
q = Queue()
def worker():
    while not q.empty():
        upload(q.get())
if __name__ == '__main__':  
    print('execute value: range(start, end)')
    x = int(input('start(yy-%%%):'))
    y = int(input('end(yy-%%%):'))
    for i in range(x,y):
        q.put(x)
    p = []
    for i in range(16):
        p.append(Process(target=worker()))
        p[i].start()
    for i in range(16):
        p[i].join()
