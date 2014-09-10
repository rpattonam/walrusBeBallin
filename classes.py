# Author: Russell Patton
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
    def __init__(self, name,fmaterial, fweight, fcost):
        self.name = name
        self.fmaterial = fmaterial
        self.fweight = fweight
        self.fcost = fcost


class BikeModel(object):
    """Assemble Bike Frame"""
    def __init__(self,mname,wheel,frame, manufacturer):
        self.bikeweight = wheel.weight * 2 + frame.fweight
        self.prodcost = wheel.cost * 2 + frame.fcost
        self.mname =mname
        self.manufacturer = manufacturer


class BikeManufacturer(object):
    """Create a Manufacturer"""
    def __init__(self, name, profit):
        self.name = name
        self.profit = profit
       
            

class BikeShop(object):
    """Create a bike shop"""
    def __init__(self, margin, name):
        self.margin = margin
        self.name = name


class Customer(object):
    """Create a customer"""
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
