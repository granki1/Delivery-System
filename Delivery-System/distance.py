import csv
import datetime

# Reads CSV
with open('./data/distances.csv') as csvfile_1:
    distances_csv = list(csv.reader(csvfile_1, delimiter=','))
with open('./data/addresses.csv') as csvfile_2:
    addresses_csv = list(csv.reader(csvfile_2, delimiter=','))

    # Retrieves addresses
    def get_address():
        return addresses_csv

    # Calculates total distance
    def get_distance(row, col, total):
        distance = distances_csv[row][col]
        if distance == '':
            distance = distances_csv[col][row]

        return total + float(distance)

    # Calculates current distance
    def get_current_distance(row, col):
        distance = distances_csv[row][col]
        if distance == '':
            distance = distances_csv[col][row]

        return float(distance)

    # Calculates total distance for truck
    def get_time(distance, truck_list):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
        total = datetime.timedelta()
        for i in truck_list:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs),
                                        minutes=int(mins), seconds=int(secs))
        return total

    # Lists for sorted trucks
    first_truck = []
    first_truck_indices = []
    second_truck = []
    second_truck_indices = []
    final_truck = []
    final_truck_indices = []

    def get_shortest_route(_list, num, curr_location):
        if not len(_list):
            return _list

        lowest_value = 50.0
        location = 0

        for i in _list:
            value = int(i[1])
            if get_current_distance(curr_location, value) <= lowest_value:
                lowest_value = get_current_distance(
                    curr_location, value)
                location = value

        for i in _list:
            if get_current_distance(curr_location, int(i[1])) == lowest_value:
                if num == 1:
                    first_truck.append(i)
                    first_truck_indices.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    get_shortest_route(_list, 1, curr_location)
                elif num == 2:
                    second_truck.append(i)
                    second_truck_indices.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    get_shortest_route(_list, 2, curr_location)
                elif num == 3:
                    final_truck.append(i)
                    final_truck_indices.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    get_shortest_route(_list, 3, curr_location)

    # Start indices at 0
    first_truck_indices.insert(0, '0')
    second_truck_indices.insert(0, '0')
    final_truck_indices.insert(0, '0')

    # Returns values
    def first_truck_index():
        return first_truck_indices

    def first_truck_list():
        return first_truck

    def second_truck_index():
        return second_truck_indices

    def second_truck_list():
        return second_truck

    def final_truck_index():
        return final_truck_indices

    def final_truck_list():
        return final_truck