class MyCircularDeque {
public:
    int k;
    std::vector<int> elements;
    
    /** Initialize your data structure here. Set the size of the deque to be k. */
    MyCircularDeque(int k) {
        this->k = k;
        this->elements.reserve(k);
    }
    
    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    bool insertFront(int value) {
        if (this->elements.size() < this->k)
        {
            this->elements.insert(elements.begin(), value);
            return true;
        }
        else
        {
            return false;
        }
    }
    
    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    bool insertLast(int value) {
        if (this->elements.size() < this->k)        
        {
            this->elements.push_back(value);
            return true;
        }
        else
        {
            return false;
        }
    }
    
    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    bool deleteFront() {
        if (this->elements.empty())
        {
            return false;
        }
        else
        {
            this->elements.erase(this->elements.begin());
            return true;
        }
    }
    
    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    bool deleteLast() {
        if (this->elements.empty())
        {
            return false;
        }
        else
        {
            this->elements.pop_back();
            return true;
        }        
    }
    
    /** Get the front item from the deque. */
    int getFront() {
        if (this->elements.empty())
        {
            return -1;
        }
        else
        {
            return this->elements[0];
        }
    }
    
    /** Get the last item from the deque. */
    int getRear() {
        if (this->elements.empty())
        {
            return -1;
        }
        else
        {
            return this->elements[this->elements.size()-1];
        }
    }
    
    /** Checks whether the circular deque is empty or not. */
    bool isEmpty() {
        return this->elements.empty();
    }
    
    /** Checks whether the circular deque is full or not. */
    bool isFull() {
        return this->elements.size() == this->k;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
