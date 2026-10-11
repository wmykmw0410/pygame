"""__init__.py のエクスポートを使うパターン"""
from shapes import circle_area, circle_perimeter, rectangle_area, rectangle_perimeter

print(circle_area(5))          # 78.539...
print(circle_perimeter(5))     # 31.415...
print(rectangle_area(4, 6))    # 24
print(rectangle_perimeter(4, 6)) # 20
