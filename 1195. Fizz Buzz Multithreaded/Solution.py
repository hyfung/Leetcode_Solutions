import threading

barrier = threading.Barrier(4)

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        # self.barrier = threading.Barrier(4)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                # print('a')
                printFizz()
            barrier.wait()
    	
    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 5 == 0 and i % 3 != 0:
                # print('b')
                printBuzz()
            barrier.wait()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                  # print('c')
                printFizzBuzz()
            barrier.wait()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 != 0:
                  # print('d')
                printNumber(i)
            barrier.wait()
            
    thrA = threading.Thread(target=fizz, )
    thrB = threading.Thread(target=buzz, )
    thrC = threading.Thread(target=fizzbuzz, )
    thrD = threading.Thread(target=number, )
    
    thrA.start()
    thrB.start()
    thrC.start()
    thrD.start()
    
    thrA.join()
    thrB.join()
    thrC.join()
    thrD.join()
