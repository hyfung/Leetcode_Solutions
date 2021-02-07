class MyCircularQueue {
public:
    int k;
    std::vector<int> elements;
    
    MyCircularQueue(int k) {
        this-> k = k;
        this->elements.reserve(k);
    }
    
    bool enQueue(int value) {
        if (this->elements.size() < k)
        {
            this->elements.push_back(value);
            return true;
        }
        else
        {
            return false;
        }
    }
    
    bool deQueue() {
        if(this->elements.size() > 0)
        {
            this->elements.erase(this->elements.begin());
            return true;
        }
        else
        {
            return false;
        }
    }
    
    int Front() {
        if(this->elements.size() > 0)
        {
            return this->elements[0];
        }
        else
        {
            return -1;
        }
    }
    
    int Rear() {
        if(this->elements.size() > 0)
        {
            return this->elements[this->elements.size()-1];
        }
        else
        {
            return -1;
        }        
    }
    
    bool isEmpty() {
        return this->elements.size() == 0;
        
    }
    
    bool isFull() {
        return this->elements.size() == this->k;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
