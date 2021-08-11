from multiprocessing import Process, Lock, Queue
import time

def worker(id, lock, backlog):
    while True:
        with lock:  # always aquire lock before checking shared memory
            if not backlog.empty(): # check not empty
                print(id, backlog.get())
        time.sleep(1)

if __name__ == '__main__':
    backlog = Queue(5)
    lock = Lock()
    processes = list()
    for i in range(3):
        p = Process(target=worker, args=(i,lock,backlog))
        processes.append(p)
        p.start()
    for i in range(10):
        with lock:
            print('add to backlog', i)
            if not backlog.full():  # check not full
                backlog.put('task'+str(i))
        time.sleep(0.3)
    while True:
        if backlog.empty():   #check not empty again
            break
        time.sleep(1)
    for p in processes:
        p.terminate()
        p.join()
    print('finished')