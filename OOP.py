#Assignment 1
#Base Class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery 

    def make_call(self, number):
        return f"Calling {number} from {self.model}..."

    def charge(self, amount):
        self.battery = min(100, self.battery + amount) 
        return f"Battery charged to {self.battery}%" 

    def __str__(self):
        return f"{self.brand} {self.model} (Battery: {self.battery}%)"  

#Inheritance + Encapsulation
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, gpu):
        super().__init__(brand, model, battery)             
        self.gpu = gpu 

    def play_game(self, game):
        if self.battery > 20:
            self.battery -= 20
            return f"Playing {game} on {self.model} with {self.gpu} GPU!"
        else:
            return "Battery too low to play games!"  

#Polymorphism
def __str__(self):
    return f"{self.brand} {self.model} (Gaming GPU: {self.gpu}, Battery: {self.battery}%)"

#Example    
phone1 = Smartphone("Samsung", "S23", "50")
phone2 = GamingPhone("Asus", "ROG 7", 80, "Adreno 740")

print(phone1)
print(phone1.make_call("0712345678"))
print(phone1.charge(30))

print("\n" + str(phone2))
print(phone2.play_game("Call of Duty"))
print(phone2.charge(10))


#Assignment 2
class Vehicle:
    def move(self):
        return "Moving..."

class Car(Vehicle):
    def move(self):
        return "Driving on the road"
    
class Plane(Vehicle):
    def move(self):   
        return "Flying in the sky"  

class Boat(Vehicle):
    def move(self):
        return "Sailing on water"

#Example
vehicles = [Car(), Plane(), Boat()] 

for v in vehicles:
    print(v.move())
