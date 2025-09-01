# OOP Assignment - Complete Solution

# ==========================================
# Assignment 1: Design Your Own Class
# ==========================================

class Smartphone:
    """A class representing a smartphone with various attributes and methods."""
    
    def __init__(self, brand, model, storage, battery_percentage=100):
        """Initialize a smartphone with brand, model, storage, and battery."""
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_percentage = battery_percentage
        self.is_on = False
        self.apps_installed = []
    
    def power_on(self):
        """Turn on the smartphone."""
        if not self.is_on:
            self.is_on = True
            self.battery_percentage -= 1
            print(f"{self.brand} {self.model} is now ON")
        else:
            print(f"{self.brand} {self.model} is already on")
    
    def power_off(self):
        """Turn off the smartphone."""
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF")
        else:
            print(f"{self.brand} {self.model} is already off")
    
    def install_app(self, app_name, app_size):
        """Install an app if there's enough storage."""
        used_storage = sum(app['size'] for app in self.apps_installed)
        if used_storage + app_size <= self.storage:
            self.apps_installed.append({'name': app_name, 'size': app_size})
            print(f"Successfully installed {app_name}")
        else:
            print(f"Not enough storage to install {app_name}")
    
    def check_battery(self):
        """Check and display current battery percentage."""
        print(f"Battery: {self.battery_percentage}%")
        return self.battery_percentage
    
    def get_info(self):
        """Display complete information about the smartphone."""
        used_storage = sum(app['size'] for app in self.apps_installed)
        status = "ON" if self.is_on else "OFF"
        
        print(f"\n--- {self.brand} {self.model} Info ---")
        print(f"Status: {status}")
        print(f"Battery: {self.battery_percentage}%")
        print(f"Storage: {used_storage}GB used of {self.storage}GB")
        print(f"Installed Apps: {len(self.apps_installed)}")
        for app in self.apps_installed:
            print(f"  - {app['name']} ({app['size']}GB)")


# ==========================================
# Activity 2: Polymorphism Challenge
# ==========================================

class Animal:
    """Base class for all animals."""
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """Base move method - to be overridden by subclasses."""
        pass


class Car:
    """Car class that also has a move method for polymorphism."""
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """Car's implementation of move."""
        print(f"🚗 {self.name} is driving on the road")


class Plane:
    """Plane class that also has a move method for polymorphism."""
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """Plane's implementation of move."""
        print(f"✈️ {self.name} is flying through the sky")


class Dog(Animal):
    """Dog class inheriting from Animal."""
    
    def move(self):
        """Dog's implementation of move."""
        print(f"🐕 {self.name} is running and wagging its tail")


class Fish(Animal):
    """Fish class inheriting from Animal."""
    
    def move(self):
        """Fish's implementation of move."""
        print(f"🐠 {self.name} is swimming gracefully underwater")


class Bird(Animal):
    """Bird class inheriting from Animal."""
    
    def move(self):
        """Bird's implementation of move."""
        print(f"🐦 {self.name} is soaring through the air")


# ==========================================
# Main Program - Testing Everything
# ==========================================

def main():
    print("=" * 50)
    print("ASSIGNMENT 1: SMARTPHONE CLASS DEMONSTRATION")
    print("=" * 50)
    
    # Create smartphone instances
    my_phone = Smartphone("Apple", "iPhone 15", 128, 85)
    friend_phone = Smartphone("Samsung", "Galaxy S24", 256, 92)
    
    # Test smartphone methods
    print("\n--- Testing My Phone ---")
    my_phone.get_info()
    my_phone.power_on()
    my_phone.install_app("Instagram", 2)
    my_phone.install_app("Netflix", 5)
    my_phone.check_battery()
    
    print("\n--- Testing Friend's Phone ---")
    friend_phone.get_info()
    friend_phone.power_on()
    friend_phone.install_app("TikTok", 3)
    friend_phone.install_app("Spotify", 4)
    friend_phone.get_info()
    
    print("\n" + "=" * 50)
    print("ACTIVITY 2: POLYMORPHISM DEMONSTRATION")
    print("=" * 50)
    
    # Create instances of different classes
    moving_objects = [
        Dog("Buddy"),
        Fish("Nemo"), 
        Bird("Eagle"),
        Car("Tesla Model 3"),
        Plane("Boeing 747")
    ]
    
    print("\n--- Polymorphism in Action ---")
    print("All objects using the same move() method with different behaviors:\n")
    
    # Demonstrate polymorphism - same method call, different behaviors
    for obj in moving_objects:
        obj.move()
    
    print("\n--- Individual Method Calls ---")
    # You can also call move() on individual objects
    dog = Dog("Max")
    car = Car("Honda Civic")
    
    print(f"\nCalling move() on {dog.name}:")
    dog.move()
    
    print(f"\nCalling move() on {car.name}:")
    car.move()
    
    print("\n" + "=" * 50)
    print("ASSIGNMENT COMPLETED SUCCESSFULLY!")
    print("=" * 50)


# Run the main program
if __name__ == "__main__":
    main()