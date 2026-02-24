import random
import time

# Accept min and max temperature limits from user
min_temp = float(input("Enter minimum temperature limit: "))
max_temp = float(input("Enter maximum temperature limit: "))

print("\n--- Temperature Monitoring System Started ---\n")

# Infinite loop to simulate IoT temperature readings
while True:
    # Generate random temperature value
    current_temp = random.uniform(min_temp - 10, max_temp + 10)
    
    # Display current temperature
    print(f"Current Temperature: {current_temp:.2f} °C")
    
    # Compare with limits and display appropriate message
    if current_temp < min_temp:
        print("⚠️ ALERT: Temperature below minimum limit!\n")
    elif current_temp > max_temp:
        print("⚠️ ALERT: Temperature above maximum limit!\n")
    else:
        print("✅ Temperature is within safe range.\n")
    
    # Wait for 2 seconds before next reading
    time.sleep(2)
