class Car:
    def __init__(self, make, model, year, color):
        """
        Initializes a new Car instance.
        
        :param make: str - The make of the car
        :param model: str - The model of the car
        :param year: int - The year the car was made
        :param color: str - The color of the car
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    def start_engine(self):
        """
        Starts the car's engine.
        """
        if not self.is_running:
            self.is_running = True
            print(f"The {self.color} {self.year} {self.make} {self.model} engine has started.")
        else:
            print("The engine is already running.")

    def stop_engine(self):
        """
        Stops the car's engine.
        """
        if self.is_running:
            self.is_running = False
            print(f"The {self.color} {self.year} {self.make} {self.model} engine has stopped.")
        else:
            print("The engine is already off.")

    def honk(self):
        """
        Makes the car honk its horn.
        """
        print(f"The {self.color} {self.year} {self.make} {self.model} goes 'Beep Beep!'")

    def __str__(self):
        """
        Returns a string representation of the car.
        """
        return f"{self.color} {self.year} {self.make} {self.model}"


# Create instances of the Car class
car1 = Car("Toyota", "Corolla", 2021, "Blue")
car2 = Car("Ford", "Mustang", 1967, "Red")

# Demonstrate the functionality of the Car class
print(car1)
car1.start_engine()
car1.honk()
car1.stop_engine()

print(car2)
car2.start_engine()
car2.honk()
car2.stop_engine()
