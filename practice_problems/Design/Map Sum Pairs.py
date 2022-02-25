class MapSum(object):
    # Brute Force
    # Time complexity Insert: O(1) Sum: O(N*P) where N is the number of items in the map, and P is the length of the input prefix
    def __init__(self):
        self.map = {}
    def insert(self,key,val):
        self.map[key] = val
    def sum(self,prefix):
        return sum(val for key,val in self.maps.items() if key.startswith(prefix))

