# Author: Russell Patton
#
# 
# Classes for bicycle industry model



class BikeWheel(object):
    """Create Bicycle Wheels"""
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost =  cost

class BikeFrame(object):
    """Create Bicycle Frames"""
    def __init__(self, name):
        self.name = name

    def build_frame(self, fmaterial, fweight, fcost):
        self.fmaterial = fmaterial
        self.fweight = fweight
        self.fcost = fcost

class BikeModel(object):
    """Assemble Bike Frame"""
    def __init__(self,name, manufacturer)
        bikeweight = wheel.weight * 2 + frame.fweight
        prodcost = wheel.cost * 2 + frame.fcost
        self.name = name
        self.manufacturer = manufacturer

class BikeManufacturer(object):
    """Create a Manufacturer"""
    def __init__(self, name, models, profit)
        self.name = name
        self.models = models
        self.profit = profit

class BikeShop(object):
    """Create a bike shop"""
    def __init__(self, inventory, margin, name)
        self.inventory = inventory
        self.margin = margin
        self.name = name

class Customer(object):
    """Create a customer"""
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
