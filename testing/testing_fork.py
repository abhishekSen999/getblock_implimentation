import os
def parent_child():
    print("prodess id: ",os.getpid())
    
    pid=os.fork()
    if(pid==0):
        print("child process id: ",os.getpid())


if __name__=="__main__":
    parent_child()