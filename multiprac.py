import queue
import threading
import time

backlog = queue.Queue(5)
lock = threading.Lock()
FINISHED = False

class MyProcessor(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        while True:
            with lock:
                if not backlog.empty():
                    task = backlog.get()
                    print(self.name, 'working on task:', task)
                else:
                    print('backlog empty')
            time.sleep(1)
            if FINISHED:
                break

threads = list()
for i in range(3):
    p = MyProcessor(i)
    p.start()
    threads.append(p)
    print('thread started.', p.name)


for i in range(10):
    print('added', i)
    with lock:
        if not backlog.full():
            backlog.put(i)
    time.sleep(0.2)

while True:
    with lock:
        if backlog.empty():
            print('finished!')
            FINISHED = True
            break
        else:
            print('not empty')
    time.sleep(1)

print(threading.activeCount(), threading.enumerate())
for t in threads:
    t.join()
print(threading.activeCount(), threading.enumerate())
print("all done!")

