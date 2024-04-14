# Потік у функції

from threading import Thread
from time import sleep
import logging


def example_work(delay, blablabla):
    sleep(delay)
    logging.debug(f"Wake up! {blablabla}")

if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    
    for i in range(5):

        thread = Thread(target=example_work, args=(i, "asdfghjkll"))
        thread.start()

        # щоб вистачило часу на рандомний порядок за допомогою GIL ticks
        # thread = Thread(target=example_work, args=(5, "asdfghjkll"))
        # thread.start()
