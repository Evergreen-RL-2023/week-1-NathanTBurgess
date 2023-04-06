'''
computing averages and 1-armed bandit

3 ways to compute averages
The third method uses temporal difference
see Sutton and Barto
Q = Q + a*(R - Q), where in this case Q is the average
and R is the new value to be averaged

also use rand.gauss(0, 1) instead of i

'''
'''
computing averages and 1-armed bandit

3 ways to compute averages
'''

import random as rand

N = 10000
m = 0
s = 100
val = []
for i in range (1,N):
    val.append(rand.gauss(m,s))

def average1():
    sum = 0
    for i in range(1,N):
        sum += val[i-1]
    mean = sum / (N - 1)
    print('avg1', mean)

def average2():
    avg = 0
    for i in range(1,N):
        avg = avg * (i-1)/i + val[i-1]/i
    print("avg2", avg)

def average3():
    avg = 0
    for i in range(1,N):
        avg = (i/i) * avg - (1/i) * avg + val[i-1]/i
    print('avg3', avg)
if __name__ == '__main__':
    average1()
    average2()
    average3()
    
