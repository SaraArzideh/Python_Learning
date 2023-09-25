import threading #import the threading module to work with threading

def print_cube(num):
    print("Cube is: ", format(num*num*num))
def print_square(num):
    print("Square is: ", format(num*num))
def main():
    # Create two threads, one for printing squares and the other for printing cubes
    t1=threading.Thread(target=print_square,args=(10,))
    t2=threading.Thread(target=print_cube,args=(10,))

    #Start both threads
    t1.start()
    t2.start()

    # waait for both threads to finish(join them)
    t1.join()
    t2.join()
    # After bothy threads are done, print Done!
    print("Done!")

if __name__=="__main__":
    main()
