# Create
person = {"name": "Sakib", "age": 18}
print(person)

# Read
print(person["name"])

# Update
person["age"] = 19
print(person)

# Delete
del person["age"]
print(person)

# Kesalahan umum
# print(person["address"])  # Akan menyebabkan KeyError