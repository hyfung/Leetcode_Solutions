class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.d = dict()
        self.CAP = dict()
        
        self.CAP[1] = big
        self.CAP[2] = medium
        self.CAP[3] = small
        self.d[1] = 0
        self.d[2] = 0
        self.d[3] = 0
        

    def addCar(self, carType: int) -> bool:
        if self.d[carType] <  self.CAP[carType]:
            self.d[carType] += 1
            return True
        else:
            return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
