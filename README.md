# Python OOP Assignment: A Complete Solution

This repository contains a complete solution for an **Object-Oriented Programming (OOP)** assignment in Python.  
The code is divided into two main sections, each demonstrating a core OOP concept: **class design** and **polymorphism**.

---

## 📂 Project Structure

The project consists of a single Python file:

- `week_5.py` → contains all the necessary classes and the main program to demonstrate their functionality.

---

## 📝 Assignment 1: Designing Your Own Class

This section focuses on designing and implementing a custom class from scratch.

### 🔹 The Smartphone Class

The `Smartphone` class is a blueprint for creating smartphone objects. It encapsulates a number of attributes and behaviors, making the code more organized and easier to manage.

#### Key Features:
- **`__init__` (Constructor):** Initializes a new smartphone object with a brand, model, and storage size.  
  It also sets default values for `battery_percentage`, `is_on` status, and an empty list of `apps_installed`.
- **Methods:**  
  - `power_on()`: Turns the phone on and reduces the battery by 1%.  
  - `power_off()`: Turns the phone off.  
  - `install_app(app_name, app_size)`: Installs a new application, checking if there is enough storage available.  
  - `check_battery()`: Displays the current battery level.  
  - `get_info()`: Prints a detailed summary of the smartphone's status, including used storage and installed apps.  

---

## 📝 Activity 2: Polymorphism Challenge

This section demonstrates **polymorphism**, a fundamental concept in OOP where objects of different classes can be treated through a common interface.

### 🔹 The move() Method

The challenge is solved by defining a `move()` method in several different classes:

- **Animal (Base Class):** An empty `move()` method is defined here to be overridden by its subclasses.  
- **Subclasses (Dog, Fish, Bird):** These classes inherit from `Animal` and provide their own unique implementation of the `move()` method.  
- **Unrelated Classes (Car, Plane):** These classes also define a `move()` method, but without inheriting from `Animal`.  

By placing instances of all these classes into a single list, we can iterate through them and call the same `move()` method on each object.  
Python then automatically calls the correct `move()` implementation for each object, showcasing **polymorphism**.  

---

## 📌 Expected Output

```bash
python main.py


==================================================
ASSIGNMENT 1: SMARTPHONE CLASS DEMONSTRATION
==================================================

--- Testing My Phone ---
--- Apple iPhone 15 Info ---
Status: OFF
Battery: 85%
Storage: 0GB used of 128GB
Installed Apps: 0

Apple iPhone 15 is now ON
Successfully installed Instagram
Successfully installed Netflix
Battery: 83%

--- Testing Friend's Phone ---
--- Samsung Galaxy S24 Info ---
Status: OFF
Battery: 92%
Storage: 0GB used of 256GB
Installed Apps: 0

Samsung Galaxy S24 is now ON
Successfully installed TikTok
Successfully installed Spotify

--- Samsung Galaxy S24 Info ---
Status: ON
Battery: 91%
Storage: 7GB used of 256GB
Installed Apps: 2
  - TikTok (3GB)
  - Spotify (4GB)

==================================================
ACTIVITY 2: POLYMORPHISM DEMONSTRATION
==================================================

--- Polymorphism in Action ---
All objects using the same move() method with different behaviors:

🐕 Buddy is running and wagging its tail
🐠 Nemo is swimming gracefully underwater
🐦 Eagle is soaring through the air
🚗 Tesla Model 3 is driving on the road
✈️ Boeing 747 is flying through the sky

--- Individual Method Calls ---

Calling move() on Max:
🐕 Max is running and wagging its tail

Calling move() on Honda Civic:
🚗 Honda Civic is driving on the road

==================================================
ASSIGNMENT COMPLETED SUCCESSFULLY!
==================================================
