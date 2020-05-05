import timeit

SETUP_CODE = """
import requests
import repackage

repackage.up()
numbers = ""

with open("numbers.txt") as f:
    numbers = f.read()

def makePostRequest(url):
    r= requests.post(url, data = numbers)  
    return r.text
"""

TEST_CODE_PYTHON = """
makePostRequest('http://127.0.0.1:5000/api/sort')
"""

TEST_CODE_JS = """
#Change this to the js url
makePostRequest('http://127.0.0.1:5000/api/sort')
"""

import numpy as np
from scipy import stats

times1 = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 100, number = 1)
#Just to try t-test
times2 = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE_JS, repeat = 100, number = 1)

mean = np.mean(times1)
median = np.median(times1)
tTest = stats.ttest_ind(times1, times2)


print(f"Medelvärde: {mean} Median: {median} T-test: {tTest}")




