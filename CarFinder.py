AllowedVehiclesList = [
    'Ford F-150',
    'Chevrolet Silverado',
    'Tesla CyberTruck',
    'Toyota Tundra',
    'Nissan Titan'
]

def print_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
    print()

def main():
    while True:
        print_menu()
        user_input = input()

        if user_input == "1":
            print_vehicles()
        elif user_input == "2":
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("\nInvalid input. Please enter 1 or 2.\n")

    input()

