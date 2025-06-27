# 1. Writing to a File
with open("demo_file.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

print("File written successfully.")

# 2. Reading from a File
with open("demo_file.txt", "r") as file:
    content = file.read()
    print("\n--- File Content ---")
    print(content)

# 3. Reading Line by Line
with open("demo_file.txt", "r") as file:
    print("\n--- Reading Line by Line ---")
    for line in file:
        print(line.strip())

# 4. Appending to a File
with open("demo_file.txt", "a") as file:
    file.write("This line is appended.\n")

# 5. Reading Again After Append
with open("demo_file.txt", "r") as file:
    print("\n--- Updated File Content ---")
    print(file.read())

# 6. Writing a List of Lines
lines = ["Python is fun!\n", "Let's learn file handling.\n"]
with open("list_lines.txt", "w") as file:
    file.writelines(lines)

# 7. Using try-except for Safe File Access
try:
    with open("non_existing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("\nFile 'non_existing.txt' not found.")
