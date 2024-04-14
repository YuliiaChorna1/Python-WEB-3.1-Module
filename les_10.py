from threading import Thread, Event
import logging
from time import sleep


def example_work(event_for_exit: Event, new_event: Event):

    while True:
        sleep(1)
        logging.debug("Run event work")

        if new_event.is_set():
            logging.debug("I caught it!")
            new_event.clear()

        if event_for_exit.is_set():
            break

def example_worker_2(event_for_exit: Event, new_event: Event):
    while True:
        sleep(2)
        logging.debug("I sent it!")
        new_event.set()

        if event_for_exit.is_set():
            break

if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    
    event = Event()
    new_event = Event()
    thread = Thread(target=example_work, args=(event, new_event))
    thread.start()

    thread = Thread(
        target=example_worker_2, 
        kwargs={"event_for_exit": event, "new_event": new_event}
        )
    thread.start()

    # new_event.set()
    # sleep(2)
    # new_event.set() # instead of def worker2

    sleep(5)
    event.set()

    logging.debug("End of program")