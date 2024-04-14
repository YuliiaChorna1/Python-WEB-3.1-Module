# Предположим, что у нас есть список текстовых файлов в папке, например, C:/temp/.
# Мы хотим заменить текст во всех файлах.
# Многопоточная программа:

from time import perf_counter
from threading import Thread


def replace(filename, substr, new_substr):
    print(f"Working on the file {filename}")
    
    # getting file content
    with open(filename, 'r') as f:
        content = f.read()

    # replacing substr on new_substr
    content = content.replace(substr, new_substr)

    # writing data
    with open(filename, 'w') as f:
        f.write(content)

def main():
    filenames = [
        'c:/Test_HW/test1.txt',
        'c:/Test_HW/test2.txt',
        'c:/Test_HW/test3.txt',
        'c:/Test_HW/test4.txt',
        'c:/Test_HW/test5.txt',
    ]

    # creating treads
    threads = [Thread(target=replace, args=(filename, "id", "ids"))
               for filename in filenames]
    
    # starting threads
    for thread in threads:
        thread.start()

    # waiting for completing
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f"Execution took {end_time - start_time: 0.2f} seconds")
