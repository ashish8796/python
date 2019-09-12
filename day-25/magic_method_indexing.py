# # MAGIC METHOD
# '''
# There are several magic methods fo rmaking classes act like containes.
# '''
# __len__  # for len()
# __getitem__  # for assigning to indexed values
# __delitem__  # for deleting indexed values
# __iter__  # for iteration over objects
# __contains__  # for in

# magic method for indexing and lenght  in a mutable type data structure

class VagueList:
    def __init__(self, cont):
        self.cont = cont
    
    def __getitem__(self, index):
        return self.cont[index]
    
    def __len__(self):
        return len(self.cont)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(vague_list[3])