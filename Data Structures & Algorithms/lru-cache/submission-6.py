class LRUCache:
    #intialise hashmap and capacity
    #perform the get operation, if pair is not in cache then return -1, if it is. remove and readd to show that it was 'used'
    # perform the put operation, if the key exists update it to be the most recently used, if it isnt add it to cache anyway. At the end aswell if the cache is bigger than the capacity we are given then pop from the left until we are within range

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        

    def get(self, key: int) -> int: #we must return an int
        if key not in self.cache:
            return -1 
        value = self.cache.pop(key)
        self.cache[key] = value 
        return value 
        

    def put(self, key: int, value: int) -> None: # we return nothing
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value 

        if len(self.cache) > self.capacity:
            lru = next(iter(self.cache))
            self.cache.pop(lru)
        




#for this problem we could only ever be 1 size over the capacity. So the if condition satisfies. If it didnt however then we could do the following. 
 #   while len(self.cache) > self.capacity:
  #      lru = next(iter(self.cache))
  #       del self.cache[lru]
        
