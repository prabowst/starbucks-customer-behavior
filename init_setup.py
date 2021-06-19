import pandas as pd
import numpy as np

df = pd.read_json('data/portfolio.json', orient='records', lines=True)
print(df.head(15))