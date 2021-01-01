import threading

h_semaphore = threading.Semaphore(2)
o_semaphore = threading.Semaphore(1)

class H2O:
    def __init__(self):
        self.cnt = 0


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        h_semaphore.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        # Free oxygen thread
        self.cnt += 1
        if self.cnt == 2:
            o_semaphore.release()
            self.cnt = 0


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        o_semaphore.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        # Free hydrogen Thread
        h_semaphore.release()
        h_semaphore.release()
        
        
    thrA = threading.Thread(target=hydrogen)
    thrB = threading.Thread(target=oxygen)
    
    thrA.start()
    thrB.start()
    
    thrA.join()
    thrB.join()
