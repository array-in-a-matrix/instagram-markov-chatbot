import sys
from markov import markov


try:
    cmd_length = sys.argv[1]
    
    if cmd_length.isdigit():
        print(markov(int(cmd_length) - 1))
    else:
        print(markov())
except IndexError:
    print(markov())
