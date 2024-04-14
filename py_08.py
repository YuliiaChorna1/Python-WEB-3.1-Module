# Семафори підходять до блокування іншим шляхом та вказують, що 
# кілька потоків можуть користуватися ресурсом одночасно і цим обмежують кількість потоків. 
# Наприклад, ми не хочемо надсилати десятки тисяч запитів до мережі одночасно, 
# щоб не створювати навантаження на обладнання і вкажемо семафор, 
# щоб не більше ста потоків могли одночасно надсилати запити. 
# Щойно якийсь із потоків закінчить роботу і семафор його відпустить, 
# то наступний потік із черги очікування зможе зробити свій запит.
# Як приклад розглянемо виконання 10 потоків 
# і обмежимо виконання за допомогою семафору до 2 одночасно:

from threading import Semaphore, Thread
import logging 
from time import sleep


def worker(semaphore):

    with semaphore:
        
        logging.debug(f"Got semaphore")
        sleep(0.5)
        logging.debug(f"Finished")


if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    semaphore = Semaphore(3)

    for num in range(10):
        
        thread = Thread(name=f"Th-{num}", target=worker, args=(semaphore, ))
        thread.start()


