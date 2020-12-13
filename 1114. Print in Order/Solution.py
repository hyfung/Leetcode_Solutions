class Foo:
    def __init__(self):
        self.second_ready = False
        self.third_ready = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_ready = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.second_ready:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_ready = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.third_ready:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
