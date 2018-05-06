import argparse
import sys
import time

def get_seed(s):
    ''' returns the seed (0, 1, 01, 10, 010, 101) for a given string '''
    count_zero = s.count('0')
    count_one = s.count('1')
    if (count_zero == 0 and count_one != 0):
        return '1'
    if (count_zero != 0 and count_one == 0):
        return '0'
    if s[0] == '0' and s[len(s) - 1] == '0':
        return '010'
    if s[0] == '0':
        return '01'
    if s[len(s) - 1] == '0':
        return '10'
    return '101'

def possible_dedupes(s):
    '''Given string s, return a list of all possible deduplications'''
    dedupes = set() # sets discard duplicate elements
    for offset in range(len(s)):
        for dist in range(1, int((len(s) - offset) / 2) + 1):
            if (s[offset:offset+dist] == s[offset+dist:offset+ 2*dist]):
                dedupes.add(s[:offset] + s[offset+dist:])
    return list(dedupes)

def solve(s):
    n = 0
    '''this is the template solve function. please place your code here
    it should return an integer with value n which maps to the number
    of steps it takes to get to the initial string'''
    seed = get_seed(s)
    # TODO
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
    
