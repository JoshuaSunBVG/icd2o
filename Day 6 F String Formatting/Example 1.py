average = 12.65675765
print(f"{average}")     # 12.65675765
print(f"{average:.2f}") # rounds to 2 decimal places -> 12.66
print(f"{average:.3f}") #12.657

number = 6.1
print(f"{number:.2f}")  # 6.10

number = 6
print(f"{number:.2f}")  # 6.00

math_mark = 34
math_total = 45

math_average = math_mark / math_total

print(f"{math_average}")       # 0.755555555
print(f"{math_average:.1%}")   # 75.6%
print(f"{math_average:.1f}")   # 0.8



x = 54.547545647564754
print(f"{x}")
print(f"{x:.5f}")
print(f"{x:.5}")
print(f"{x:.2}") #5.5e+01 -> scientific notation 5.5 x 10^1
print(f"{x:.3}") #54.5
print(f"{x:.1}") # 5e+01 -> scientific notation 5 x 10^1

y = 5.6585634654
print(f"{y:.1}")    # 6e+00 -> scientific notation 6 x 10^0