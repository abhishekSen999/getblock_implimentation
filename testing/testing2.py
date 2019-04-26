# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:23:26 2019

@author: abhishek sen
"""
import multiprocessing
def print_value_1(num,iterations):
    n=1
    for i in range(0,iterations*iterations):
        n=n*num*num*num*num*num*num*num*num*num*num*num*num*num*num*num*num*num*num*num
    # print("iterations: {0}    value: {1}".format(iterations,n) )
    return -1

def print_value_2(num):
    # print("value2",(num))
    return -2

if __name__=="__main__":
    p1=multiprocessing.Process(target=print_value_1, args=(10,1))
    p2=multiprocessing.Process(target=print_value_1,args=(10,10))
    p2.start()
    p1.start()
    
   
    
    p2.join()
    
    p1.join()
   
 
    print("done")
    k=input("press enter to exit")


