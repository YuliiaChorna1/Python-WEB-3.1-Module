# Condition

import logging
from threading import Thread, Condition
from time import sleep


def worker(condition: Condition):

    logging.debug("Worker is ready to work")
    
    with condition:
        condition.wait()
        logging.debug("The worker can do the work")

def master(condition: Condition):

    logging.debug("Main is doing some work")
    sleep(2)

    with condition:

        logging.debug("Informing that workers can do the work")
        condition.notify_all()


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")

    condition = Condition()

    master = Thread(name="master", target=master, args=(condition, ))
    
    worker_one = Thread(name="worker_one", target=worker, args=(condition, ))
    worker_two = Thread(name="worker_two", target=worker, args=(condition, ))

    worker_one.start()
    worker_two.start()
    master.start()

    logging.debug("End of program")
