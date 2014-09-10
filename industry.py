import classes

#Russell Patton
#
#
# Bicylce Industry model: creates a model bicycle industry by generating 
# manufacturers, bicycles, frames, wheels, customers, and stores

# Create 3 types of wheels
wheel_1 = classes.BikeWheel("racing wheel", 1256, 23.20)
wheel_2 = classes.BikeWheel("street wheel", 1406, 19.89)
wheel_3  = classes.BikeWheel("all terrain wheel", 1602, 15.47)

# Create 3 types of frames
frame_1 = classes.BikeFrame("Cheapy D","aluminum", 5460, 69.27)
frame_2 = classes.BikeFrame("Doppleganger","carbon", 4873, 117.40)
frame_3 = classes.BikeFrame("NotManof","steel", 6026, 103.43)

# Create 6 types of bikes by combining frames and wheels
model_1 = classes.BikeModel("Sonic",wheel_1, frame_1,"Yoshimitsu")
model_2 = classes.BikeModel("Bikatana", wheel_3, frame_2, "Yoshimitsu")
model_3 = classes.BikeModel("Bikecyclops",wheel_2, frame_3, "Yoshimitsu")
model_4 = classes.BikeModel("Miss Daisy", wheel_2, frame_1, "Easy Rider")
model_5 = classes.BikeModel("Wheelie Cheech", wheel_1, frame_3, "Easy Rider")
model_6 = classes.BikeModel("Rocking Wheels", wheel_3, frame_2, "Easy Rider")

# Create 2 bicycle manufacturers
manufacturer_1 = classes.BikeManufacturer("Yoshimitsu",60)
manufacturer_2 = classes.BikeManufacturer("Easy Rider",30)

# Create Bicycle Shop
bikeshop = classes.BikeShop(20, "Mustache Rides")

# Create 3 customers
customer_1 = classes.Customer("Benjamin Dover", 200)
customer_2 = classes.Customer("Barney Stone", 500)
customer_3 = classes.Customer("Isaac Hayes", 1000)

# Print out bike shop
print "Welcome to %"
print "We carry the following models:"
print model_1.mname, model_1.prodcost
print model_2.mname, model_2.prodcost
print model_3.mname, model_3.prodcost
print model_4.mname, model_4.prodcost
print model_5.mname, model_5.prodcost
print model_6.mname, model_6.prodcost

# Print out customers
print "The following customers arrived today, with the following budgets:"
print customer_1.name, customer_1.funds
print customer_2.name, customer_2.funds
print customer_3.name, customer_3.funds

# Print out the manufacturers 
