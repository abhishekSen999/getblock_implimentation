import multiprocessing
import time
def print_value_1(num):
    
    while(num!=0):
        time.sleep(1)
        num=num-1
    print("value1:",num )

def print_value_2(num):
    while(num!=0):
        time.sleep(1)
        num=num-1
    print("value2",(num))

def print_value_3(num,lock):
    lock.acquire()
    print("value3",(num))

if __name__=="__main__":
    lock=multiprocessing.Lock()
    p1=multiprocessing.Process(target=print_value_3,args=(5,lock,))
    p2=multiprocessing.Process(target=print_value_3,args=(10,lock,))
   # p3=multiprocessing.Process(target=print_value_3,args=(2,))
    
    p1.start()
    p2.start()
    #p3.start()
    p2.join()
    p1.join()
    #p3.join()
    print("done")
    # k=input("press enter to exit")
#problem as lock not released

