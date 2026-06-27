"""
== : 値が等しいかどうかを比較
オブジェクトの中身(値)が同じであればTrue
"""

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True（値が同じ）


"""
is : オブジェクトが同一かどうかを比較
オブジェクトのID（メモリ上の場所）が同じであればTrue
"""
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False（同じリストではなく、値が同じだけ）

print(f"aのIDは{id(a)}")
print(f"bのIDは{id(b)}")

c = a
print(a is c)  # True（aとcは同じオブジェクトを指している）

print(f"aのIDは{id(a)}")
print(f"cのIDは{id(c)}")

