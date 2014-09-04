import class.py

#Russell Patton
#
#
# Bicylce Industry model: creates a model bicycle industry by generating 
# manufacturers, bicycles, frames, wheels, customers, and stores

# Create 3 types of wheels
wheel_1 = BikeWheel("racing wheel", 1256, 23.20)
wheel_2 = BikeWheel("street wheel", 1406, 19.89)
wheel_3  = BikeWheel("all terrain wheel", 1602, 15.47)

# Create 3 types of frames
frame_1 = BikeFrame("aluminum", 5460, 69.27)
frame_2 = BikeFrame("carbon", 4873, 117.40)
frame_3 = BikeFrame("steel", 6026, 103.43)

# Create 6 types of bikes by combining frames and wheels
model_1 = BikeModel()
model_2 = BikeModel()
model_3 = BikeModel()
model_4 = BikeModel()
model_5 = BikeModel()
model_6 = BikeModel()

# Create 2 bicycle manufacturers
manufacturer_1 = BikeManufacturer("Yoshimitsu",placeholder,60)
manufacturer_2 = BikeManufacturer("Easy Rider",placeholder,30)

# Create Bicycle Shop
bikeshop = BikeShop(inventory, 20, "Mustache Rides")

# Create 3 customers
customer_1 = Customer("Benjamin Dover", 200)
customer_2 = Customer("Barney Stone", 500)
customer_3 = Customer("Isaac Hayes", 100)

# Print out bike shop
print "Welcome to %" bikeshop.name
print "We carry the following models:"
print model_1.name, model_1.cost
print model_2.name, model_2.cost
print model_3.name, model_3.cost
print model_4.name, model_4.cost
print model_5.name, model_5.cost
print model_6.name, model_6.cost

# Print out customers
print "The following customers arrived today, with the following budgets:"
print customer_1.name, customer_1.funds
print customer_2.name, customer_2.funds
