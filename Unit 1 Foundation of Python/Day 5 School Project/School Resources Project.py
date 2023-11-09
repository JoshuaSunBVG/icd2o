print("Welcome to the BVG Resources Program")
print()
print("Location: Upper School")
print()

print("Data Collection: ")
print()

print("Water Fountains: ")
num_fountains = int(input("Enter the number of water fountains: "))
fountain_locations = input("Enter the locations of water fountains: ")
fountain_conditions = input("Describe the condition of the water fountains: ")
print()

print("Restrooms: ")
num_washrooms = int(input("Enter the number of restrooms:"))
washroom_locations = input("Enter the locations of restrooms: ")
washroom_cleanliness = input("Describe the cleanliness of the restrooms: ")
print()

print("Cafeteria: ")
cafeteria_capacity = int(input("Enter the seating capacity of the cafeteria: "))
cafeteria_daily_attendance = int(input("Enter the average daily attendance in the cafeteria: "))
cafeteria_condition = input("Describe the condition of the cafeteria: ")
print()

print("Classrooms: ")
num_classrooms = int(input("Enter the total number of classrooms: "))
print()


average_fountains_per_classroom = num_fountains / num_classrooms
average_washrooms_per_classroom = num_washrooms / num_classrooms

print("Data Collected: ")
print()

print("Water Fountains: ")
print(f"Number of Water Fountains: {num_fountains}")
print(f"Locations: {fountain_locations}")
print(f"Condition: {fountain_conditions}")
print()

print("Restrooms: ")
print(f"Number of Restrooms: {num_washrooms}")
print(f"Locations: {washroom_locations}")
print(f"Cleanliness: {washroom_cleanliness}")
print()


print("Cafeteria: ")
print(f"Seating Capacity: {cafeteria_capacity}")
print(f"Average Daily Attendance: {cafeteria_daily_attendance}")
print(f"Condition: {cafeteria_condition}")
print()

print("Classrooms: ")
print(f"Total Number of Classrooms: {num_classrooms}")
print(f"Number of Water Fountains per Classroom: {average_fountains_per_classroom}")
print(f"Number of Restrooms per Classroom: {average_washrooms_per_classroom}")
print()