# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:50:32 2019
Framework for my kivy convert app
@author: hanneke
"""

# All the modules needed to build the app
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

# This is everything that can be converted
all_foods = {}
with open("all_foods.txt","r") as foods:
    for line in foods.readlines():
        if not line.startswith("#"):
            name = line.split(",")[0]
            density= line.split(",")[1].rstrip()
            density = float(density)
            all_foods[name] = density

# All the conversions needed to calculate stuff
def converting(origin, weight):
    weight = float(weight)
    density = all_foods[origin]
    ml = round(density * weight, 2) # in ml
    teaspoon = round(ml/5, 2)
    tablespoon = round(ml/15, 2)
    cup = round(ml/240, 2)
    # to convert the amount of food in grams to various volumes
    answer = [ml, teaspoon, tablespoon, cup]
    return answer

# The app itself
class ConvertingWidget(BoxLayout):
    # To store the metric system
    new_value_ml = StringProperty()
    new_value_teaspoon = StringProperty()
    new_value_tablespoon = StringProperty()
    new_value_cup = StringProperty()
    current_value = 0
    food_type = ""
    all_foodnames = sorted(list(all_foods.keys()))
    
    # This part stores the user input
    def store_value(self, *args):
        if len(args[0]) > 0:
            self.current_value = float(args[0])
        else:
            self.current_value = 0  
    
    # This part chooses the unit from a dropdown menu
    def store_food_type(self, *args):
        self.food_type = args[0]

    # Upon pressing the convert button, this will convert the unit to the new one
    def convert(self):
        new_values = converting(self.food_type, self.current_value)
        self.new_value_ml = str(new_values[0]) + " mL"
        self.new_value_teaspoon = str(new_values[1]) + " tsp"
        self.new_value_tablespoon = str(new_values[2]) + " tbsp"
        self.new_value_cup = str(new_values[3]) + " cup"
        
class ConvertingApp(App):
    def build(self):
        return ConvertingWidget()

if __name__ == "__main__":
    ConvertingApp().run()