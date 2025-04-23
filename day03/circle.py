import sys
import math

# Expect: python circle.py <radius>
if len(sys.argv) != 2:
    print("Usage: python circle.py <radius>")
    sys.exit(1)

try:
    radius = float(sys.argv[1])
except ValueError:
    print("Radius must be a number.")
    sys.exit(1)

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")
