# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 22:10:50 2025
@author: Hamid

Zoo Management System
=====================
Problem Description:
A zoo wants to create an animal management system.
Using Object-Oriented Programming (OOP) in Python, design this system.

-----------------------------------------------------
1. OOP Introduction
Task:
Define a class named 'Animal' with the following attributes:
    - name
    - species
    - age
    - sound
Then, create an instance of this class for a "lion" and print its details.
-----------------------------------------------------
2. Attributes and Class Keyword
Task:
Add a method make_sound() to the Animal class to print the animal's sound.
-----------------------------------------------------
3. Class Object Attributes and Methods
Task:
Add a class attribute (zoo_name) representing the zoo name.
Also, define an info() method to print animal details.
-----------------------------------------------------
4. Inheritance and Polymorphism
Task:
Create a new class 'Bird' inheriting from Animal with an additional
attribute wing_span, and override make_sound() for bird-specific behavior.
-----------------------------------------------------
5. Magic/Dunder Methods
Task:
Implement the __str__ method in Animal so that printing an object
shows the animal's details.
-----------------------------------------------------
"""

# =====================================================
# 1. OOP Introduction
# =====================================================
class Animal:
    """Base class representing an animal."""

    # 3. Class Object Attributes and Methods
    zoo_name = "Private Zoo"

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    # 2. Attributes and Class Keyword
    def make_sound(self):
        """Make the animal's sound."""
        print(f"{self.name} is {self.sound}ing.")

    # 3. Class Object Attributes and Methods
    def info(self):
        """Display animal's information."""
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Sound: {self.sound}")

    # 5. Magic / Dunder Methods
    def __str__(self):
        """Return a string representation of the animal."""
        return f"{self.name} ({self.species}) - Age: {self.age}, Sound: {self.sound}"


# Example instance
animal_1 = Animal("Lion", "Mammal", 12, "roar")

# Display attributes
print(animal_1.name)
print(animal_1.age)
print(animal_1.sound)

# Change class attribute for this instance
animal_1.zoo_name = "Central Zoo"
print(animal_1.zoo_name)

# Call methods
animal_1.make_sound()
animal_1.info()


# =====================================================
# 4. Inheritance and Polymorphism
# =====================================================
class Bird(Animal):
    """Subclass representing a bird (inherits from Animal)."""

    def __init__(self, wing_span, name, species, age, sound):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span  # additional attribute

    # Override make_sound method
    def make_sound(self):
        """Birds make sound differently (polymorphism example)."""
        print(f"{self.name} is {self.sound}ing in the sky with a wingspan of {self.wing_span} meters.")


# Create a Bird instance
bird_1 = Bird(2, "Sparrow", "Bird", 1, "chirp")

# Demonstrate overridden method
bird_1.make_sound()

# Display string representation (__str__)
print(animal_1)
