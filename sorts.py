import time
import random
import sys

#a = (4,7,2,3,4,8,5,2,3,6,7,9)                                                                                                                                                                                                           

def qsort(a):
    if not a: return []
    return qsort([x for x in a if x < a[0]]) + [x for x in a if x == a[0]] + qsort([x for x in a if x > a[0]])

m = int(sys.argv[1])
a = [random.randint(0, m) for x in range(m)]
print("Starting")

start_0 = time.time()
ss = sorted(a)
print("Etalon: %d" %(time.time() - start_0))

start_1 = time.time()
rs = [a[0]]
rn = [a[0]]
min = a[0]
max = a[0]
for x in a[1:]:
    #print("Checking " + str(x))
    if (x <= min):                                                                                                                                                                                                                       
        rn[0] = x
        #print("Before moving min %s" % (rn))
        rn[1:] = rs[:]
        #print("After moving min %s" % (rn))
        min = x
    else:
        if (x > max):
            rn.append(x)
            max = x
        else:
            num = 0
            for y in rs:
                #print("Inside check %d" % y)
                #time.sleep(1)
                if (x <= y):
                    #print("Found place %d" % x)
                    rn[num] = x
                    rn[num + 1:] = rs[num:]
                    break

                rn.append(y)
                num = num + 1

    rs = rn[:]
    #print("Preresult " + str(rs))

if (rs != ss):
    res = "FAILED"
else:
    res = "PASSED"

print("Result: %s %d" % (res, time.time() - start_1))

start_2 = time.time()
qs = qsort(a)
if (qs != ss):
    res = "FAILED"
else:
    res = "PASSED"

print("QSort:  %s %d" % (res, time.time() - start_2))

