# Предположим, что у нас есть список текстовых файлов в папке, например, C:/temp/.
# Мы хотим заменить текст во всех файлах.
# Однопоточная программа:

from time import perf_counter

def replace(filename, substr, new_substr):
    print(f"Working on the file {filename}")
    
    try:
        # получаем содержимое файла
        with open (filename, 'r') as f:
            content = f.read()

        # заменяем substr на new_substr
        content = content.replace(substr, new_substr)

        # записываем данные в файл
        with open (filename, 'w') as f:
            f.write(content)

    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
    except PermissionError:
        print(f"Error: Permission denied writing to {filename}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():

    filenames = [
        'c:/Test_HW/test1.txt',
        'c:/Test_HW/test2.txt',
        'c:/Test_HW/test3.txt',
        'c:/Test_HW/test4.txt',
        'c:/Test_HW/test5.txt',
    ]

    for filename in filenames:
        replace(filename, "ids", "id")


if __name__ == '__main__':
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f"Execution took {end_time - start_time} seconds")
