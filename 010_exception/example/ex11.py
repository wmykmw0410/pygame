"""Noneの使い方"""

water = ["水素", None, "水素"]

for i in range(len(water)):
    if water[i] is None:
        water[i] = "酸素"

print(water)