# Temperature-Monitoring-System_VanshikaBansal_202501100700221
🌡️ Temperature Monitoring System
1️⃣ Problem Statement

Design a Temperature Monitoring System that simulates real-time temperature readings using Python.

The system should:

Accept minimum and maximum temperature limits from the user.

Continuously generate random temperature readings (simulating IoT sensor data).

Compare each reading with the defined limits.

Display:

⚠️ Alert if temperature is below minimum limit

⚠️ Alert if temperature is above maximum limit

✅ Safe message if temperature is within range

Repeat the process every 2 seconds.

2️⃣ Approach

Import required modules:

random → to generate random temperature values.

time → to pause execution for 2 seconds between readings.

Take user inputs:

Minimum temperature limit

Maximum temperature limit

Use an infinite while True loop to simulate continuous monitoring.

Inside the loop:

Generate a random temperature between (min_temp - 10) and (max_temp + 10)

Print the current temperature.

Compare it with user-defined limits using:

if → for below minimum limit

elif → for above maximum limit

else → for safe range

Pause execution for 2 seconds using time.sleep(2).

3️⃣ How to Run the Program
Step 1: Save the Code

Save the file as:

temperature_monitor.py
Step 2: Open Terminal / Command Prompt

Navigate to the folder where the file is saved.

Step 3: Run the Program
python temperature_monitor.py

OR (if using Python 3 specifically):

python3 temperature_monitor.py
Step 4: Enter Inputs

Example:

Enter minimum temperature limit: 20
Enter maximum temperature limit: 30

The system will start monitoring continuously.

To stop the program:
Press CTRL + C

4️⃣ Example Output
Enter minimum temperature limit: 20
Enter maximum temperature limit: 30

--- Temperature Monitoring System Started ---

Current Temperature: 18.45 °C
⚠️ ALERT: Temperature below minimum limit!

Current Temperature: 25.67 °C
✅ Temperature is within safe range.

Current Temperature: 34.12 °C
⚠️ ALERT: Temperature above maximum limit!

Current Temperature: 27.89 °C
✅ Temperature is within safe range.
