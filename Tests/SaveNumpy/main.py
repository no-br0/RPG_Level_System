import numpy as np
import os

region = np.zeros((5,5), dtype=int)
print(region)


mylist = np.random.randint(1,10, size=(4,4))
print(mylist)


otherlist = np.arange(1,10).reshape(3,3)
print(otherlist)


#list = np.zeros((10,10), dtype=int)
#print(list)
#list[0,0] = 1
#np.savetxt("Tests/SaveNumpy/test.txt", list, fmt='%i')
#if os.path.exists("Tests/SaveNumpy/test.txt"):
#    list2 = np.loadtxt('Tests/SaveNumpy/test.txt', dtype=int)
#
#    print(list2)


