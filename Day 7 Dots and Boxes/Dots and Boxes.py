name = input("What is your name: ")
print()

print("Game #1")
game_1_opp = input("Who was your opponent: ")
game_1_p_1 = int(input("What was your score: "))
game_1_p_2 = int(input("What was their score: "))
print()

print("Game #2")
game_2_opp = input("Who was your opponent: ")
game_2_p_1 = int(input("What was your score: "))
game_2_p_2 = int(input("What was their score: "))
print()

print("Game #3")
game_3_opp = input("Who was your opponent: ")
game_3_p_1 = int(input("What was your score: "))
game_3_p_2 = int(input("What was their score: "))
print()

print("Game #4")
game_4_opp = input("Who was your opponent: ")
game_4_p_1 = int(input("What was your score: "))
game_4_p_2 = int(input("What was their score: "))
print()

print("Game #5")
game_5_opp = input("Who was your opponent: ")
game_5_p_1 = int(input("What was your score: "))
game_5_p_2 = int(input("What was their score: "))
print()

total_points_p_1 = game_1_p_1 + game_2_p_1 + game_3_p_1 + game_4_p_1 + game_5_p_1
total_points_p_2 = game_1_p_2 + game_2_p_2 + game_3_p_2 + game_4_p_2 + game_5_p_2
print()

percent_boxes_p_1 = total_points_p_1 / 5 * 36
print()

print("Dots and Boxes Score Tracker: ")
print()

print(f"Player's Name: {name}")
print()

print(f"{'Opponent':<10} {'Your Points':>5} {'Opponent Points':>10} {'Box %':>15}")