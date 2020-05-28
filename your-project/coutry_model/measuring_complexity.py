import pandas as pd
import numpy as np

import time
start_time = time.time()

df = pd.DataFrame(columns=['id', 'age', 'gender', 'BMI', 'smoke', 'alco', 'active'])

for i in range(3*(10**5)):
    df = df.append({'id':0, 'age':0, 'gender':0, 'BMI':0, 'smoke':0, 'alco':0, 'active':0} , ignore_index=True)

print ("My program took", time.time() - start_time, "to run")