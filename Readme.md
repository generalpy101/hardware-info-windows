## Get Realtime Hardware Information

### Description
This script is used to get the realtime hardware information of the system. This script is written for **Windows** and uses **Libre Hardware Monitor** to access realtime data. Data will be stored in CSV file and can be used for further analysis. A lot of information can be extracted from the system like CPU, GPU, RAM, Motherboard, Storage, Network, etc. but this script is used to get temperatures(usecase specific).

### Requirements
- Python 3.x
- [Libre Hardware Monitor](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor)
- [WMI](https://pypi.org/project/WMI/)

### Installation
- Install Python 3.x
- Install required packages using `pip install -r requirements.txt`
- Download and install Libre Hardware Monitor from [here](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases)
- Run the script using `python main.py`