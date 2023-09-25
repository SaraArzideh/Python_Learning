import threading
from time import sleep
from random import randint

condition_value=0

# Worker function for the threads.
def worker(lock,id,value,condition):
    global condition_value
    with lock:
        print("{} thread acquired lock".format(id))
        print("Will sleep for {} seconds".format(value))
        sleep(value)
        condition_value=condition_value+1
        if condition_value==10:
            print ("Last one. Notifynig main")
            condition.notify()
    return value

# Main function where the program starts execution.
def main():
    lock=threading.Lock()
    condition =threading.Condition(lock)
    threads=[]
    condition.acquire()
    for i in range (10):    # Create and start 10 worker threads.storing the thread objects in the 'threads' list.
        thread_id=threading.Thread(target=worker,args=(lock,i,randint(0,5),condition))
        thread_id.start()
        threads.append(thread_id)
    
    print("Main: waiting for condition")
    condition.wait()   # Main thread waits until the condition is fulfilled.
    
    for j in range(10):
        threads[j].join()   # Wait for all worker threads to complete.
    print("Done!")

if __name__=="__main__":
    main()
