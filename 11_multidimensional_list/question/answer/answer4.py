"""よく使うメソッド 解答"""

fruits = ["banana", "apple", "cherry"]
fruits.sort()
print(fruits)           # ['apple', 'banana', 'cherry']

fruits.append("mango")
print(fruits)           # ['apple', 'banana', 'cherry', 'mango']

fruits.remove("apple")
print(fruits)           # ['banana', 'cherry', 'mango']

print("grape" in fruits)  # False
