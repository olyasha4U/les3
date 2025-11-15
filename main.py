# створює ітератор
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
# ітерований об'єкт
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