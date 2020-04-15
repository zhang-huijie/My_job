import time
import itertools

time_start=time.time()
sum2=0 
a=[1,2,3,4] 
for i in itertools.permutations(a,3): 
    print(i) 
sum2+=1 
time_end=time.time()
print(sum2)
print('time cost',time_end-time_start,'s')