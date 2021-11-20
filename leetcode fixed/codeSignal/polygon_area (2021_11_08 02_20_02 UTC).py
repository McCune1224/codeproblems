# 1 -> 1
# 2 -> 5
# 3 -> 13
# 4 -> 25
def shapeArea(n):
    if n == 1:
        return n
    
    area = 1
    for x in range(1, n+1):
        print(f"A = {area} | x = {x} | x-1*4 = {4*(x-1)}")
        area = area + (4*(x-1))   
        print(area)   

shapeArea(int(input("n:")))
