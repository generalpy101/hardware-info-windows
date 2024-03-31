################################################################
# Install:
# * python.exe -m pip install pypiwin32
# * python.exe -m pip install wmi
#
# Usage:
# * !! Make sure librehardwaremonitor is running !!
# * python basicwmi.py
################################################################

import wmi
import csv
import time

from datetime import datetime

hwmon = wmi.WMI(namespace="root\LibreHardwareMonitor")
sensors = hwmon.Sensor(SensorType="Temperature")

# File name format is dataset_YYYY-MM-DD.csv
with open(f"dataset_{datetime.now().date()}.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(['Timestamp'] + [s.Name for s in sensors])
    
    while True:
        try:
            # Write values, each column contains the value of the sensor
            writer.writerow([datetime.now()]+[s.Value for s in sensors])
            
            # Sleep for a while for better readings
            time.sleep(1)
        except KeyboardInterrupt:
            break

print("Done")
