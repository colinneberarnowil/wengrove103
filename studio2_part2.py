######################################################################
# Program Filename: studio2_part2
# Author: Colin Wilson
# Date: 4/7/22
# Description: calculating gallons used and fuel costs of various cars
# Input: car type (with MPG or MPGe), cost of gas/electricity
# Output: the description above
#######################################################################

miles = 14032 #annual mileage per person, per the FHWA data for Oregon drivers

low_cost_of_gas = 4.72 #dollars per gallon
high_cost_of_gas = 5.92 #dollars per gallon
low_cost_of_power = 0.1116 #price per kWh at home
high_cost_of_power = 0.30 #price per kWh at public chargers

# listing MPG's
sedan = 30
sedan_hybrid = 45
suv = 20
suv_hybrid = 30

# listing MPGe's
tesla = 126
bolt = 108

sedan_gals = miles//sedan
sedan_low_cost = sedan_gals*low_cost_of_gas//1
sedan_high_cost = sedan_gals*high_cost_of_gas//1

print("Sedan drivers in Oregon use about", sedan_gals,"gallons of gas in a year.")
print("It costs them about $", sedan_low_cost, "when gas is cheap, and $", sedan_high_cost,"when gas is spendy.")

sedan_hybrid_gals = miles//sedan_hybrid
sedan_hybrid_low_cost = (sedan_hybrid_gals*low_cost_of_gas)//1
sedan_hybrid_high_cost = (sedan_hybrid_gals*high_cost_of_gas)//1

print("Sedan hybrid drivers in Oregon use about", sedan_hybrid_gals,"gallons of gas in a year.")
print("It costs them about $", sedan_hybrid_low_cost, "when gas is cheap, and $", sedan_hybrid_high_cost,"when gas is spendy.")

suv_gals = miles//suv
suv_low_cost = suv_gals*low_cost_of_gas//1
suv_high_cost = suv_gals*high_cost_of_gas//1

print("SUV drivers in Oregon use about", suv_gals,"gallons of gas in a year.")
print("It costs them about $", suv_low_cost, "when gas is cheap, and $", suv_high_cost, "when gas is spendy.")

suv_hybrid_gals = miles//suv_hybrid
suv_hybrid_low_cost = suv_hybrid_gals*low_cost_of_gas//1
suv_hybrid_high_cost = suv_hybrid_gals*high_cost_of_gas//1

print("SUV hybrid drivers in Oregon use about", suv_hybrid_gals,"gallons of gas in a year.")
print("It costs them about $", suv_hybrid_low_cost, "when gas is cheap, and $", suv_hybrid_high_cost,"when gas is spendy.")

tesla_kwh = miles/tesla*33.7//1  #including mpge conversion to kwh's
tesla_low_cost = tesla_kwh*low_cost_of_power//1
tesla_high_cost = tesla_kwh*high_cost_of_power//1

print("The fortunate souls that pilot Teslas use about", tesla_kwh,"kilowatt-hours per year.")
print("It costs them about $", tesla_low_cost,"to get all that electricity at home, and about $", tesla_high_cost,"to get it at charging stations.")

bolt_kwh = miles/bolt*33.7//1 #mpge conversion
bolt_low_cost = bolt_kwh*low_cost_of_power//1
bolt_high_cost = bolt_kwh*high_cost_of_power//1

print("Normal electric car drivers, with vehicles like a Chevy Bolt, use about", bolt_kwh, "kilowatt-hours per year.")
print("It costs them about $", bolt_low_cost, "to get all that eletricity at home, and about $", bolt_high_cost,"to get it at charging stations.")