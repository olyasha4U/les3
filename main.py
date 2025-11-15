# створює ітератор(нескінченний)
a = iter([1,2, 3,4, 5])

# отрмати наступний елемент
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
try:
    print(next(a))
except:
    print("Error")
# ітерований об'єкт (який повторюється, скінчений)
class Counter:
    def __init__(self):
        self.a = 1

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        self.a *= 2
        return self.a

c = iter(Counter())
for i in range(50):
    print(next(c))

#генератори
def gen(number):
    b = number
    i = 0
    while True:
        i += 1
        b += 1
        yield b
g =gen(5)
print(next(g))
print(next(g))
print(next(g))
#декоратори
def dec(f1):
    def f2():
        result=f1()
        return f"Result:{result}"
    return f2
@dec
def test():
    return "Test"
print(test())