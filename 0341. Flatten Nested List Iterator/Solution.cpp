/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
public:
    int counter;
    vector<int> flattenedIntegers;
    
    vector<int> flatten(vector<NestedInteger> ls)
    {
        vector<int> ret;
        
        for (auto &element : ls)
        {
            if (element.isInteger())
            {
                ret.push_back(element.getInteger());
            }
            else
            {
                auto tmp = flatten(element.getList());
                ret.insert(ret.end(), tmp.begin(), tmp.end());
            }
        }
        return ret;
    }
    
    NestedIterator(vector<NestedInteger> &nestedList) {
        this->flattenedIntegers = flatten(nestedList);
    }
    
    int next() {
        int ret = this->flattenedIntegers[0];
        this->flattenedIntegers.erase(this->flattenedIntegers.begin());
        return ret;
        
    }
    
    bool hasNext() {
        return !this->flattenedIntegers.empty();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
