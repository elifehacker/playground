import multiprocessing as mp
from multiprocessing import Process, Lock
import time

#https://docs.python.org/3/library/multiprocessing.html

def run(i, lock, backlog):
    print('new run')
    while True:
        with lock:
            if not backlog.empty():
                task = backlog.get()
                print(i, 'working on task:', task)
            else:
                print(i,'backlog empty')
        time.sleep(1)
        
if __name__ == '__main__':
    backlog = mp.Queue(5)
    lock = Lock()
    ps = list()
    for i in range(3):
        p = Process(target=run, args=(i,lock,backlog))
        print('process created',p)
        p.start()
        ps.append(p)
        print('process started.')
    i = 0
    while i < 10:
        with lock:
            if not backlog.full():
                print('added', i)
                backlog.put(i)
                i+=1
            else:
                print('cannot add becuase backlog is full')
        time.sleep(0.15)

    while True:
        with lock:
            if backlog.empty():
                print('finished!')
                break
            else:
                print('not empty')
        time.sleep(1)

    for p in ps:
        p.terminate()
        p.join()
    print("all done!")

