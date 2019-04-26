# Python program to illustrate
# the concept of locks
# in multiprocessing
import multiprocessing
import os
# function to withdraw from account


def withdraw(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

# function to deposit to account


def deposit(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value + 1
        
        lock.release()


def perform_transactions():

    # initial balance (in shared memory)
    balance2 = multiprocessing.Value('i', 200)
    balance1 = multiprocessing.Value('i', 100)
    lock = multiprocessing.Lock()

    # creating new processes
    p1 = multiprocessing.Process(target=withdraw, args=(balance1, lock))
    p2 = multiprocessing.Process(target=deposit, args=(balance1, lock))
    p3 = multiprocessing.Process(target=withdraw, args=(balance2, lock))
    p4 = multiprocessing.Process(target=deposit, args=(balance2, lock))

    # starting processes
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    # wait until processes are finished
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    # print final balance
    print("Final balance = {}".format(balance1.value))
    print("Final balance = {}".format(balance2.value))


if __name__ == "__main__":
    for _ in range(10):

        # perform same transaction process 10 times
        perform_transactions()
