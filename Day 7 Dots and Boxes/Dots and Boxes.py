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

percent_boxes_p_1_total = total_points_p_1 / 180
print()

percent_game_1_p_1 = round(game_1_p_1 / 36, 2)
percent_game_2_p_1 = round(game_2_p_1 / 36, 2)
percent_game_3_p_1 = round(game_3_p_1 / 36, 2)
percent_game_4_p_1 = round(game_4_p_1 / 36, 2)
percent_game_5_p_1 = round(game_5_p_1 / 36, 2)

print("Dots and Boxes Score Tracker: ")
print()

print(f"Player's Name: {name}")
print()

print(f"{'Opponent':<10} {'Your Points':>20} {'Opponent Points':>25} {'Box %':>15}")
print("=========================================================================")
print(f"{game_1_opp:<10} {game_1_p_1:>20} {game_1_p_2:>25} {percent_game_1_p_1:>15.2%}")
print(f"{game_2_opp:<10} {game_2_p_1:>20} {game_2_p_2:>25} {percent_game_2_p_1:>15.2%}")
print(f"{game_3_opp:<10} {game_3_p_1:>20} {game_3_p_2:>25} {percent_game_3_p_1:>15.2%}")
print(f"{game_4_opp:<10} {game_4_p_1:>20} {game_4_p_2:>25} {percent_game_4_p_1:>15.2%}")
print(f"{game_5_opp:<10} {game_5_p_1:>20} {game_5_p_2:>25} {percent_game_5_p_1:>15.2%}")
print("=========================================================================")
print()

print(f"Summary: ")
print(f"Total Points: {total_points_p_1}")
print(f"Total Opponent Points: {total_points_p_2}")
print(f"Percentage Points Received: {percent_boxes_p_1_total:.2%}")