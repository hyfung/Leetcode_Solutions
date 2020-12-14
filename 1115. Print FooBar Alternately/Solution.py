import threading

foo_lock = threading.Lock()
bar_lock = threading.Lock()

class FooBar:
    def __init__(self, n):
        self.n = n
        
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            foo_lock.acquire()
            printFoo()
            bar_lock.release()
            


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            bar_lock.acquire()
            printBar()
            foo_lock.release()

            
    thrFoo = threading.Thread(target=foo)
    thrBar = threading.Thread(target=bar)

    bar_lock.acquire()

    thrFoo.start()
    thrBar.start()

    thrFoo.join()
    thrBar.join()
