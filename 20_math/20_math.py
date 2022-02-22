import math


print(f"The square root of 16 is {math.sqrt(16)}")

print(f"Pi is {math.pi}")

def Sum10th(data):
    sum = 0
    for i, d in enumerate(data):
        if(i % 10 == 0): sum = sum + d
    return sum

if __name__ == "__main__":
    d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    print(len(d))
    result = Sum10th(d)
    print(result)