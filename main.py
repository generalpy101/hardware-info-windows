import wmi
import csv
import time

from datetime import datetime

# File name format is dataset_posixtimestamp.csv
with open(f"dataset_{datetime.now().timestamp()}.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    hwmon = wmi.WMI(namespace="root\LibreHardwareMonitor")
    sensors = hwmon.Sensor(SensorType="Temperature")

    writer.writerow(['Timestamp'] + [s.Name + s.Identifier for s in sensors])
    
    while True:
        hwmon = wmi.WMI(namespace="root\LibreHardwareMonitor")
        sensors = hwmon.Sensor(SensorType="Temperature")

        try:
            # Write values, each column contains the value of the sensor
            writer.writerow([datetime.now()]+[s.Value for s in sensors])
            
            # Sleep for a while for better readings
            time.sleep(1)
        except KeyboardInterrupt:
            break

print("Done")
