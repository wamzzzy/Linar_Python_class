#write a python code to calculate the the total number of blocks and the total cost of building a python structure(4 rooms and a toilet) using either 600naira block or 1000naira block.
#dimension for 600naira block given as 6"by9"by15" and 1000naira block given as 10"by12"by20"
#with the customer specifying the dimensions of the rooms and toilet of the building
#with a constant room height of 12ft

print("Hello!\nWelcome to AM Building Nigeria Limited")

import math

Dimensions_room1 = {"h1":int(input("Enter dimensiion for room 1\nEnter length (figures only): ")),"b1":int(input("Enter breadth (figures only): "))}
Dimensions_room2 = {"h2":int(input("Enter dimensiion for room 2\nEnter length (figures only): ")),"b2":int(input("Enter breadth (figures only): "))}
Dimensions_room3 = {"h3":int(input("Enter dimensiion for room 3\nEnter length (figures only): ")),"b3":int(input("Enter breadth (figures only): "))}
Dimensions_room4 = {"h4":int(input("Enter dimensiion for room 4\nEnter length (figures only): ")),"b4":int(input("Enter breadth (figures only): "))}
Dimensions_toilet ={"h5":int(input("Enter dimensiion for toilet\nEnter length (figures only): ")),"b5":int(input("Enter breadth (figures only): "))}

room_height = 12

#Calculating for first room
#calculation to get number of blocks and the total cost for 600naira block for first room
block_type1_height = 0.75 #The height of the block have been coverted to feet
block_type1_breadth = 1.25 #The breadth of the block have been converted to feet
r1 = room_height/block_type1_height
r111 = Dimensions_room1["h1"]/block_type1_height
r1111 = math.ceil(r111)
r11 = (r1111*r1)*2
r122 = Dimensions_room1["b1"]/block_type1_breadth
r1222 = math.ceil(r122)
r12 = (r1222*r1)*2
no_of_blocks1_room1 = r11+r12
cost_type1_room1 = no_of_blocks1_room1*600

#calculation to get number of blocks and the total cost for 1000naira block for first room
block_type2_height = 1 #The height of the block have been coverted to feet
block_type2_breadth = 1.67 #The breadth of the block have been coverted to feet
r2 = room_height/block_type2_height
r211 = Dimensions_room1["h1"]/block_type2_height
r2111 = math.ceil(r211)
r21 = (r2111*r2)*2
r222 = Dimensions_room1["b1"]/block_type2_breadth
r2222 = math.ceil(r222)
r22 = (r2222*r2)*2
no_of_blocks2_room1 = r22+r21
cost_type2_room1 = no_of_blocks2_room1*1000

#clculating for second room
#calculation to get number of blocks and the total cost for type1 block for second room
rr111 = Dimensions_room2["h2"]/block_type1_height
rr1111 = math.ceil(rr111)
rr11 = (rr1111*r1)*2
rr122 = Dimensions_room2["b2"]/block_type1_breadth
rr1222 = math.ceil(rr122)
rr12 = (rr1222*r1)*2
no_of_blocks1_room2 = rr11+rr12
cost_type1_room2 = no_of_blocks1_room2*600

#calculation to get number of blocks and the total cost for type2 block for second room
rr211 = Dimensions_room2["h2"]/block_type2_height
rr2111 = math.ceil(rr211)
rr21 = (rr2111*r2)*2
rr222 = Dimensions_room2["b2"]/block_type2_breadth
rr2222 = math.ceil(rr222)
rr22 = (rr2222*r2)*2
no_of_blocks2_room2 = rr22+rr21
cost_type2_room2 = no_of_blocks2_room2*1000

#clculating for third room
#calculation to get number of blocks and the total cost for type1 block for third room
rrr111 = Dimensions_room3["h3"]/block_type1_height
rrr1111 = math.ceil(rrr111)
rrr11 = (rrr1111*r1)*2
rrr122 = Dimensions_room3["b3"]/block_type1_breadth
rrr1222 = math.ceil(rrr122)
rrr12 = (rrr1222*r1)*2
no_of_blocks1_room3 = rrr11+rrr12
cost_type1_room3 = no_of_blocks1_room3*600

#calculation to get number of blocks and the total cost for type2 block for third room
rrr211 = Dimensions_room3["h3"]/block_type2_height
rrr2111 = math.ceil(rrr211)
rrr21 = (rrr2111*r2)*2
rrr222 = Dimensions_room3["b3"]/block_type2_breadth
rrr2222 = math.ceil(rrr222)
rrr22 = (rrr2222*r2)*2
no_of_blocks2_room3 = rrr22+rrr21
cost_type2_room3 = no_of_blocks2_room3*1000

#clculating for fourth room
#calculation to get number of blocks and the total cost for type1 block for fourth room
rrrr111 = Dimensions_room4["h4"]/block_type1_height
rrrr1111 = math.ceil(rrrr111)
rrrr11 = (rrrr1111*r1)*2
rrrr122 = Dimensions_room4["b4"]/block_type1_breadth
rrrr1222 = math.ceil(rrrr122)
rrrr12 = (rrrr1222*r1)*2
no_of_blocks1_room4 = rrrr11+rrrr12
cost_type1_room4 = no_of_blocks1_room4*600

#calculation to get number of blocks and the total cost for type2 block for fourth room
rrrr211 = Dimensions_room4["h4"]/block_type2_height
rrrr2111 = math.ceil(rrrr211)
rrrr21 = (rrrr2111*r2)*2
rrrr222 = Dimensions_room4["b4"]/block_type2_breadth
rrrr2222 = math.ceil(rrrr222)
rrrr22 = (rrrr2222*r2)*2
no_of_blocks2_room4 = rrrr22+rrrr21
cost_type2_room4 = no_of_blocks2_room4*1000

#clculating for the toilet
#calculation to get number of blocks and the total cost for type1 block for the toilet
t111 = Dimensions_toilet["h5"]/block_type1_height
t1111 = math.ceil(t111)
t11 = (t1111*r1)*2
t122 = Dimensions_toilet["b5"]/block_type1_breadth
t1222 = math.ceil(t122)
t12 = (t1222*r1)*2
no_of_blocks1_toilet = t11+t12
cost_type1_toilet = no_of_blocks1_toilet*600

#calculation to get number of blocks and the total cost for type2 block for the toilet
t211 = Dimensions_toilet["h5"]/block_type2_height
t2111 = math.ceil(t211)
t21 = (t2111*r2)*2
t222 = Dimensions_toilet["b5"]/block_type2_breadth
t2222 = math.ceil(t222)
t22 = (t2222*r2)*2
no_of_blocks2_toilet = t22+t21
cost_type2_toilet = no_of_blocks2_toilet*1000

#calculating the total number of blocks and total cost
total_no_of_blocks1 = no_of_blocks1_room1+no_of_blocks1_room2+no_of_blocks1_room3+no_of_blocks1_room4+no_of_blocks1_toilet
total_no_of_blocks2 = no_of_blocks2_room1+no_of_blocks2_room2+no_of_blocks2_room3+no_of_blocks2_room4+no_of_blocks2_toilet
total_cost1 = cost_type1_room1+cost_type1_room2+cost_type1_room3+cost_type1_room4+cost_type1_toilet
total_cost2 = cost_type2_room1+cost_type2_room2+cost_type2_room3+cost_type2_room4+cost_type2_toilet
int_total_blocks1 = int(total_no_of_blocks1)
int_total_blocks2 = int(total_no_of_blocks2)
int_total_cost1 = int(total_cost1)
int_total_cost2 = int(total_cost2)

print(f"The total number of blocks for 600naira block is {int_total_blocks1} blocks and the total cost of blocks for 600naira block is {int_total_cost1} naira")
print(f"The total number of blocks for 1000naira block is {int_total_blocks2} blocks and the total cost of blocks for 1000naira block is {int_total_cost2} naira")
print("Thanks for choosing AM Building Nigeria Limited")