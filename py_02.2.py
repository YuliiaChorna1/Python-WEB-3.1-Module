from time import sleep, perf_counter
from threading import Thread


def task():

    print("Start working on task...")
    sleep(1)
    print("Done")

start_time = perf_counter()

t1 = Thread(target=task)
t2 = Thread(target=task)

# запускаем потоки
t1.start()
t2.start()

# ждем, когда потоки выполнятся
t1.join()
t2.join()

end_time = perf_counter()

print(f"Execution took {end_time - start_time: 0.2f} seconds")
