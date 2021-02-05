#include <map>
#include <vector>

struct entry
{
    int iValue = 0;
    int iUsed = 0;
    int iLastUsed = 0;
};

class LFUCache {
public:
    std::map<int, struct entry> cache;
    int iCapacity;
    int iEpoch;
    
    LFUCache(int capacity) {
        this->iCapacity = capacity;
        this->iEpoch = 0;
    }
    
    int get(int key) {
        this->iEpoch++;
        if(this->cache.find(key) != this->cache.end())
        {
            this->cache[key].iUsed++;
            this->cache[key].iLastUsed = this->iEpoch;
            return this->cache[key].iValue;
        }
        else
        {
            return -1;
        }
    }
    
    void put(int key, int value) {
        this->iEpoch++;
        // Check if the key already exists in our cache
        // Just renew the cache entry if so
        if (this->cache.find(key) != this->cache.end())
        {
            this->cache[key].iValue = value;
            this->cache[key].iLastUsed = this->iEpoch;
            return;
        }

        // The key does not exist, check if we have enough space 
        if (this->cache.size() < this->iCapacity)
        {
            this->cache[key].iValue = value;
            this->cache[key].iLastUsed = this->iEpoch;
            this->cache[key].iUsed = 0;
            return;
        }

        // We need to evict an old key

        std::vector<int> iEvictCandidatesKey;
        int iLeastUsed = 2147483647;

        // Create a list of candidate keys to be evicted
        for (auto & [k, v] : this->cache)
        {
            // Item with lesser use count found, flush our candidate
            if (v.iUsed < iLeastUsed)
            {
                // Flush our candidate
                iEvictCandidatesKey.clear();

                //Update new counter
                iLeastUsed = v.iUsed;
                iEvictCandidatesKey.push_back(k);
            }

            // Item is within our least used count so add to candidate
            if (v.iUsed == iLeastUsed)
            {
                iEvictCandidatesKey.push_back(k);
            }
        }

        if (iEvictCandidatesKey.size() == 1)
        {
            // We only has 1 key to evict
            auto it = this->cache.find(iEvictCandidatesKey[0]);
            this->cache.erase(it);

            this->cache[key].iValue = value;
            this->cache[key].iLastUsed = this->iEpoch;
            this->cache[key].iUsed = 0;
            return;
        }
        else
        {
            int iRecentUsed = 2147483647;
            int iEvictTarget;
            for (auto &k : iEvictCandidatesKey)
            {
                if (this->cache[k].iLastUsed < iRecentUsed)
                {
                    iEvictTarget = k;
                    iRecentUsed = this->cache[k].iLastUsed;
                }
            }

            auto it = this->cache.find(iRecentUsed);
            this->cache.erase(it);

            this->cache[key].iValue = value;
            this->cache[key].iLastUsed = this->iEpoch;
            this->cache[key].iUsed = 0;
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
