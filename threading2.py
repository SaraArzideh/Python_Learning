from time import sleep         # import sleep function from the time module
from random import randint     # import randint function from the raandom module
from threading import Thread   # import Thread class from the threading module
from threading import Lock     # import lock class from the threading module

def task(lock, id, value):
    with lock:
        # acquire the lock and print the thread ID
        print(f"{format(id)} thread aquiring lock")
        # print the sleep duraation
        print(f"Will sleep for {format(value)} seconds")
        # sleep for specified duration
        sleep(value)

def main():
    lock=Lock()
    # Create and start 10 threads, each running the 'task' function with different arguments
    for i in range(10):
        Thread(target=task,args=(lock,i,randint(0,5))).start()

if __name__=="__main__":
    main()

        