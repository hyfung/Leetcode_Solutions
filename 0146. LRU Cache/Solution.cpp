#include <map>

struct entry
{
    int value;
    int lastUsed;
};

class LRUCache {
public:
    int capacity;
    int epoch;
    std::map<int, entry> cache;
    
    LRUCache(int capacity) {
        this->capacity = capacity;
        this->epoch = 0;
    }
    
    int get(int key) {
        this->epoch++;
        // cout << "Get key: " << key << " = ";
        if (this->cache.find(key) != this->cache.end())
        {
            this->cache[key].lastUsed = this->epoch;
            // cout << this->cache[key].value << endl;
            return this->cache[key].value;
        }
        else
        {
            // cout << "Not found" << endl;
            return -1;
        }
    }
    
    void put(int key, int value) {
        this->epoch++;
        // cout << "Put key: " << key << ":" << value << endl;
        if (this->cache.size() < this->capacity)
        {
            this->cache[key] = (struct entry){value, epoch};
        }
        else
        {
            if (this->cache.find(key) != this->cache.end())
            {
                this->cache[key].value = value;
                this->cache[key].lastUsed = this->epoch;
                return;
            }

            int lowest_key;
            int lowest_epoch = 2147483647;
            for (auto [cKey, cEntry] : this->cache)
            {
                // cout << cKey << ":" << cEntry.lastUsed << ",";
                if (cEntry.lastUsed < lowest_epoch)
                {
                    lowest_key = cKey;
                    lowest_epoch = cEntry.lastUsed;
                }
            }

            // cout << endl;

            // cout << "Evicted key: " << lowest_key << endl;

            auto it = this->cache.find(lowest_key);
            this->cache.erase(it);

            this->cache[key] = (struct entry){value, epoch};

        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
