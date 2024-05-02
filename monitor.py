##############################################################################
#                                FILE INFORMATION                            #
##############################################################################
# File Name   : your_file_name.py
# Author      : Ben Miller
# Class       : Your Class/Subject
# Date        : 2024-05-01
# Description : 
#   This Python file serves the purpose of provide a detailed description
##############################################################################
import clr  # Import the pythonnet module
import time

# Add a reference to the Open Hardware Monitor library DLL
clr.AddReference(r'OpenHardwareMonitorLib')

from OpenHardwareMonitor.Hardware import Computer, SensorType

# Initialize the Computer object and enable CPU and GPU monitoring
computer = Computer()
computer.CPUEnabled = True
computer.GPUEnabled = True
computer.Open()

try:
    while True:
        # Iterate through all hardware items (CPU, GPU, etc.)
        for hardware in computer.Hardware:
            hardware.Update()  # Update the hardware data
            # Iterate through all sensors in this hardware
            for sensor in hardware.Sensors:
                # Check if the sensor is a temperature sensor
                if sensor.SensorType == SensorType.Temperature:
                    print(f"{sensor.Name}: {sensor.Value}°C")
        time.sleep(1)  # Sleep for 1 second before updating again
except KeyboardInterrupt:
    print("Stopped by user")

# Close the connection to the hardware
computer.Close()
