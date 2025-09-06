# Define a simple class
class Car:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method to display car info
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Create objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model 3")

# Access object attributes
print("Car 1 brand:", car1.brand)
print("Car 2 model:", car2.model)

# Call methods
car1.display_info()
car2.display_info()
