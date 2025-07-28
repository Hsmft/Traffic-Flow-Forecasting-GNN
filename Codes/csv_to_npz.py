import numpy as np
import pandas as pd

file_path = "PeMS08.csv"

print("data is loading..")
df = pd.read_csv(file_path, sep=",")

df["time"] = pd.to_datetime(df["time"])
df = df.sort_values(by="time")

features = ["traffic_flow", "traffic_occupancy", "traffic_speed"]

df[features] = df[features].apply(lambda x: x.fillna(x.mean()), axis=0)

unique_sensors = sorted(df["entity_id"].unique())
time_steps = df["time"].nunique()

sensor_to_index = {sensor: i for i, sensor in enumerate(unique_sensors)}

data_array = np.zeros((time_steps, len(unique_sensors), len(features)), dtype=np.float32)

for i, (timestamp, group) in enumerate(df.groupby("time")):
    for _, row in group.iterrows():
        sensor_idx = sensor_to_index[row["entity_id"]]
        data_array[i, sensor_idx, :] = row[features].values

np.savez_compressed("PEMS08.npz", data=data_array)
print("npz file created")


