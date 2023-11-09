def input_bug_counts(bug_type):
    count = int(input(f"Enter the amount of {bug_type}: "))
    print()
    return count

def calculate_percent(total, count):
    percent = count / total
    return percent

def input_bug_type_and_count():
    bug_type = input("Enter the type of bug: ")
    count = input_bug_counts(bug_type)
    return bug_type, count

def display_table(bug_1, count_1, bug_2, count_2, bug_3, count_3):
    total = count_1 + count_2 + count_3
    total_percent = (count_1 / total) + (count_2 / total) + (count_3 / total)
    print(f"{'Bug Type':<10} {'Count':>20} {'Percentage':>15}")
    print("="*47)
    print(f"{bug_1:<10} {count_1:>20} {calculate_percent(total, count_1):>15.2%}")
    print(f"{bug_2:<10} {count_2:>20} {calculate_percent(total, count_2):>15.2%}")
    print(f"{bug_3:<10} {count_3:>20} {calculate_percent(total, count_3):>15.2%}")
    print("="*47)
    print(f"{'Total':<10} {total:>20} {total_percent:>15.2%} ")
    print()

bug_1, count_1 = input_bug_type_and_count()
bug_2, count_2 = input_bug_type_and_count()
bug_3, count_3 = input_bug_type_and_count()

display_table(bug_1, count_1, bug_2, count_2, bug_3, count_3)