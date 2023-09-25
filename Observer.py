# Overall, this code demonstrates object-oriented principles in Python,
# particularly inheritance and polymorphism,
# by defining classes for different types of bells and a bell ringer that can manage and ring these bells.
# When you run the script, it will output messages indicating that the bells have been rung.

class IRingBell():
    # It serves as a template for classes that want to implement the ringbell method.
    def ringbell(self):
        pass

class RingBigBell(IRingBell):
    # This class inherits from IRingBell and overrides the ringbell method to print "Ring big bell, BOING" when called.
    def ringbell(self):
        print('Ring big bell, BOING')

class RingSmallBell(IRingBell):
    # This class also inherits from IRingBell and overrides the ringbell method to print "Ring small bell, Ding" when called.
    def ringbell(self):
        print('Ring small bell, Ding')

class BellRinger():
    # This class is a bell ringer that can manage a list of bells.
    # The __init__ method initializes an empty list self.belllist for storing bells.
    def __init__(self):
        self.belllist = []
    
    def addbell(self, bell):
    # The addbell(self, bell) method takes a bell as a parameter and adds it to the belllist if it is an instance of IRingBell.
        if isinstance (bell,IRingBell):
            self.belllist.append(bell)

    def ringbells(self):
    # The ringbells(self) method iterates through the belllist and calls the ringbell method on each bell, effectively ringing all the added bells.
        for bell in self.belllist:
            bell.ringbell()

def main():
# This is the main function where the demonstration of the bell ringing is performed.
    big_bell_a = RingBigBell()
    big_bell_b = RingBigBell()
    small_bell_a = RingBigBell()
    small_bell_b = RingBigBell()
    
    bellringer = BellRinger()
    bellringer.addbell(big_bell_a)
    bellringer.addbell(big_bell_b)
    bellringer.addbell(small_bell_a)
    bellringer.addbell(small_bell_b)

    bellringer.ringbells()

if __name__ == "__main__":
# to ensure that the main() function is executed only if the script is run directly and not when it's imported as a module.
    main()