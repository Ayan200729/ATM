class Car(object):
    def __init__(self, model, company, color, speedLimit):
       self.color = color
       self.model = model
       self.company = company
       self.speedLimit = speedLimit


    def start(self):
        print("started")

    def stop(self):
        print("stoped")

    def accelerate(self):
        print("accelerating...")
        "accleratorFunctionalityHere"

    
audi = Car("a6", "audi", "red", "200")

print(audi.company)