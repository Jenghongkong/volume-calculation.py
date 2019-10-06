import math

print("This program calculate [straigh cylinder, straight pyramid, straight cone, sphere]")

class straight_cylinder():
    def volume(r,high):
        volume = math.pi * r**2 * high
        return volume
    def r(volume,high):
        r = math.sqrt(math.pi * volume * high)
        return r
    def high(volume,r):
        high = volume/math.pi/r**2
        return high

class straight_pyramid():
    def volume(side1,side2,high):
        volume = side1 * side2 / 3 * high
        return volume
    def total_side(volume,high):
        total_side = (volume * 3) / high
        return total_side
    def high(volume,total_side):
        high = (volume * 3) / total_side
        return high

class straight_cone():
    def volume(r, high):
        volume = math.pi * r**2 * high / 3
        return volume

    def r(volume, high):
        r = math.sqrt((volume * 3) / (math.pi * h))
        return r

    def high(volume, r):
        high = (v * 3) / (math.pi * r**2)
        return high

class sphere():
    def volume(r):
        volume = math.pi * r**3 * 4 /3
        return volume
    def r(volume):
        r = ((v*3) / (4 * math.pi)) **(1./3.)
        return r


a = input("type: ")
b = input("which?: ")


if a == "straight cylinder":
    if b == "volume":
        r = int(input("r: "))
        high = int(input("high: "))
        print(float(straight_cylinder.volume(r,high)))
    elif b == "r":
        volume = int(input("volume: "))
        high = int(input("high: "))
        print(float(straight_cylinder.r(volume,high)))
    elif b == "high":
        volume = int(input("volume: "))
        r = int(input("r: "))
        print(float(straight_cylinder.high(volume,r)))
    else:
        print("Error")

elif a == "straight pyramid":
    if b == "volume":
        side1 = int(input("side1: "))
        side2 = int(input("side2: "))
        high = int(input("high: "))
        print(float(straight_pyramid.volume(side1,side2,high)))
    elif b == "total side":
        volume = int(input("volume: "))
        high = int(input("high: "))
        print(float(straight_pyramid.total_side(volume,high)))
    elif b == "high":
        volume = int(input("volume: "))
        total_side = int(input("total side: "))
        print(float(straight_pyramid.high(volume,total_side)))
    else:
        print("Error")

elif a == "straight cone":
    if b == "volume":
        r = int(input("r: "))
        high = int(input("high: "))
        print(float(straight_cone.volume(r,high)))
    elif b == "r":
        volume = int(input("volume: "))
        high = int(input("high: "))
        print(float(straight_cone.r(volume,high)))
    elif b == "high":
        volume = int(input("volume: "))
        r = int(input("r: "))
        print(float(straight_cone.high(volume,r)))
    else:
        print("Error")

elif a == "sphere":
    if b == "volume":
        r = int(input("r: "))
        print(float(sphere.volume(r)))
    elif b == "r":
        volume = int(input("volume: "))
        print(float(sphere.r(volume)))
    else:
        print("Error")

























