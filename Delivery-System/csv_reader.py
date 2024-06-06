import csv
from hash_table import HashMap

with open('./data/packages.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')

    hash_map = HashMap()  # Creates HashMap
    first_delivery = []  # Truck One
    second_delivery = [] # Truck Two
    final_delivery = [] # Last Truck

    # Key/Value Pairs
    for row in read_csv:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        size = row[6]
        note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = ''
        truck_number = ''

        value = [id, address_location, address, city, state, zip, deadline, size, 
            note, delivery_start, delivery_status, truck_number]

        # These IF statements put package on appropriate truck.

        # Truck One
        if value[6] != 'EOD':
            if 'Must' in value[8] or '' in value[8]:
                value[11] = 'Truck One'
                first_delivery.append(value)

        # Truck Two
        if 'Can only be on truck 2' in value[8] or 'Delayed' in value[8]:
            value[11] = 'Truck Two'
            second_delivery.append(value)

        # Last Truck, which includes Package 9 special note of the wrong address
        # Address is updated at 10:20 and this truck will leave at 11:00 to allow the mistake to be corrected before departure
        if 'EOD' in value[6]:
            if 'Wrong' in value[8]:
                value[11] = 'Truck Three'
                final_delivery.append(value)

        # This if statement will update the address of any package with the note of "wrong"
        # In this case, we know the correct address of package after 10:20 so we are updating it before truck 3 leaves at 11:00
        if 'Wrong' in value [8]:
            value[2] = '410 S State St'
            value[3] = 'Salt Lake City'
            value[4] = 'UT'
            value[5] = '84111'
        
        # Check remaining packages
        if value not in first_delivery and value not in second_delivery and value not in final_delivery:
            if len(second_delivery) < len(final_delivery):
                value[11] = 'Truck Two'
                second_delivery.append(value) 
            else:
                value[11] = 'Truck Three'
                final_delivery.append(value)

        # Insert into the hash table
        hash_map.insert(id, value)

    def get_first_delivery():
        return first_delivery

    def get_second_delivery():
        return second_delivery

    def get_final_delivery():
        return final_delivery

    def get_hash_map():
        return hash_map