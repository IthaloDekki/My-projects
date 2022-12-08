x, y, z = map(int, input().split())
def ordem():
    global x
    global y
    global z
    if x < y and x < z:
        print(x)
    elif y < x and y < z:
        print(y)
    elif z < x and z < y:
        print(z)
    if (x > y and x < z) or (x < y and x > z):
        print(x)
    elif (y > x and y < z) or (y < x and y > z):
        print(y)
    elif (z > x and z < y) or (z < x and z > y):
        print(z)
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    elif z > x and z > y:
        print(z)
ordem()
print('')
print(x)
print(y)
print(z)

