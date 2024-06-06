import datetime
import distance
import csv_reader

# Lists to have packages sorted and distance tracked
first_delivery = []
second_delivery = []
final_delivery = []
first_distance = []
second_distance = []
final_distance = []

# Times set for truck departure
first_leave = ['8:00:00']
second_leave = ['9:05:00']
final_leave = ['11:00:00']

# All packages on truck one are set with the first truck departure time
for index, value in enumerate(csv_reader.get_first_delivery()):
    csv_reader.get_first_delivery()[index][9] = first_leave[0]
    first_delivery.append(csv_reader.get_first_delivery()[index])
    
# Addresses for truck one are compared to the list
for index, outer in enumerate(first_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            first_distance.append(outer[0])
            first_delivery[index][1] = inner[0]

# Sorts packages on truck for shortest route
distance.get_shortest_route(first_delivery, 1, 0)
total_distance_1 = 0

# Calculates distance traveled for truck one
for index in range(len(distance.first_truck_index())):
    try:
        total_distance_1 = distance.get_distance(int(distance.first_truck_index()[index]), int(distance.first_truck_index()[index + 1]), total_distance_1)
        
        deliver_package = distance.get_time(distance.get_current_distance(int(distance.first_truck_index()[index]), int(distance.first_truck_index()[index + 1])), first_leave)
        distance.first_truck_list()[index][10] = (str(deliver_package))
        csv_reader.get_hash_map().update(int(distance.first_truck_list()[index][0]), first_delivery)
    except IndexError:
        pass

# All packages on truck two are set with the second truck departure time
for index, value in enumerate(csv_reader.get_second_delivery()):
    csv_reader.get_second_delivery()[index][9] = second_leave[0]
    second_delivery.append(csv_reader.get_second_delivery()[index])

# Addresses for truck two are compared to the list
for index, outer in enumerate(second_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            second_distance.append(outer[0])
            second_delivery[index][1] = inner[0]

# Sorts packages on truck for shortest route
distance.get_shortest_route(second_delivery, 2, 0)
total_distance_2 = 0

# Calculates distance traveled for truck two
for index in range(len(distance.second_truck_index())):
    try:
        total_distance_2 = distance.get_distance(int(distance.second_truck_index()[index]), int(distance.second_truck_index()[index + 1]), total_distance_2)
        
        deliver_package = distance.get_time(distance.get_current_distance(int(distance.second_truck_index()[index]), int(distance.second_truck_index()[index + 1])), second_leave)
        distance.second_truck_list()[index][10] = (str(deliver_package))
        csv_reader.get_hash_map().update(int(distance.second_truck_list()[index][0]), second_delivery)
    except IndexError:
        pass

# All packages on the final truck are set with the final truck departure time
for index, value in enumerate(csv_reader.get_final_delivery()):
    csv_reader.get_final_delivery()[index][9] = final_leave[0]
    final_delivery.append(csv_reader.get_final_delivery()[index])

# Addresses for the final truck are compared to the list
for index, outer in enumerate(final_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            final_distance.append(outer[0])
            final_delivery[index][1] = inner[0]

# Sorts packages on truck for shortest route
distance.get_shortest_route(final_delivery, 3, 0)
total_distance_3 = 0

# Calculates distance traveled for final truck
for index in range(len(distance.final_truck_index())):
    try:
        total_distance_3 = distance.get_distance(int(distance.final_truck_index()[index]), int(distance.final_truck_index()[index + 1]), total_distance_3)
        
        deliver_package = distance.get_time(distance.get_current_distance(int(distance.final_truck_index()[index]), int(distance.final_truck_index()[index + 1])), final_leave)
        distance.final_truck_list()[index][10] = (str(deliver_package))
        csv_reader.get_hash_map().update(int(distance.final_truck_list()[index][0]), final_delivery)
    except IndexError:
        pass

# Adds up distance traveled of all trucks
def total_distance():
    return total_distance_1 + total_distance_2 + total_distance_3