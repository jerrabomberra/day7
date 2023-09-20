import random
from collections import Counter

counter=Counter()

object_list=["a","b","c","d","e"]

tab=[]
for _ in range(100):
    obj=random.choice(object_list)
    counter[obj]+=1
for key, value in sorted(counter.items()):
    print(''.join(key),":",''.join(str(value)))
   
