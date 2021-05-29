n = int(input())  # the number of temperatures to analyse
closest = None
# print(n)
if n != 0: 
    for i in input().split():
        # print(i)
        current = int(i)
        if current is None:
            print(0)
        else:
            if (closest is None or abs(closest) > abs(current) or (abs(closest) == abs(current) and closest < current)):
                    closest = current
    
    print(closest)
else: 
    print(0)
