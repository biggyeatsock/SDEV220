class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        
        #Calling in the __init__ of the parent class
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # Usage of the class
    # vehicle_type = "car" to set the vehicle to car 
    # year = "2020" to set the year of the vehicle
    # make = "Toyota" to set the make of the vehicle
    # model = "Camry" to set the model of the vehicle
    # doors = "4" to set the number of doors of the vehicle
    # roof = "solid" to set the type of roof of the vehicle   

def vehicle_print(user_car): # Printer babyyeeeee WOOOOOOOOOOOO
    print("\nVehicle Type:", user_car.vehicle_type)
    print("Year:", user_car.year)
    print("Make:", user_car.make)
    print("Model:", user_car.model)
    print("Doors:", user_car.doors)
    print("Roof:", user_car.roof)

def main():
    vehicle_type_input = input("Enter the type of vehicle (Car or Truck): ")
    try:
        vehicle_year_input = int(input("Enter the year of the vehicle: "))
    except ValueError:  # Handle invalid input (non-integer)
        print("Invalid input. Please enter a valid year.\n")
        while ValueError:
            try:
                vehicle_year_input = int(input("Enter the year of the vehicle: "))
                break 

            except ValueError: # This will constantly be in a loop to make sure the user inputs the correct value.
                print("Invalid input. Please enter a valid year.\n")
                continue
        
    vehicle_make_input = input("Enter the make of the vehicle: ")
    vehicle_model_input = input("Enter the model of the vehicle: ")

    try: # Vehicle doors input
        vehicle_doors_input = int(input("Enter the number of doors of the vehicle (2 or 4): "))
        if vehicle_doors_input not in(2,4):
            raise ValueError("Invalid input. Please enter a valid number of doors. (2 or 4)")
        
    except ValueError:  # Handle invalid input (non-integer)
        print("Invalid input. Please enter a valid number of doors.\n")
        while ValueError:
            try:
                vehicle_doors_input = int(input("Enter the number of doors of the vehicle (2 or 4): "))
                if vehicle_doors_input in (2,4):
                    break
                else:
                    raise ValueError("Invalid input. Please enter a valid number of doors. (2 or 4)")
            except ValueError: # This will constantly be in a loop to make sure the user inputs the correct value.
                print(f"Error: {ValueError}")
                
        
    vehicle_roof_input = input("Enter the type of roof of the vehicle (Solid or Sunroof): ")

    user_car = Automobile( # This assigns everything to the class values.
        vehicle_type=vehicle_type_input,
        year=vehicle_year_input,
        make=vehicle_make_input,
        model=vehicle_model_input,
        doors=vehicle_doors_input,
        roof=vehicle_roof_input,
    )

    vehicle_print(user_car)

if __name__ == "__main__":
    main()
