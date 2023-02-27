import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv("Traffic_Incidents_Archive_2017.csv")
df["vehicle_count"] = np.empty(len(df), dtype=str)
df["day_of_year"] = np.empty(len(df), dtype=int)

vehicle_counts = []
for i in range(len(df)):
    desc = df.iloc[i][1].lower()
    if "two vehicle" in desc or "2 vehicle" in desc:
        vehicle_counts.append("two")
    elif "multi vehicle" in desc or "multi-vehicle" in desc:
        vehicle_counts.append("multi")
    elif "single vehicle" in desc or "single-vehicle" in desc or "stalled" in desc:
        vehicle_counts.append("one")
    elif "pedestrian" in desc:
        vehicle_counts.append("pedestrian")
    elif "light" in desc or "signal" in desc or "blank" in desc:
        vehicle_counts.append("traffic signal")
    elif "closed" in desc or "block" in desc or "closure" in desc:
        vehicle_counts.append("road closed")
    else:
        vehicle_counts.append("other")

df.vehicle_count = vehicle_counts

doy = []
for i in range(len(df)):
    date = datetime.strptime(df.iloc[i][2][:10], "%m/%d/%Y")
    doy.append(date.timetuple().tm_yday)

df.day_of_year = doy

df.to_csv("traffic_incidents_2017_modified.csv")
