####################################################################
###
### Author: Jose Moran 
### Email : jmoran071996@gmail.com
### Github: jose0796
### Description: Hash table implementation using chaining resolution
### for solving collisions. 
###
####################################################################

class htable:

    def __init__(self):
        self.size = 0
        self.cont = [[] for _ in range(100)]
        self.keys = list()

    def hash(self,key):
        return ((hash(key)*23092 + 43734*hash(key)) << 27)% 100
    
    def __setitem__(self,key,val):

        
        hval = self.hash(key)
        if key not in self.keys:
            self.cont[hval].append((key,val))
            self.keys.append(key)
    
    def __getitem__(self,key):

        for el in self.cont[self.hash(key)]:
            if key == el[0]:
                return el[1]
        return -1

    def keyset(self):
        return self.keys

    def __str__(self):
        s = ""
        for key in self.keys:
            s += str(self.hash(key)) + " : " + str(self.cont[self.hash(key)]) + "\n"
        return s
