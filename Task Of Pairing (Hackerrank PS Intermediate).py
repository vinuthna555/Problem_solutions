!/bin/python3

import math
import os
import random
import re
import sys



# Complete the 'taskOfPairing' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY freq as parameter.
#

def taskOfPairing(freq):
    ans=0
    n=len(freq)
    for i in range(0,len(freq)-1):
        ans+=freq[i]//2
        if freq[i+1]!=0:
            freq[i+1]+=freq[i]%2
    return ans+freq[n-1]//2
    
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    freq_count = int(input().strip())

    freq = []

    for _ in range(freq_count):
        freq_item = int(input().strip())
        freq.append(freq_item)

    result = taskOfPairing(freq)

    fptr.write(str(result) + '\n')

    fptr.close()

