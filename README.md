# UAV GROUND STATION v1.0

This project is a **Ground Station Application** for Unmanned Aerial Vehicles (UAVs). It provides a graphical interface to monitor and control UAVs in real-time. The application displays telemetry data, visualizes graphs for altitude and velocity, and includes a live camera feed. It is built using Python and various libraries such as `Tkinter`, `Matplotlib`, and `Pymavlink`.

---

## Features

- **Real-Time Telemetry**: Displays UAV telemetry data such as latitude, longitude, altitude, velocity, battery status, and more.
- **Graphical Visualization**: Real-time graphs for altitude, velocity, and battery status.
- **Live Camera Feed**: Displays a live video feed from a connected camera.
- **Data Logging**: Logs telemetry data to a file for later analysis.
- **Interactive Interface**: Easy-to-use buttons for switching between telemetry views, graphs, and battery status.

---

## Prerequisites

Before running the application, ensure you have the following installed:

1. **Python 3.8+**
2. Required Python libraries:
   - `tkinter`
   - `matplotlib`
   - `pymavlink`
   - `opencv-python`
   - `Pillow`
   - `serial`

You can install the required libraries using the following command:

```bash
pip install matplotlib pymavlink opencv-python Pillow pyserial
```
---
## Installation

1. Clone the repository or download the project files:
```bash
git clone https://github.com/your-repo/uav-ground-station.git
cd uav-ground-station
```

2. Ensure the `main.py` file and the `assets` folder (containing images and other resources) are in the same directory.

3. Update the `ASSETS_PATH` in the `main.py` file to point to the correct location of your assets folder:

```ruby
ASSETS_PATH = Path(r"C:\path\to\your\assets\folder")
```

4. Connect your UAV to the computer via a serial port. Update the `COM` port in the `main.py` file:

```ruby
serial.Serial("COM1")  # Replace "COM1" with your UAV's serial port
```

---
## Usage
1. Run the application:

```bash
python main.py
```

2. The main window will open, displaying the following features:

    - **Graphs:** Real-time graphs for altitude and velocity.
    - **Telemetry Table:** Displays GPS data (latitude, longitude, altitude) in a table format.
    - **Battery Status:** Visual representation of the UAV's battery level.
    - **Live Camera Feed:** Displays a live video feed from the connected camera.

3. Use the buttons to switch between views:

    - **General Data:** Displays altitude and velocity graphs.
    - **GPS Data:** Displays the telemetry table.
    - **Battery Status:** Displays battery and voltage graphs.

4. To connect to the UAV, click the Connect button. The application will start receiving telemetry data and updating the graphs and table in real-time.

5. To disconnect from the UAV, click the Disconnect button.

## Logging

The application logs all telemetry data to a file named logs.txt. The log file contains the following information:

 - Timestamp
 - Latitude
 - Longitude
 - Altitude
 - Velocity
 - Roll, Pitch, Yaw
 - Battery Voltage and Remaining Capacity

The log file is saved in the same directory as the application.

## Future Improvements

- Add support for multiple UAVs.
- Integrate a map view for real-time UAV tracking.
- Enhance the user interface with more customization options.
- Add support for additional telemetry data.

## Contact

For any questions or issues, please contact:
 - Name: Timur Mert USTA
 - Email: timurmertusta@gmail.com
 - GitHub: https://github.com/timurmert/
