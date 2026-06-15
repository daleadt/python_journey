# list

import time

size = 10_000_000
start_time = time.time()
li = [x * x for x in range(size)]
endtime = time.time()
print(endtime - start_time)


# numpy


import numpy as np
import time

size = 10_000_000
start_time = time.time()
a = np.array(size)
b = np.array(size)
c = a * b
diff = time.time()
print(diff - start_time)
