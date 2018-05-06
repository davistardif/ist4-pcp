import argparse
import sys
import time
def solve(s):
    n = 0
    '''this is the template solve function. please place your code here
    it should return an integer with value n which maps to the number
    of steps it takes to get to the initial string'''
    #to do fill in code to get n
    return n

if __name__ == "__main__":
    if len(sys.argv) < 2: 
        print("using this file requires an input string \n python solver.py 1010 \n will run the program to solve for string 1010")
    else:  
        s = sys.argv[1]
        start_time = time.time()
        val = solve(s)
        total_time = time.time() - start_time 
        print('solved for string {} in {} steps taking {:1.4f} seconds'.format(s, val, time.time() - start_time))
    
