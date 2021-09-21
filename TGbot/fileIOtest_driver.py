
import os

print(os.getcwd())

import pandas as pd

csv = pd.read_csv('user_profile.csv', index_col=0)

print(csv.head())