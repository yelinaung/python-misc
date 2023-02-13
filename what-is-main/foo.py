print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print(f"Function B {math.sqrt(100)}")

print("before __name__")

if __name__ == '__main__':
    functionA()
    functionB()

print("after __name__")
