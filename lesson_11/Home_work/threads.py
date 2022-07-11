import random
import threading
from time import sleep

my_list = []
max_num = 1_000_000


def list_creation(max_num, my_list):
    print("Starting Thread_1")
    for i in range(0, max_num):
        i = random.randint(1, 1500)
        my_list.append(i)
    print("Сalculations done")


def get_sum(my_list):
    print("Starting Thread_2")
    print("Sum ======>", sum(my_list))


def get_average(max_num, my_list):
    print("Starting Thread_3")
    print("Average ======>", sum(my_list) / max_num)


def main():

    thread_1 = threading.Thread(
        target=list_creation, kwargs={"max_num": max_num, "my_list": my_list}
    )
    thread_2 = threading.Thread(target=get_sum, kwargs={"my_list": my_list})
    thread_3 = threading.Thread(
        target=get_average, kwargs={"max_num": max_num, "my_list": my_list}
    )

    thread_1.start()

    while True:
        if thread_1.is_alive():
            sleep(1)
        else:
            thread_2.start()
            thread_3.start()
            break


if __name__ == "__main__":
    main()
