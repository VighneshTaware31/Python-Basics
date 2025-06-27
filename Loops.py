# 1. For Loop with Range
print("For Loop from 1 to 5:")
for i in range(1, 6):
    print("Number:", i)

# 2. For Loop over a List
fruits = ["apple", "banana", "cherry"]
print("\nLooping through a list:")
for fruit in fruits:
    print("Fruit:", fruit)

# 3. Nested For Loop
print("\nNested For Loop:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# 4. While Loop
print("\nWhile Loop from 1 to 5:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# 5. Loop with Break
print("\nLoop with Break:")
for i in range(10):
    if i == 5:
        print("Breaking at", i)
        break
    print("i:", i)

# 6. Loop with Continue
print("\nLoop with Continue:")
for i in range(5):
    if i == 2:
        continue
    print("i:", i)


