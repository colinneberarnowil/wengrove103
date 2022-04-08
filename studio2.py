#######################################################################
# Program Filename: studio2
# Author: Colin Wilson
# Date: 4/5/22
# Description: calculating gallons of gas per person in Oregon in 2019
# Input: gallons of gas total sold in Oregon in 2019, number of Oregonians with a license in 2019
# Output: gal/capita in Oregon in 2019
#######################################################################

# monthly gallons of gas sold in Oregon in 2019, in thousands of gallons per day
jan = 97.7
feb = 99.7
mar = 104.3
apr = 103.8
may = 101.4
jun = 110.2
jul = 110.7
aug = 112.2
sep = 106.1
oct = 112.4
nov = 98.3
dec = 105.8

monthly_average = (jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec)/12

yearly_total = monthly_average*365000 #convert to gallons and expand to a whole year

drivers = 3148455 #active licenses in Oregon in 2019

gallons_per_capita = yearly_total/drivers

print("Driving Oregonians used an average of",gallons_per_capita,"gallons of gas per person in 2019.")

miles_peryear_perperson = 14032 #average driving per FHWA
