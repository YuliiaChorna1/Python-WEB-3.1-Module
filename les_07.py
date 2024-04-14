# LOCK / RLOCK examples

import logging
from threading import Thread, Lock, RLock
from time import time, sleep

# lock = Lock()
lock = RLock()

def func(locker, delay):

    timer = time()

    for i in range(3):
        locker.acquire()
        sleep(delay)
        # locker.release() # Without this - Deadlock
        logging.debug(f"Done {time() - timer}")

    for i in range(3):
        locker.release()
        
if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG, 
        format="%(threadName)s %(message)s"
        )
    
    t1 = Thread(target=func, args=(lock, 2))
    t2 = Thread(target=func, args=(lock, 2))

    t1.start()
    t2.start()
    
    logging.debug("Started")
