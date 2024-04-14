import logging
from threading import Thread
from time import sleep

def runner(*args, **kwargs):
    sleep(2)

    for i in args:
        logging.debug(f"arg: {i}")

    for key, value in kwargs.items():
        logging.debug(f"kwargs: {key}={value}")

    logging.debug("Finish")


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(threadName)s %(message)s"
    )

    threads = []

    for i in range(5):
        thread = Thread(
            target=runner,
            args=(1, 2, 3),
            kwargs={"a": 3, "b": 2}
        )

        thread.start()
        threads.append(thread)

    # while any ([thread.is_alive() for thread in threads]):
    #     logging.debug("Waiting...")
    #     sleep(2)
        
    for thread in threads:
        thread.join()
        
    print("Useful message")
