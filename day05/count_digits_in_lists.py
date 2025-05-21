numbers = [1203, 1256, 312456, 98]

# Initialize a dictionary to hold counts for each digit 0-9
count = {}
for d in range(10):
    count[str(d)] = 0
print(count)

#Iterate through each number and each character in its string form
for num in numbers:
    for ch in str(num):
        if ch.isdigit():
            count[ch] += 1

# Print the results for digits 0 through 9
for d in range(len(count)):
    print(f"{d}  {count[str(d)]}")
