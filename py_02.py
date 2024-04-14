# Functor

from threading import Thread
from time import sleep
import logging


class UsefulClass():

    def __init__(self, second_num) -> None:
        self.delay = second_num

    def __call__(self):
        sleep(self.delay)
        logging.debug("Wake up!")


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")

    t2 = UsefulClass(2)
    
    thread_1 = Thread(target=t2) # Напряму створюємо екземпляр класу Tread # target = аргумент, що має бути функцією
    thread_2 = Thread(target=t2)
    thread_3 = Thread(target=t2)
    
    thread_1.start()
    thread_2.start()
    thread_3.start()

    print("Some stuff")
