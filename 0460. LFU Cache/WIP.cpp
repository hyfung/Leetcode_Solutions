#include <map>
#include <vector>

bool contains(std::map<int, int> &mymap, int value)
{
    if(mymap.find(value) != mymap.end())
        return true;
    return false;
}

class LFUCache {
public:

    std::map<int, int> store;
    std::map<int, int> use_count;
    std::map<int, int> last_use;
    int capacity, epoch;

    LFUCache(int capacity) {
        this->capacity = capacity;
        this->epoch = 0;
    }
    
    int get(int key) {
        this->epoch++;

        if(contains(this->store, key))
        {
            this->use_count[key]++;
            this->last_use[key] = this->epoch;
            return this->store[key];
        }
        else
        {
            return -1;
        }

    }
    
    void put(int key, int value) {
        if (this->capacity == 0)
            return;

        this->epoch++;

        if (contains(this->store, key))
        {
            this->store[key] = value;
            this->last_use[key] = this->epoch;
            this->use_count[key] += 1;
            return;
        }

        if (this->store.size() < this->capacity)
        {
            this->store[key] = value;
            this->last_use[key] = this->epoch;
            this->use_count[key] = 0;
            return;
        }

        int lowest_use_count = 2147483647;
        int lowest_use_count_key = 0;
        std::vector<int> lowest_use_count_keys;
        
        for (auto & [k,v] : this->use_count)
        {
            if (v < lowest_use_count)
            {
                lowest_use_count_keys.clear();
                lowest_use_count_keys.push_back(k);
                lowest_use_count = v;
            }
            if (v == lowest_use_count)
            {
                lowest_use_count_keys.push_back(k);
            }
        }

        if (lowest_use_count_keys.size() == 1)
        {
            // Single key to evict
            lowest_use_count_key = lowest_use_count_keys[0];
            
            auto itStore = this->store.find(lowest_use_count_key);
            this->store.erase(itStore);

            auto itLastUse = this->last_use.find(lowest_use_count_key);
            this->last_use.erase(itLastUse);

            auto itUseCount = this->use_count.find(lowest_use_count_key);
            this->use_count.erase(itUseCount);

            this->store[key] = value;
            this->last_use[key] = this->epoch;
            this->use_count[key] = 0;
            return;
        }
        else
        {
            //Multiple key to evict
            int lowest_last_use = 2147483647;
            int lowest_last_use_key = 0;
            for (auto & [k,v] : this->last_use)
            {
                if (v < lowest_last_use)
                {
                    lowest_last_use = v;
                    lowest_last_use_key = k;
                }
            }
            auto itStore = this->store.find(lowest_last_use_key);
            this->store.erase(itStore);

            auto itLastUse = this->last_use.find(lowest_last_use_key);
            this->last_use.erase(itLastUse);

            auto itUseCount = this->use_count.find(lowest_last_use_key);
            this->use_count.erase(itUseCount);

            this->store[key] = value;
            this->last_use[key] = this->epoch;
            this->use_count[key] = 0;
            return;

        }


    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
