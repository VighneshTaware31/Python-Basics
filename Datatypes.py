# Numeric Types
integer_num = 42
float_num = 3.14
print("Integer:", integer_num, "| Type:", type(integer_num))
print("Float:", float_num, "| Type:", type(float_num))


# String
text = "Hello, Python!"
print("String:", text, "| Type:", type(text))

# Boolean
is_python_fun = True
print("Boolean:", is_python_fun, "| Type:", type(is_python_fun))

# None Type
nothing = None
print("None:", nothing, "| Type:", type(nothing))

# List
fruits = ["apple", "banana", "cherry"]
print("List:", fruits, "| Type:", type(fruits))

# Tuple
dimensions = (1920, 1080)
print("Tuple:", dimensions, "| Type:", type(dimensions))

# Set
unique_numbers = {1, 2, 3, 2}
print("Set:", unique_numbers, "| Type:", type(unique_numbers))

# Dictionary
student = {"name": "Vighnesh", "age": 21, "course": "Python"}
print("Dictionary:", student, "| Type:", type(student))

# Bytes
binary_data = bytes([65, 66, 67])
print("Bytes:", binary_data, "| Type:", type(binary_data))

# Bytearray
mutable_binary = bytearray([68, 69, 70])
print("Bytearray:", mutable_binary, "| Type:", type(mutable_binary))

# Range
range_obj = range(5)
print("Range:", list(range_obj), "| Type:", type(range_obj))

# Type Conversion
str_to_int = int("123")
float_to_int = int(9.8)
int_to_str = str(100)
print("String to Int:", str_to_int)
print("Float to Int:", float_to_int)
print("Int to String:", int_to_str)

# Dynamic Typing
var = 10
print("var =", var, "| Type:", type(var))
var = "Now I'm a string"
print("var =", var, "| Type:", type(var))
