class AlgoHashTable:

    def __init___(self, size):
        self.size = size
        #create many mini lists within one big list
        self.hash_table = [[] for _ in range(self.size)]

    def create_buckets(self):
        pass

    def set_val(self, key, value):
        pass

    def get_val(self, key):
        pass

    #called when tried to print ht object
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(256)
print(hash_table)
