class AlgoHashTable:

    def __init___(self, size):
        self.size = size
        #create many mini lists within one big list
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key] 
        found_key = False
        #setting key to some other value
        
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value)
        else:

            bucket.append((key,value)) #append to take care of collision


    def get_val(self, key):
        

    #called when tried to print ht object
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(256)
print(hash_table)
