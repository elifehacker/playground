import threading
import queue
import time

thread_names = ["t1","t2","t3"]
task_strs = ['job1','job2','job3','job4','j5','j6','j7']

lock = threading.Lock()
todos = queue.Queue(5)

class Processor(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        while exitflag != 1:
            with lock:
                if not todos.empty():
                    data = todos.get()
                    print('working on it!', self.name, data)
                    print('data', data)
            #lock.release()
            time.sleep(1)

threads = []
exitflag = 0

for p in thread_names:
    print('thread name', p)
    t = Processor(p)
    threads.append(t)
    t.start()
    
print('threads', threads)
print(threading.activeCount(), threading.enumerate())

for t in task_strs:
    print('putting in jobs', t)
    with lock:
        if not todos.full():
            todos.put(t)
        else:
            print('todos is not full!')

    #lock.release()
    time.sleep(1)

while not todos.empty():
    print('sleeping 1, q[0]', todos.queue[0])
    time.sleep(1)

exitflag = 1
print(threading.activeCount(), threading.enumerate())
for t in threads:
    print('joins', t.name, t.is_alive())
    t.join()

print('exit main thread')