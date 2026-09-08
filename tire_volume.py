import math
from datetime import datetime

# Get the tire measurements from the user
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the tire volume in liters

volume = (
    math.pi
    * width ** 2
    * aspect_ratio
    * (width * aspect_ratio + 2540 * diameter)
) / 10000000000

# Display the volume
print(f"The approximate volume is {volume:.2f} liters")

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Append the information to volumes.txt
with open("volumes.txt", "a") as file:
    file.write(
        f"{current_date}, {width}, {aspect_ratio}, "
        f"{diameter}, {volume:.2f}\n"
    )


