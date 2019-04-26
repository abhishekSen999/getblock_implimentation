import os
import time
import multiprocessing
import signal

def sigint_catcher( sig,frame):
    print("caught sigint pid:",os.getpid())

def process1(i):

    # print("print process group process1:", os.getpgid(os.getpid()))



    signal.signal(signal.SIGINT,sigint_catcher)
    print("process1 pid:",os.getpid(),"will pause")
    
    signal.pause()


def process2(i):

    # print("print process group process2:", os.getpgid(os.getpid()))


    signal.signal(signal.SIGHUP,sigint_catcher)
    print("process2 pid:",os.getpid(),"will pause")
    
    signal.pause()





if __name__=="__main__":
    p1=multiprocessing.Process(target=process1,args=(1,))
    p2=multiprocessing.Process(target=process2,args=(1,))
    p1.start()
    p2.start()

    # print("print process id main:", os.getpid())

    # print("print process group main:", os.getpgid(os.getpid()))


    print("waiting for 5 seconds")
    time.sleep(2)
    os.killpg(os.getpgid(os.getpid()),signal.SIGINT)
    #os.kill(p2.pid,signal.SIGCHLD)
    print("reached")

    time.sleep(5)
    os.killpg(os.getpgid(os.getpid()),signal.SIGHUP)


    


    