import hashlib

x = 1
y = 3.14
z = True
name = "Python"
numbers = [1, 2, 3]
coordinates = (10, 20)
unique_numbers = {1, 2, 3}
person = {"name": "Anton", "age": 28}

report = (
    f"x = {x}, type = {type(x)}\n"
    f"y = {y}, type = {type(y)}\n"
    f"z = {z}, type = {type(z)}\n"
    f"name = {name}, type = {type(name)}\n"
    f"numbers = {numbers}, type = {type(numbers)}\n"
    f"coordinates = {coordinates}, type = {type(coordinates)}\n"
    f"unique_numbers = {unique_numbers}, type = {type(unique_numbers)}\n"
    f"person = {person}, type = {type(person)}\n"
    f"ФИО: Щербинин Антон Владимирович"
)


report_bytes = report.encode("utf-8")
md5_hash = hashlib.md5(report_bytes).hexdigest() 
sha256_hash = hashlib.sha256(report_bytes).hexdigest()

print(report)
print()
print("MD5:", md5_hash)
print("SHA-256:", sha256_hash)
