# Glen Rankin Student ID: 001201268

from csv_reader import get_hash_map
from packages import total_distance
from packages import first_delivery
from packages import second_delivery
from packages import final_delivery
import datetime

class Main:
    # Display Message
    print("")
    print('WGUPS Routing')
    print(f'Total Distance Traveled: {total_distance():.2f} miles\n') 

    user_input = input("""
    Input "All" for All Package Info
    Input "One" for Specific Package Info
                       
    Or Type "Exit" to End Program
""")

    while user_input.lower() != 'exit':
        # Status of All Packages
        if user_input.lower() == 'all':
            try:
                input_time = input('Enter Time HH:MM:SS: ')
                (hrs, mins, secs) = input_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                for count in range(1,41):
                    try:
                        first_time = get_hash_map().get_value(str(count))[9]
                        second_time = get_hash_map().get_value(str(count))[10]
                        (hrs, mins, secs) = first_time.split(':')
                        convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                        (hrs, mins, secs) = second_time.split(':')
                        convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    except ValueError: pass
                    
                    # Which packages have left
                    if convert_first_time >= convert_user_time:
                        get_hash_map().get_value(str(count))[10] = 'At Hub'
                        get_hash_map().get_value(str(count))[9] = 'Leaves At ' + first_time

                        # Shows Status
                        print(
                            f'{get_hash_map().get_value(str(count))[0]}, '
                            f'{get_hash_map().get_value(str(count))[10]}, '
                            f'{get_hash_map().get_value(str(count))[2]}, '
                            f'{get_hash_map().get_value(str(count))[3]}, '
                            f'{get_hash_map().get_value(str(count))[4]}, '
                            f'{get_hash_map().get_value(str(count))[5]}, '
                            f'{get_hash_map().get_value(str(count))[7]}, '
                            f'Deadline: {get_hash_map().get_value(str(count))[6]}, '
                            f'{get_hash_map().get_value(str(count))[9]}, '
                            f'Delivery By: {get_hash_map().get_value(str(count))[11]}'
                        )

                    # Which packages are en route
                    elif convert_first_time <= convert_user_time:
                        if convert_user_time < convert_second_time:
                            get_hash_map().get_value(str(count))[10] = 'In transit'
                            get_hash_map().get_value(str(count))[9] = 'Left At ' + first_time

                            # Shows Status
                            print(
                                f'{get_hash_map().get_value(str(count))[0]}, '
                                f'{get_hash_map().get_value(str(count))[10]}, '
                                f'{get_hash_map().get_value(str(count))[2]}, '
                                f'{get_hash_map().get_value(str(count))[3]}, '
                                f'{get_hash_map().get_value(str(count))[4]}, '
                                f'{get_hash_map().get_value(str(count))[5]}, '
                                f'{get_hash_map().get_value(str(count))[7]}, '
                                f'Deadline: {get_hash_map().get_value(str(count))[6]}, '
                                f'{get_hash_map().get_value(str(count))[9]}, '
                                f'Delivery By: {get_hash_map().get_value(str(count))[11]}'
                            )

                        # Which packages are delivered
                        else:
                            get_hash_map().get_value(str(count))[10] = 'Delivered ' + second_time
                            get_hash_map().get_value(str(count))[9] = 'Left At ' + first_time

                            # Shows Status
                            print(
                                f'{get_hash_map().get_value(str(count))[0]}, '
                                f'{get_hash_map().get_value(str(count))[10]}, '
                                f'{get_hash_map().get_value(str(count))[2]}, '
                                f'{get_hash_map().get_value(str(count))[3]}, '
                                f'{get_hash_map().get_value(str(count))[4]}, '
                                f'{get_hash_map().get_value(str(count))[5]}, '
                                f'{get_hash_map().get_value(str(count))[7]}, '
                                f'Deadline: {get_hash_map().get_value(str(count))[6]}, '
                                f'{get_hash_map().get_value(str(count))[9]}, '
                                f'Delivery By: {get_hash_map().get_value(str(count))[11]}'
                                )

            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid')
                exit()
    
        # Status of Specific Package
        elif user_input.lower() == 'one':
            try:
                count = input('Enter Package ID: ')
                first_time = get_hash_map().get_value(str(count))[9]
                second_time = get_hash_map().get_value(str(count))[10]
                input_time = input('Enter Time (HH:MM:SS): ')
                (hrs, mins, secs) = input_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = first_time.split(':')
                convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = second_time.split(':')
                convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                # Which packages have left
                if convert_first_time >= convert_user_time:

                    get_hash_map().get_value(str(count))[10] = 'At Hub'
                    get_hash_map().get_value(str(count))[9] = 'Leaves at ' + first_time
                    
                    # Shows Status
                    print(
                                f'{get_hash_map().get_value(str(count))[0]}, '
                                f'{get_hash_map().get_value(str(count))[10]}, '
                                f'{get_hash_map().get_value(str(count))[2]}, '
                                f'{get_hash_map().get_value(str(count))[3]}, '
                                f'{get_hash_map().get_value(str(count))[4]}, '
                                f'{get_hash_map().get_value(str(count))[5]}, '
                                f'{get_hash_map().get_value(str(count))[7]}, '
                                f'Deadline: {get_hash_map().get_value(str(count))[6]}, '
                                f'{get_hash_map().get_value(str(count))[9]}, '
                                f'Delivery By: {get_hash_map().get_value(str(count))[11]}'
                    )

                # Which packages are en route
                elif convert_first_time <= convert_user_time:
                    if convert_user_time < convert_second_time:
                        get_hash_map().get_value(str(count))[10] = 'In Transit'
                        get_hash_map().get_value(str(count))[9] = 'Left At ' + first_time

                        # Shows Status
                        print(
                                f'{get_hash_map().get_value(str(count))[0]}, '
                                f'{get_hash_map().get_value(str(count))[10]}, '
                                f'{get_hash_map().get_value(str(count))[2]}, '
                                f'{get_hash_map().get_value(str(count))[3]}, '
                                f'{get_hash_map().get_value(str(count))[4]}, '
                                f'{get_hash_map().get_value(str(count))[5]}, '
                                f'{get_hash_map().get_value(str(count))[7]}, '
                                f'Deadline: {get_hash_map().get_value(str(count))[6]}, '
                                f'{get_hash_map().get_value(str(count))[9]}, '
                                f'Delivery By: {get_hash_map().get_value(str(count))[11]}'
                        )

                    # Which packages have been delivered
                    else:
                        get_hash_map().get_value(str(count))[10] = 'Delivered ' + second_time
                        get_hash_map().get_value(str(count))[9] = 'Left At ' + first_time

                        # Shows Status
                        print(
                                f'{get_hash_map().get_value(str(count))[0]}, '
                                f'{get_hash_map().get_value(str(count))[10]}, '
                                f'{get_hash_map().get_value(str(count))[2]}, '
                                f'{get_hash_map().get_value(str(count))[3]}, '
                                f'{get_hash_map().get_value(str(count))[4]}, '
                                f'{get_hash_map().get_value(str(count))[5]}, '
                                f'{get_hash_map().get_value(str(count))[7]}, '
                                f'Deadline: {get_hash_map().get_value(str(count))[6]}, '
                                f'{get_hash_map().get_value(str(count))[9]}, '
                                f'Delivery By: {get_hash_map().get_value(str(count))[11]}'
                        )

            except ValueError:
                print('Invalid')
                exit()

        # End Program
        elif user_input.lower() == 'exit':
            exit()

        # Anything else will present error and exit program
        else:
            print('Error, Please Rerun Program')
            exit()