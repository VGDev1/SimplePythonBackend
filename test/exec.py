import timeit

SETUP_CODE = """
import requests
import repackage

repackage.up()
numbers = ""

with open("numbers.txt") as f:
    numbers = f.read()

def makePostRequest():
    r= requests.post('http://127.0.0.1:5000/api/sort', data = numbers)  
    return r.text
"""

TEST_CODE = """
makePostRequest()
"""

import numpy as np
from scipy import stats

times1 = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 100, number = 1)
#Just to try t-test
times2 = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 100, number = 1)

mean = np.mean(times1)
median = np.median(times1)
tTest = stats.ttest_ind(times1, times2)


print(f"Medelvärde: {mean} Median: {median} T-test: {tTest}")




