import threading
barrier = threading.Barrier(3)
zero_lock = threading.Lock()
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:

        for i in range(1, self.n + 1):
            printNumber(0)
            zero_lock.release()
            barrier.wait()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        
        for i in range(1, self.n + 1):
            if i % 2 == 0 and i != 0:
                zero_lock.acquire()
                printNumber(i)
            barrier.wait()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 1:
                zero_lock.acquire()
                printNumber(i)
            barrier.wait()
        
    thrA = threading.Thread(target=zero, )
    thrB = threading.Thread(target=even, )
    thrC = threading.Thread(target=odd, )
            
    zero_lock.acquire()
    
    
    thrA.start()
    thrB.start()
    thrC.start()
    
    thrA.join()
    thrB.join()
    thrC.join()
