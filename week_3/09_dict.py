
class Dict:
    def __init__(self):
        self.item = [None] * 8

    def put(self, key, value):
        self.item[hash(key) % 8] = value

    def get(self, key):
        return self.item[hash(key) % 8]

my_dict = Dict()
my_dict.put("Jiwon", 7)
print(my_dict.get("Jiwon"))