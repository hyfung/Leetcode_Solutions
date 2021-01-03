class ParkingSystem {
public:
        int quota[4];
        int cur[4];
    ParkingSystem(int big, int medium, int small) {
        cur[1] = 0;
        cur[2] = 0;
        cur[3] = 0;
        quota[1] = big;
        quota[2] = medium;
        quota[3] = small;        
    }
    
    bool addCar(int carType) {
        if (cur[carType] < quota[carType])
        {
            cur[carType]++;
            return true;
        } else
        {
            return false;
        }
        
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
