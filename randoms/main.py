import random

a = random.random()
print(a)

a = random.uniform(1, 10)
print(a)

a = random.randint(1, 10) # 10 is inclued
print(a)

a = random.randrange(1, 10) # 10 is excluded
print(a)

list1 = list("SANIYAJ")
print(random.choice(list1))

list1 = list("SANIYAJ")
print(random.sample(list1, 3)) #only 3 will bw taken

list1 = list("SANIYAJ")
random.shuffle(list1) # print the list in randome order
print(list1) # print the list in randome order


# seed function used to produce same randoms
# same seed values will produce same output
random.seed(1)
print(random.randint(0,9))
random.seed(2)
print(random.randint(0,9))
random.seed(1)
print(random.randint(0,9))
random.seed(2)
print(random.randint(0,9))

# so for security purpose we use secrets
import secrets
# not re produce able

print(secrets.randbelow(2)) # 2 is excluded
print(secrets.randbits(3)) # range in binary 111, for 4 it will be 1111


import numpy as np
a =np.random.rand(3) # 3 is a dimention here, we can use 3,2 for two diamentions
print(a)
b= [int(i*10) for i in a ]
print(b)









