# 1. Creating a Dictionary
person = {"name": "Vighnesh", 
          "age": 21, 
          "city": "Pune"}

# 2. Accessing Values
print("Name:", person["name"])

# 3. Using get() Method
print("Course:", person.get("course", "Not Enrolled"))

# 4. Adding a New Key-Value Pair
person["course"] = "Python Programming"
print("Updated Dictionary:", person)

# 5. Updating Existing Value
person["age"] = 22
print("Updated Age:", person)

# 6. Removing a Key using pop()
person.pop("city")
print("After Removing 'city':", person)

# 7. Checking Key Existence
print("Is 'name' in dictionary?", "name" in person)

# 8. Looping Through Dictionary Keys and Values
for key, value in person.items():
    print(f"{key}: {value}")

# 9. Nested Dictionary
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 21}
}
print("Student 2 Name:", students["student2"]["name"])

# 10. Dictionary from List of Tuples
pairs = [("brand", "Nike"), ("size", 9)]
shoes = dict(pairs)
print("Shoes Dictionary:", shoes)
