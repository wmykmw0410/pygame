class Counter():
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        if self.count > 0:
            self.count -= 1

    def reset(self):
        self.count = 0

    def show(self):
        print(f"count: {self.count}")


c = Counter()
c.increment()
c.increment()
c.increment()
c.show()       # count: 3

c.decrement()
c.show()       # count: 2

c.reset()
c.show()       # count: 0
