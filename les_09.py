# Analog Condition via Semaphore

import logging
from threading import Thread, Semaphore
from time import sleep


def worker(condition: Semaphore):
    logging.debug("Worker is ready to work")

    condition.acquire()

    logging.debug("The worker can do the work")


def master(condition: Semaphore):
    logging.debug("Master's doing some work")
    sleep(2)

    logging.debug("Informing that workers can do their work")
    
    for _ in range(2):
        condition.release()

if __name__ == '__main__':
    
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(threadName)s %(message)s"
    )

    condition = Semaphore(0) # створюємо залочену семафору

    master = Thread(name="master", target=master, args=(condition,))

    worker_one = Thread(name="worker_one", target=worker, args=(condition,))
    worker_two = Thread(name="worker_two", target=worker, args=(condition,))

    worker_one.start()
    worker_two.start()

    master.start()

    logging.debug("End program")
