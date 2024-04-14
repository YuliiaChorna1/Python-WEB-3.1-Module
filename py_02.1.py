import logging
from threading import Thread
from time import sleep


class ExecutorClass:

    def __init__(self, seconds):
        self.seconds = seconds

    def __call__(self):
        sleep(self.seconds)
        logging.debug("Wake up!")
        logging.debug(f"args: {self.seconds}")


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(threadName)s %(message)s"
    )

    for i in range(5):
        thread = Thread(target=ExecutorClass(i))
        thread.start()

    print("Useful message")

