"""
    Load simulation data from a sensor to blob storage
"""
import os
import json
import dotenv

from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

import pandas as pd
import numpy as np

import auth
import storage

load_dotenv()

with Path(__file__).with_name('sensors.json').open('r') as f:
    sensors = json.load(f)

sensors = pd.DataFrame(sensors)
samples = 1000
random_sensors = np.random.randint(0, sensors.shape[0], samples)
data = sensors.to_numpy()[random_sensors]
data = np.column_stack((np.arange(samples), data, data[:, 1] + np.random.randn(samples)*data[:,2]))

df = pd.DataFrame(data, columns=['time', 'id', 'mean', 'var', 'value'])[['time', 'id', 'value']]
df['time'] = df['time'].apply(lambda t: (datetime.now()+timedelta(minutes=t)).isoformat())
df = df[['id', 'time', 'value']]

date = datetime.now().strftime("%Y%m%d")
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

storage_client = storage.StorageClient(os.getenv('STORAGE_ACCOUNT'), auth.get_default_credential())
storage_client.create_blob(
    os.getenv('CONTAINER'),
    f'sensors/{date}/{timestamp}.csv',
    bytes(df.to_csv(index=False), encoding='utf-8')
)