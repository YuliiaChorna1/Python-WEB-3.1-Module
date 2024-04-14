# У цьому прикладі ми запустили два потоки і один загальний RLock.
# Таке виведення означає, що один із потоків "взяв" lock і поки він його не "відпустив", 
# інший чекав доки lock звільниться. 
# Блокування ресурсу досягається виконанням команди locker.acquire(). 
# Це робиться, щоб загальним ресурсом міг користуватися лише один потік на один момент часу,
# і лише коли потік закінчить роботу із загальним ресурсом, він відпускає lock, 
# у нашому випадку команда locker.release(), і хтось інший зможе попрацювати з ресурсом. 
# Так гарантується, що загальний ресурс не потрапить у невизначений стан, 
# коли хтось почав із ним роботу та не закінчив, а хтось інший почав, і так далі.

from threading import Thread, RLock
import logging
from time import time, sleep


def func(locker, delay):

    timer = time()

    locker.acquire()
    sleep(delay)
    locker.release()

    logging.debug(f"Done {time() - timer}")


if __name__ == '__main__':

    lock = RLock()

    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")

    t1 = Thread(target=func, args=(lock, 2))
    t2 = Thread(target=func, args=(lock, 2))

    t1.start()
    t2.start()

    logging.debug("Started")
