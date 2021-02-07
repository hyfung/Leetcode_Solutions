class CustomStack {
public:
    int max;
    std::vector<int> stack;
        
    CustomStack(int maxSize) {
        this->max = maxSize;
        this->stack.reserve(maxSize);
    }
    
    void push(int x) {
        if (this->stack.size() < this->max)
        {
            this->stack.push_back(x);
        }        
    }
    
    int pop() {
        if (this->stack.size() > 0)
        {
            int ret = this->stack[this->stack.size()-1];
            stack.pop_back();
            return ret;
        }
        else
        {
            return -1;
        }
    }
    
    void increment(int k, int val) {
        for(int i=0;i<k;i++)
        {
            if (i < this->stack.size())
            {
                this->stack[i] += val;
            }
            else
            {
                break;
            }
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
