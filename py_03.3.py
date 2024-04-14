# Передача аргументов в потоки
from time import sleep, perf_counter
from threading import Thread


def task(id):

    print(f"Starting executing task {id}...")
    sleep(1)
    print(f"Task {id} is done")

start_time = perf_counter()

# making 10 threads
threads = []
for n in range(1, 11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

# ждем, когда потоки выполнятся
for t in threads:
    t.join()

end_time = perf_counter()


print(f"Execution took {end_time - start_time: 0.2f} seconds")
