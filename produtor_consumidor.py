#!/usr/bin/env python3
import threading
import time
import random
import sys

time = int(sys.argv[1])
thread_pro=int(sys.argv[2])
thread_con=int(sys.argv[3])

class Armazem:
    size_buffer = 5
    mutex = threading.Semaphore(1)
    empty = threading.Semaphore(tamanho_buffer)
    full = threading.Semaphore(0)
    buffer = list(range(tamanho_buffer))
    live = 0
    empty = 0


    def insert(self, value):
        self.empty.acquire()
        with self.mutex:
            self.buffer[self.live] = value
        self.live = (self.live + 1) % self.size_buffer
        self.full.release()

    def remove(self):
        self.full.acquire()
        with self.mutex:
            item = self.buffer[self.empty]
        self.empty = (self.empty + 1) % self.size_buffer
        self.empty.release()
        return item


a = Armazem()

def produtor(a):
    while True:
        sleep=random.randint(1,10)
        time.sleep(sleep)
        value = random.randint(1,100)
        a.insert(value)
        print('PRODUTOR',i,': produziu',value)
        print('PRODUTOR',i,': Dormindo por',sleep)


def consumidor(a):
    while True:
        sleep=random.randint(1, 10)
        time.sleep(sleep)
        value = a.remove()
        print('CONSUMIDOR ',i,': Consumiu:',value)
        print ('CONSUMIDOR ',i,': Dormindo por', sleep)



def main():
    for i in range(thread_pro):
        p = threading.Thread(target=produtor,daemon=True,args=(a,i,)).start()
    for i in range(thread_con):
        c = threading.Thread(target=consumidor,daemon=True, args=(a,i,)).start()
    time.sleep(time)

main()
