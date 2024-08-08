import os
import time

# Define application path and delay
application_path = "C:\Program Files\WinRAR\WinRAR.exe"  # Replace with your actual path
delay = 10 # Adjust delay as needed (in seconds)

try:
    while True:
        # Open the application
        print(f"Opening application: {application_path}")
        os.startfile(application_path)

        # Wait for the specified delay
        time.sleep(delay)

        # Close the application using taskkill (construct command outside f-string)
        command = "taskkill /f /im " + application_path.split('\\')[-1]
        os.system(command)

except KeyboardInterrupt:
    print("Program terminated by user.")
