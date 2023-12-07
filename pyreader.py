import time
import os
import sys

def delay_print(s):
    s='\033[92m'+s+'\n'
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.08)

os.system('cls')
f = open("textFileToRead.txt", "r")


for x in f:
    x=x.rstrip()
    if (len(x.strip())!=0):
        delay_print(x)
    else:
        time.sleep(0.5)
f.close()


