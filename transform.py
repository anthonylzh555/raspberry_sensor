import time
from datetime import datetime
from tqdm import tqdm

def transform(time:list):
    n = 0 
    new = []
    for i in tqdm(time, position=0, leave=True):
        time.iloc[n] = datetime.fromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S')
        n += 1
    return time