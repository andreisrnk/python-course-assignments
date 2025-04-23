import sys

# Expect: python rectangle.py <height> <width>
if len(sys.argv) != 3:
    print("Usage: python rectangle.py <height> <width>")
    sys.exit(1)

try:
    height = float(sys.argv[1])
    width  = float(sys.argv[2])
except ValueError:
    print("Height and width must be numbers.")
    sys.exit(1)

area = height * width
perimeter = 2 * (height + width)

print(f"Area of the rectangle: {area:.2f}")
print(f"Perimeter of the rectangle: {perimeter:.2f}")
