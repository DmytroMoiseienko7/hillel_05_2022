import random
import threading

my_list = []
max_num = 1_000_000


def list_creation(max_num, my_list):
    print("Starting Thread_1")
    for i in range(0, max_num):
        i = random.randint(1, 1500)
        my_list.append(i)
    print("Сalculations done")


def get_sum(my_list, thread):
    print("Starting Thread_2")
    while True:
        if thread.is_alive() is True:
            True
        else:
            print("Sum ======>", sum(my_list))
            break


def get_average(max_num, my_list, thread):
    print("Starting Thread_3")
    while True:
        if thread.is_alive() is True:
            True
        else:
            print("Average ======>", sum(my_list) / max_num)
            break


def main():

    thread_1 = threading.Thread(
        target=list_creation, kwargs={"max_num": max_num, "my_list": my_list}
    )
    thread_2 = threading.Thread(
        target=get_sum, kwargs={"my_list": my_list, "thread": thread_1}
    )
    thread_3 = threading.Thread(
        target=get_average,
        kwargs={"max_num": max_num, "my_list": my_list, "thread": thread_1},
    )

    thread_1.start()
    thread_2.start()
    thread_3.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()


if __name__ == "__main__":
    main()
