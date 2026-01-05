#polymorphism with classes and objects

class bird:
    def intro(self):
        print("There are many types of birds.")
    
    def flight(self):
        print("Most of the birds can fly but some cannot.")
class sparrow(bird):
    def flight(self):
        print("Sparrows can fly.")
class ostrich(bird):
    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = bird()
obj_sparrow = sparrow()
obj_ostrich = ostrich()
obj_bird.intro()
obj_bird.flight()
obj_sparrow.intro()
obj_sparrow.flight()
obj_ostrich.intro()
obj_ostrich.flight()
# Output:
# There are many types of birds.    