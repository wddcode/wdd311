class Animal:
    
    num_legs = 4
    awake = True
    age = None

    def make_noise(self):
        print 'making noise'

    def sleep(self):
        print 'ZzZzZzZzzzzZZzz'
        self.awake = False

    def wakeup(self):
        print 'Waking up!!'
        self.awake = True

    def celebrate_birthday(self):
        self.age += 1
        print "Happy Birthday %s !!" % self.__class__.__name__ 


class Dog(Animal):

    def bark(self):
        print 'WuffWuff'

    def make_noise(self):
        self.bark()

class Cat(Animal):

    def miau(self):
        print 'Miau!!'

    def make_noise(self):
        self.miau()


    

