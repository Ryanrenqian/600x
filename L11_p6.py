class queue(object):
    def __init__(self):
        self.vals=[]
        
    def insert(self,e):
        self.vals.append(e)
        
    def remove(self):
        if not self.vals[0] ==[]:
            e=self.vals[0]
            self.vals.remove(e)
            return e
        else:
            raise ValueError("")