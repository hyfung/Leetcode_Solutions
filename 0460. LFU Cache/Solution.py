class LFUCache:

    def __init__(self, capacity: int):
        self.store = dict()
        self.use_count = dict()
        self.last_use = dict()
        self.capacity = capacity
        self.epoch = 0
        

    def get(self, key: int) -> int:
        # Always increment epoch
        self.epoch += 1

        if key in self.store:
            self.use_count[key] += 1
            self.last_use[key] = self.epoch
            return self.store[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        self.epoch += 1

        # Update existing key
        if key in self.store:
            self.store[key] = value
            self.last_use[key] = self.epoch
            self.use_count[key] += 1
            return

        # Add new key without evicting
        if len(self.store) < self.capacity:
            self.store[key] = value
            self.last_use[key] = self.epoch
            self.use_count[key] = 0
            return

        # Add new key with evicting

        #Find key with lowest use count
        lowest_use_count = min([v for k,v in self.use_count.items()])

        lowest_use_count_keys = [k for k,v in self.use_count.items() if v == lowest_use_count]

        # Only has 1 evict candidate, so we evict that
        if len(lowest_use_count_keys) == 1:
            k = lowest_use_count_keys[0]
            del self.store[k]
            del self.use_count[k]
            del self.last_use[k]

            self.store[key] = value
            self.last_use[key] = self.epoch
            self.use_count[key] = 0
            return

        # We have more than 1 key to evict, check its last use stamp
        min_last_use = min([v for k,v in self.last_use.items() if k in lowest_use_count_keys])

        evict_target = [k for k,v in self.last_use.items() if v == min_last_use][0]

        del self.store[evict_target]
        del self.use_count[evict_target]
        del self.last_use[evict_target]

        self.store[key] = value
        self.last_use[key] = self.epoch
        self.use_count[key] = 0
        return

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
