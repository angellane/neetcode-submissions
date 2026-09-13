class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =  capacity 
        self.cache = {}
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value 
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value

        if len(self.cache)>self.capacity:
            lru = next(iter(self.cache)) #lru = list(cache)[0], this would work too but we would have to scan through all of the cache map and add everything to the list, O(n) time and more memory is being used when we make the list 
            del self.cache[lru] #self.cache.pop(lru) works here also but the difference is that when you pop it you return the value and when you delete it you dont 

    #both the put and get functions pop the key value pair from the hashmap and readd it to the end as that pair has been 'used'