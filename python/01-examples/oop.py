

class Animal:
    

    def __init__(self, num_legs=None):
        
        if num_legs:
            self.num_legs = num_legs
    
    awake = True
    
    def sleep(self):
        print 'ZzZzzzzZZZzzZzz...'
        self.awake = False
        
    def wakeup(self):
        print 'Wakeing uPP'
        self.awake = True
        
    def make_noise(self):
        print "making NOISE!!"
        
        
        
class Dog(Animal):
    
    def make_noise(self):
        print "WuffWuff"
        