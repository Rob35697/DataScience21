#define new class
class ListKeeper:
    #initialize with default dictionary
    def __init__(self):
        self.listkeeperdict = {
            'names':['example'],
            'list':[[1,2,3,4,5]]
        }
        
    #return all names from list
    def show(self):
        return self.listkeeperdict["names"]
    
    #add a new list
    def add(self,name,list):
        self.listkeeperdict["names"].append(name)
        self.listkeeperdict["list"].append(list)
        
    #delete list
    def delete(self,name):
        position = self.listkeeperdict["names"].index(name)
        self.listkeeperdict["names"].pop(position)
        self.listkeeperdict["list"].pop(position)
                                       
    #return the sorted list
    def sort(self,name):
        position = self.listkeeperdict["names"].index(name)
        self.listkeeperdict["list"][position].sort()
        return self.listkeeperdict["list"][position]
    
    #append list
    def append(self,name,list):
        position = self.listkeeperdict["names"].index(name)
        self.listkeeperdict["list"][position].extend(list)